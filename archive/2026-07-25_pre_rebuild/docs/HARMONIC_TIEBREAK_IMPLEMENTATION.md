# Harmonic Tie-Break Implementation

*Phase 6.1 — Component C. Documents the implementation of the formal preference hierarchy from HARMONIC_RESOLUTION_SPECIFICATION.md Section 3.*

---

## The Gap

`HARMONIC_RESOLUTION_SPECIFICATION.md` Section 3 defines three ordered rules for selecting the fundamental period when aliases are degenerate:

1. **Event Support Preference** — more supporting events wins.
2. **Coverage Preference** — higher observable coverage fraction wins.
3. **Residual Preference** — lower residual MAD wins.

Pre-Phase 6.1 code (comment in `harmonic_resolver.py` line 76):
```python
# S3-9 / Harmonic Ambiguity tie-break is handled during final consensus ranking
```

The consensus ranker never implemented this hierarchy. It applied a linear heuristic score that could rank a $2P$ alias above the true $P$ when the alias happened to have higher coverage (because $2P$ has fewer expected transits, reducing the coverage denominator and making the fraction look better).

---

## Design: The `HarmonicEvaluationContext` Pattern

Per the user's architectural direction:
- The resolver must remain a **pure decision function**.
- It must **not** receive events, light curves, or pipeline state.
- `recoverer.py` is responsible for **measurement**; `harmonic_resolver.py` is responsible for **decision**.

The solution is a compact frozen dataclass:

```python
@dataclass(frozen=True)
class HarmonicEvaluationContext:
    period: float           # Candidate period (days)
    support_count: int      # N events satisfying the ephemeris
    coverage_fraction: float # Observable coverage fraction
    residual_mad: float     # MAD in days (native units)
```

`recoverer.py` computes all four values during its normal evaluation loop, then passes contexts to the resolver for decision-making.

---

## The `resolve_alias_pair()` Function

```python
def resolve_alias_pair(ctx1, ctx2) -> int:
    # Rule 1: Event support preference
    if ctx1.support_count != ctx2.support_count:
        return 1 if ctx1.support_count > ctx2.support_count else 2

    # Rule 2: Coverage preference (threshold: 2pp)
    if abs(ctx1.coverage_fraction - ctx2.coverage_fraction) > 0.02:
        return 1 if ctx1.coverage_fraction > ctx2.coverage_fraction else 2

    # Rule 3: Residual MAD preference (threshold: 0.001 days ≈ 1.4 min)
    if abs(ctx1.residual_mad - ctx2.residual_mad) > 0.001:
        return 1 if ctx1.residual_mad < ctx2.residual_mad else 2

    return 0  # Intractable ambiguity
```

The function returns:
- `1` → ctx1 is preferred (fundamental)
- `2` → ctx2 is preferred (fundamental)
- `0` → ambiguous (`WARNING_HARMONIC_AMBIGUITY` fires)

---

## Integration in `recoverer.py`

After all clusters are evaluated and `PeriodCandidate` objects are built, `_apply_harmonic_tiebreaks()` scans all candidate pairs for near-integer period ratios (threshold: ratio within 0.1 of integer). For each alias pair:

1. Retrieve both `HarmonicEvaluationContext` objects.
2. Call `resolve_alias_pair()`.
3. If a winner is determined, boost its `confidence_score` by `+0.05` — enough to ensure it sorts above the alias, but not enough to override a genuine quality difference.
4. If ambiguous (verdict=0), leave scores unchanged; `WARNING_HARMONIC_AMBIGUITY` fires in the existing ambiguity check.

---

## Why the Score Boost Approach

An alternative would be to directly reorder the candidates list. The score-boost approach was chosen because:
1. It maintains the single-sort path (candidates sorted once at the end).
2. The `+0.05` boost is small enough that a genuinely superior alias (e.g., one with much higher coverage) can still outscore the boosted candidate — preventing the tie-break from overriding legitimate quality evidence.
3. It preserves the existing `ambiguity_threshold` check without modification.

---

## Tie-Break Decision Thresholds

| Criterion | Threshold | Rationale |
| :--- | :---: | :--- |
| Support count | 0 (exact integer) | Transit count is an integer — no tolerance needed |
| Coverage fraction | 2 percentage points | Sub-2pp differences are within measurement noise |
| Residual MAD | 0.001 days (~1.4 min) | Below TESS cadence precision; effectively tied |
