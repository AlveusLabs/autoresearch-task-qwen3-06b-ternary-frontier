from __future__ import annotations

from typing import Any

from competition_packs.qwen3_06b_shared.shared import default_submission


def build_submission(*, seed: int, time_budget_seconds: int, debug_dataset_name: str | None = None) -> dict[str, Any]:
    artifact = default_submission(quant_mode="ternary", kernel_task=False)
    for row in artifact["layers"]:
        if row["name"] == "attn_out":
            row["high_precision_fraction"] = 0.02
            row["threshold_multiplier"] = 0.65
    return artifact

