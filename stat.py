import glob
import json
import os
import statistics

OUTPUT_DIR = "logs/baseline"

SCORE_KEYS = ["open_source", "self_projects", "production", "technical_skills"]


def _num(value):
    """Extract a number from either a bare int or a {'score'/'points': N} object."""
    if isinstance(value, dict):
        for key in ("score", "points"):
            if key in value:
                return value[key]
        return None
    return value


def load_run(path):
    with open(path, "r") as f:
        data = json.load(f)

    scores = data.get("scores", {})
    metrics = {k: _num(scores.get(k)) for k in SCORE_KEYS}
    metrics["bonus_points"] = _num(data.get("bonus_points"))
    metrics["deductions"] = _num(data.get("deductions"))

    subtotal = sum(metrics[k] or 0 for k in SCORE_KEYS)
    metrics["total"] = subtotal + (metrics["bonus_points"] or 0) - (metrics["deductions"] or 0)
    return metrics


def main():
    paths = sorted(glob.glob(os.path.join(OUTPUT_DIR, "run_*.txt")))
    if not paths:
        print(f"no run_*.txt files in {OUTPUT_DIR}/")
        return

    runs = []
    for p in paths:
        try:
            runs.append(load_run(p))
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print(f"[skip] {p}: {e}")

    print(f"aggregated {len(runs)} runs\n")

    order = SCORE_KEYS + ["bonus_points", "deductions", "total"]
    print(f"{'metric':<18}{'mean':>8}{'sd':>8}{'min':>6}{'max':>6}")
    print("-" * 46)
    for key in order:
        vals = [r[key] for r in runs if r.get(key) is not None]
        if not vals:
            continue
        sd = statistics.pstdev(vals) if len(vals) > 1 else 0.0
        print(f"{key:<18}{statistics.mean(vals):>8.2f}{sd:>8.2f}{min(vals):>6}{max(vals):>6}")


if __name__ == "__main__":
    main()
