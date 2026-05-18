# qwen3-06b-ternary-frontier

Public Qwen3 1.7B ternary frontier task pack using the qwen3-06b-ternary-frontier compatibility slug.

Run locally from the repo root:

```bash
python3 competition_packs/qwen3_06b_ternary_frontier/prepare.py
python3 competition_packs/qwen3_06b_ternary_frontier/benchmark.py
```

Editable surfaces are defined by the coordinator task configuration.

Generated Python bytecode/cache artifacts are omitted from this task pack. Submitted patches are accepted only for the coordinator `allowed_patch_paths`, and manual bytecode/cache patch paths are rejected:

- `__pycache__/`
- `*.pyc`
- `*.pyo`
