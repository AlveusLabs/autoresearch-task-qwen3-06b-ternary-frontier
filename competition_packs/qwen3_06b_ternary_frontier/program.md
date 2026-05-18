# Program

Submit a mostly-ternary artifact under the Qwen3 1.7B ternary compression contract.
The `qwen3-06b-ternary-frontier` slug is preserved for existing public repos,
URLs, and scripts; it is not the parameter-count contract.

Primary validation is artifact-first: miners train off-chain and submit the
compressed artifact through `artifact_uri`. Use a public Hugging Face artifact
URL or another public HTTPS URL; submit `artifact_sha256` and
`artifact_size_bytes` with it. The coordinator stores URI/integrity metadata,
not artifact bytes.
Recipe/code patches are optional metadata and are not replayed as the normal
acceptance gate.

Hard gates:

- shape valid
- parameter count within the Qwen3 1.7B ternary-compatible cap
- compressed representation size within a 90% ternary plus 10% 16-bit rescue budget
- non-ternary rescue fraction `<= 10%`
- artifact loadable by the fixed validator
- heldout quality floor

Extra residuals, side tables, and other representation pieces are allowed, but
they must be declared in `artifact.accounting.extra_entries` or layer
`extra_components` so the validator counts their parameters, bits, and rescue
usage.

Survivors are Pareto-ranked on:

- `heldout_ppl` (lower is better)
- `compression_ratio`

New best acceptance uses a `0.02` heldout-PPL resolution in nats. A submission
can win by reducing PPL past that band, or by improving compression ratio while
remaining inside the incumbent's PPL band.

This task is intended to run in `centerless` mode at the coordinator layer.
