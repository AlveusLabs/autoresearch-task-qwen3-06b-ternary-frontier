# Qwen3 1.7B Mostly-Ternary Compression Frontier

This pack uses the same validator-owned proxy harness, but the pack quantization mode is ternary.
The `qwen3_06b` pack path and `qwen3-06b-*` public slug are compatibility
handles; the active model contract is Qwen3 1.7B.

Primary submission surface:

- `artifact_uri` pointing at a compressed artifact in a public Hugging Face repo
  or another public HTTPS location
- `artifact_sha256` and `artifact_size_bytes` for the exact bytes validators
  must download

Recipe/code patches are optional metadata; coordinators store only URI/integrity
metadata.
Validators download, load, account for, and score the artifact directly.

Artifact accounting is validator-computed. The hard checks are:

- parameter count within the Qwen3 1.7B ternary-compatible cap
- compressed representation size within a 90% ternary plus 10% 16-bit rescue budget
- non-ternary rescue fraction at or below `10%`

Miners can use residuals, sparse side tables, mixed ternary components, or other
designs as long as every extra component is declared in
`artifact.accounting.extra_entries` or a layer `extra_components` list so the
validator counts the parameters, bits, and rescue usage.
New best acceptance uses a `0.02`-nat PPL resolution before replacing the
incumbent on quality alone.
