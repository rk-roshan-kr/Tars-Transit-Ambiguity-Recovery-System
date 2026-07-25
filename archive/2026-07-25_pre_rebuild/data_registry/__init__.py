"""
data_registry — TARS Dataset Registry Package
==============================================

Provides governance-enforced access to the TARS corpus manifests.

Usage
-----
    from data_registry import DatasetRegistry

    registry = DatasetRegistry()
    release  = registry.get_release("TARS-250K-R1")
    registry.assert_integrity("TARS-250K-R1")
"""

from .dataset_registry import DatasetRegistry, DatasetIntegrityError, DatasetNotFoundError

__all__ = ["DatasetRegistry", "DatasetIntegrityError", "DatasetNotFoundError"]
__version__ = "1.0.0"
