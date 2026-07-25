"""
data_registry.dataset_registry — TARS Dataset Registry
=======================================================

Governance-enforced loader for TARS corpus manifests.

The DatasetRegistry loads one or more ``dataset_manifest.json`` files
from the ``data_registry/`` package directory, validates their schema,
computes their SHA256 fingerprint, and provides controlled read access.

Scientific Governance Rules
---------------------------
INV-DR-1   Manifests are read-only.  The registry never writes or modifies
           a manifest after it is frozen.
INV-DR-2   SHA256 is computed on the canonical JSON bytes (keys sorted,
           indent=2).  Any out-of-band edit will change the fingerprint.
INV-DR-3   No test-split data may be accessed through this module during
           development (``test_lock_policy`` is enforced at the application
           layer; this module raises DatasetIntegrityError if the status
           field is not 'FROZEN').
INV-DR-4   ML governance: forbidden_inputs list is surfaced from the
           manifest and must be consumed by stage6_ml.ml_engine_spec.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------

class DatasetIntegrityError(RuntimeError):
    """Raised when a manifest fails schema validation or integrity check."""


class DatasetNotFoundError(KeyError):
    """Raised when a requested release_id is not present in the registry."""


# ---------------------------------------------------------------------------
# Required manifest keys (top-level)
# ---------------------------------------------------------------------------

_REQUIRED_KEYS = {
    "release_id",
    "status",
    "corpus",
    "quality_distribution",
    "provenance",
    "reproducibility",
    "ml_governance",
    "governance_frozen_at",
}

_REQUIRED_CORPUS_KEYS = {
    "target_count",
    "completed_count",
    "fits_on_disk",
}

_REQUIRED_ML_KEYS = {
    "forbidden_inputs",
    "physics_veto_invariant",
}


# ---------------------------------------------------------------------------
# DatasetRegistry
# ---------------------------------------------------------------------------

class DatasetRegistry:
    """
    Loads and validates TARS corpus manifests from the ``data_registry/``
    directory.  Multiple manifests are supported (one per release).

    Parameters
    ----------
    registry_dir : str or Path, optional
        Directory containing ``dataset_manifest.json`` files.
        Defaults to the directory where this module lives.

    Example
    -------
    >>> registry = DatasetRegistry()
    >>> release = registry.get_release("TARS-250K-R1")
    >>> registry.assert_integrity("TARS-250K-R1")
    """

    _FROZEN_SHA256 = {
        "TARS-250K-R1": "47ad809e296f509d7da6a3abe7648663a6b58e671ca71305c402aa7dcbce6046"
    }

    def __init__(self, registry_dir: Optional[str | Path] = None):
        if registry_dir is None:
            registry_dir = Path(__file__).parent
        self._dir = Path(registry_dir)
        self._releases: Dict[str, Dict[str, Any]] = {}
        self._sha256:   Dict[str, str]            = {}
        self._load_all()
        for r_id in self.list_releases():
            self.assert_integrity(r_id)

    # ------------------------------------------------------------------
    # Loading
    # ------------------------------------------------------------------

    def _load_all(self) -> None:
        """Scan ``registry_dir`` for all ``*.json`` manifests and load them."""
        manifest_files = sorted(self._dir.glob("*.json"))
        if not manifest_files:
            raise DatasetIntegrityError(
                f"No JSON manifests found in registry directory: {self._dir}"
            )
        for path in manifest_files:
            self._load_manifest(path)

    def _load_manifest(self, path: Path) -> None:
        """Load, validate, and fingerprint a single manifest file."""
        raw_bytes = path.read_bytes()
        try:
            data = json.loads(raw_bytes)
        except json.JSONDecodeError as exc:
            raise DatasetIntegrityError(
                f"Manifest {path.name} is not valid JSON: {exc}"
            ) from exc

        # Schema validation
        self._validate_schema(data, path.name)

        release_id = data["release_id"]

        # Compute canonical SHA256 (sorted keys, indent=2)
        canonical = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)
        sha256 = hashlib.sha256(canonical.encode("utf-8")).hexdigest()

        self._releases[release_id] = data
        self._sha256[release_id]   = sha256

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def _validate_schema(self, data: Dict[str, Any], filename: str) -> None:
        """Raise DatasetIntegrityError if required keys are missing."""
        missing_top = _REQUIRED_KEYS - set(data.keys())
        if missing_top:
            raise DatasetIntegrityError(
                f"Manifest '{filename}' missing required top-level keys: {missing_top}"
            )

        corpus = data.get("corpus", {})
        missing_corpus = _REQUIRED_CORPUS_KEYS - set(corpus.keys())
        if missing_corpus:
            raise DatasetIntegrityError(
                f"Manifest '{filename}' corpus section missing keys: {missing_corpus}"
            )

        ml = data.get("ml_governance", {})
        missing_ml = _REQUIRED_ML_KEYS - set(ml.keys())
        if missing_ml:
            raise DatasetIntegrityError(
                f"Manifest '{filename}' ml_governance section missing keys: {missing_ml}"
            )

        if not isinstance(ml.get("forbidden_inputs"), list):
            raise DatasetIntegrityError(
                f"Manifest '{filename}' ml_governance.forbidden_inputs must be a list."
            )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def list_releases(self) -> List[str]:
        """Return all loaded release IDs."""
        return list(self._releases.keys())

    def get_release(self, release_id: str) -> Dict[str, Any]:
        """
        Return the manifest dict for a given release ID.

        Parameters
        ----------
        release_id : str
            e.g. "TARS-250K-R1"

        Raises
        ------
        DatasetNotFoundError
            If the release_id is not present.
        """
        if release_id not in self._releases:
            raise DatasetNotFoundError(
                f"Release '{release_id}' not found. Available: {self.list_releases()}"
            )
        return self._releases[release_id]

    def get_sha256(self, release_id: str) -> str:
        """
        Return the SHA256 fingerprint of the canonical manifest JSON.

        This fingerprint is stable across machines for identical manifest
        content (sorted keys, UTF-8 encoded).
        """
        if release_id not in self._sha256:
            raise DatasetNotFoundError(release_id)
        return self._sha256[release_id]

    def get_forbidden_inputs(self, release_id: str) -> List[str]:
        """
        Return the ML forbidden feature list for the given release.

        These must be enforced by ``stage6_ml.ml_engine_spec``.
        """
        release = self.get_release(release_id)
        return release["ml_governance"]["forbidden_inputs"]

    def get_completed_count(self, release_id: str) -> int:
        """Return the number of COMPLETED FITS files in the corpus."""
        return self.get_release(release_id)["corpus"]["completed_count"]

    def get_physics_veto_invariant(self, release_id: str) -> str:
        """Return the physics veto invariant statement."""
        return self.get_release(release_id)["ml_governance"]["physics_veto_invariant"]

    def assert_integrity(self, release_id: str) -> None:
        """
        Assert that the manifest for a given release is internally consistent.

        Checks
        ------
        1. release_id field matches the requested ID.
        2. completed_count ≥ target_count (corpus target met).
        3. forbidden_inputs is a non-empty list.
        4. physics_veto_invariant is a non-empty string.
        5. status == 'FROZEN'.

        Raises
        ------
        DatasetIntegrityError
            If any check fails.
        """
        release = self.get_release(release_id)

        # Check 1: release_id matches
        if release["release_id"] != release_id:
            raise DatasetIntegrityError(
                f"release_id mismatch: manifest says '{release['release_id']}', "
                f"requested '{release_id}'."
            )

        # Check 2: corpus target met
        completed = release["corpus"]["completed_count"]
        target    = release["corpus"]["target_count"]
        if completed < target:
            raise DatasetIntegrityError(
                f"Corpus target not met: {completed} completed < {target} target."
            )

        # Check 3: forbidden_inputs non-empty
        forbidden = release["ml_governance"]["forbidden_inputs"]
        if not forbidden:
            raise DatasetIntegrityError(
                "ml_governance.forbidden_inputs is empty — governance invariant violated."
            )

        # Check 4: physics veto non-empty
        veto = release["ml_governance"]["physics_veto_invariant"]
        if not veto:
            raise DatasetIntegrityError(
                "ml_governance.physics_veto_invariant is empty — governance invariant violated."
            )

        # Check 5: status frozen
        if release["status"] != "FROZEN":
            raise DatasetIntegrityError(
                f"Corpus status is '{release['status']}', expected 'FROZEN'. "
                "Run Phase 10.2 freeze protocol before use."
            )

        # Check 6: Immutability check for frozen releases
        expected_sha = self._FROZEN_SHA256.get(release_id)
        actual_sha = self.get_sha256(release_id)
        if expected_sha and actual_sha != expected_sha:
            raise DatasetIntegrityError(
                f"Release '{release_id}' has been modified! Expected SHA256: {expected_sha}, "
                f"got: {actual_sha}. (Immutability violation)"
            )

    def get_labeled_subset(self, release_id: str = "TARS-250K-R1") -> Any:
        """
        Cross-reference completed files in the database against TOI catalog.
        Categorize into Tiers A, B, C, D, and deterministically assign Train/Val/Test split via TIC hash.
        
        Returns
        -------
        pandas.DataFrame
            Contains columns: tic_id, filepath, sector, toi_id, period, duration, depth, disposition, tier, split
        """
        import sqlite3
        import pandas as pd

        # Assert manifest validity first
        self.assert_integrity(release_id)
        release = self.get_release(release_id)
        db_path = release["provenance"]["database_file"]

        if not os.path.exists(db_path):
            raise DatasetIntegrityError(f"Database file not found: {db_path}")

        # 1. Query database for completed light curves
        conn = sqlite3.connect(db_path)
        try:
            df_db = pd.read_sql("SELECT tic_id, filepath, sector FROM downloads WHERE status='COMPLETED'", conn)
        finally:
            conn.close()

        # Convert to string and drop potential duplicate tic_id columns
        df_db["tic_id"] = df_db["tic_id"].astype(str)

        # 2. Load TOI distribution
        # Path relative to TarsEx root
        project_root = Path(__file__).resolve().parent.parent
        toi_csv_path = project_root / "datasets" / "reference_toi_distribution.csv"
        if not toi_csv_path.exists():
            raise DatasetIntegrityError(f"TOI distribution catalog not found: {toi_csv_path}")

        df_toi = pd.read_csv(toi_csv_path)
        df_toi["tid"] = df_toi["tid"].astype(str)

        # 3. Cross-reference
        df_merged = pd.merge(df_db, df_toi, left_on="tic_id", right_on="tid", how="left")

        # Rename columns to standard schema
        df_merged = df_merged.rename(columns={
            "toi": "toi_id",
            "pl_orbper": "period",
            "pl_trandurh": "duration",
            "pl_trandep": "depth",
            "tfopwg_disp": "disposition"
        })

        # 4. Map to Label Tiers from MASTER_LABEL_REGISTRY if present
        master_csv_path = project_root / "data_registry" / "MASTER_LABEL_REGISTRY.csv"
        if master_csv_path.exists():
            df_master = pd.read_csv(master_csv_path)
            df_master["tic_id"] = df_master["tic_id"].astype(str)
            df_master_unique = df_master.drop_duplicates(subset=["tic_id"])
            df_merged = pd.merge(df_merged, df_master_unique[["tic_id", "toi_id", "label", "confidence"]], on="tic_id", how="left", suffixes=("_ref", "_master"))
            df_merged["toi_id"] = df_merged["toi_id_master"].fillna(df_merged["toi_id_ref"])

            def assign_tier_from_master(row: Any) -> str:
                if pd.isna(row["confidence"]):
                    return "Tier D"
                lbl = row["label"]
                conf = row["confidence"]
                if lbl == 1.0 and conf == 1.0:
                    return "Tier A"
                elif lbl == 1.0 and (conf == 0.75 or conf == 0.50):
                    return "Tier B"
                elif lbl == 0.0 and conf == 0.0:
                    return "Tier C"
                else:
                    return "Tier D"

            df_merged["tier"] = df_merged.apply(assign_tier_from_master, axis=1)
        else:
            # Fallback mapping
            # Tier A: Confirmed Planet (CP, KP)
            # Tier B: Planet Candidate (PC, APC)
            # Tier C: False Positive / Alarm (FP, FA)
            # Tier D: Unknown (rest)
            def assign_tier(disp: Any) -> str:
                if pd.isna(disp):
                    return "Tier D"
                disp_str = str(disp).upper().strip()
                if disp_str in ["CP", "KP"]:
                    return "Tier A"
                elif disp_str in ["PC", "APC"]:
                    return "Tier B"
                elif disp_str in ["FP", "FA"]:
                    return "Tier C"
                else:
                    return "Tier D"

            df_merged["tier"] = df_merged["disposition"].apply(assign_tier)

        # 5. Deterministic TIC-based splits via hashing
        def assign_split(tic_id_val: str) -> str:
            h = hashlib.sha256(str(tic_id_val).encode("utf-8")).hexdigest()
            score = int(h[:8], 16) % 100
            if score < 70:
                return "TRAIN"
            elif score < 80:
                return "VALIDATION"
            elif score < 90:
                return "OPTIMIZATION"
            else:
                return "BLIND"

        df_merged["split"] = df_merged["tic_id"].apply(assign_split)

        # Return clean subset
        return df_merged[[
            "tic_id", "filepath", "sector", "toi_id", "period", "duration", "depth", "disposition", "tier", "split"
        ]]

    def get_training_set(self, release_id: str = "TARS-250K-R1") -> Any:
        """
        Return the training subset: split='TRAIN' and tier in ['Tier A', 'Tier C'] only.
        """
        df = self.get_labeled_subset(release_id)
        return df[(df["split"] == "TRAIN") & (df["tier"].isin(["Tier A", "Tier C"]))]

    def get_validation_set(self, release_id: str = "TARS-250K-R1") -> Any:
        """
        Return the validation subset: split='VALIDATION' and tier in ['Tier A', 'Tier B', 'Tier C'].
        """
        df = self.get_labeled_subset(release_id)
        return df[(df["split"] == "VALIDATION") & (df["tier"].isin(["Tier A", "Tier B", "Tier C"]))]

    def get_optimization_set(self, release_id: str = "TARS-250K-R1") -> Any:
        """
        Return the optimization test subset: split='OPTIMIZATION' and tier in ['Tier A', 'Tier B', 'Tier C'].
        """
        df = self.get_labeled_subset(release_id)
        return df[(df["split"] == "OPTIMIZATION") & (df["tier"].isin(["Tier A", "Tier B", "Tier C"]))]

    def get_blind_set(self, release_id: str = "TARS-250K-R1") -> Any:
        """
        Return the blind benchmark subset: split='BLIND' and tier in ['Tier A', 'Tier B', 'Tier C'].
        """
        df = self.get_labeled_subset(release_id)
        return df[(df["split"] == "BLIND") & (df["tier"].isin(["Tier A", "Tier B", "Tier C"]))]

    def get_test_set(self, release_id: str = "TARS-250K-R1") -> Any:
        """
        Return the holdout test subset (alias for blind set): split='BLIND' and tier in ['Tier A', 'Tier B', 'Tier C'].
        """
        return self.get_blind_set(release_id)

    def summary(self, release_id: str) -> str:
        """Return a human-readable one-paragraph summary of the release."""
        r = self.get_release(release_id)
        c = r["corpus"]
        q = r["quality_distribution"]
        p = r["provenance"]
        sha = self.get_sha256(release_id)
        return (
            f"Release: {r['release_id']} | Status: {r['status']}\n"
            f"Corpus:  {c['completed_count']:,} FITS completed "
            f"(target {c['target_count']:,}) | {c['fits_on_disk']:,} on disk\n"
            f"Grades:  A={q['grade_A']:,} ({q['grade_A_pct']}%)  "
            f"B={q['grade_B']:,} ({q['grade_B_pct']}%)  "
            f"C={q['grade_C']:,} ({q['grade_C_pct']}%)\n"
            f"Mission: {p['mission']} | Cadence: {p['cadence_type']} "
            f"| Sectors: {p['sector_min']}–{p['sector_max']}\n"
            f"SHA256:  {sha}\n"
            f"Frozen:  {r['governance_frozen_at']}"
        )

