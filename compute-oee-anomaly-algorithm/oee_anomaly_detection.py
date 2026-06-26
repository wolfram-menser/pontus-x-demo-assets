#!/usr/bin/env python3
"""Compute-to-Data Algorithmus — Maschinen-Zustands-/Anomalie-Auswertung.

Läuft auf der Pontus-X Compute-to-Data-Umgebung: das (private) Dataset wird
vom Provider nach ``/data/inputs/<DID>/<index>`` gemountet, das Ergebnis
schreibt der Algorithmus nach ``/data/outputs/``. Die Rohdaten verlassen die
Compute-Umgebung NIE — der Käufer erhält nur das aggregierte Resultat.

Stdlib-only (csv/json/os), damit jedes schlanke Python-Container-Image genügt.
Erwartet ein CSV mit numerischen Spalten; erkennt optional ``health_index``
(Predictive-Maintenance-Dataset) und flaggt Anomalien (< 0,7).

Container (Ocean/Pontus-X): image z. B. ``oceanprotocol/algo_dockers``,
tag ``python-branin``, entrypoint ``python $ALGO``.
"""
from __future__ import annotations

import csv
import json
import os
import statistics

INPUT_DIR = os.environ.get("INPUTS", "/data/inputs")
OUTPUT_DIR = os.environ.get("OUTPUTS", "/data/outputs")
ANOMALY_THRESHOLD = 0.70


def find_csv_files(root: str) -> list[str]:
    hits: list[str] = []
    for dirpath, _dirs, files in os.walk(root):
        for f in files:
            if f.lower().endswith(".csv") or f.isdigit():  # Ocean mountet oft als "0"
                hits.append(os.path.join(dirpath, f))
    return hits


def numeric_columns(rows: list[dict]) -> list[str]:
    cols: list[str] = []
    if not rows:
        return cols
    for key in rows[0].keys():
        vals = 0
        for r in rows:
            try:
                float(r[key])
                vals += 1
            except (TypeError, ValueError):
                break
        if vals == len(rows):
            cols.append(key)
    return cols


def analyse(path: str) -> dict:
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        return {"source": os.path.basename(path), "row_count": 0}

    num_cols = numeric_columns(rows)
    summary = {}
    for c in num_cols:
        vals = [float(r[c]) for r in rows]
        summary[c] = {
            "min": round(min(vals), 4),
            "max": round(max(vals), 4),
            "mean": round(statistics.fmean(vals), 4),
            "stdev": round(statistics.pstdev(vals), 4),
        }

    anomalies = []
    if "health_index" in num_cols:
        label_col = next((k for k in rows[0] if k not in num_cols), None)
        for r in rows:
            if float(r["health_index"]) < ANOMALY_THRESHOLD:
                anomalies.append({
                    "asset": r.get(label_col) or r.get("asset_id") or "?",
                    "health_index": float(r["health_index"]),
                    "predicted_rul_days": r.get("predicted_rul_days"),
                })

    return {
        "source": os.path.basename(path),
        "row_count": len(rows),
        "numeric_columns": num_cols,
        "column_summary": summary,
        "anomaly_threshold": ANOMALY_THRESHOLD,
        "anomalies": anomalies,
        "anomaly_count": len(anomalies),
    }


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    results = [analyse(p) for p in find_csv_files(INPUT_DIR)]
    report = {
        "algorithm": "oee_anomaly_detection",
        "version": "1.0",
        "datasets_analysed": len(results),
        "results": results,
    }
    out_path = os.path.join(OUTPUT_DIR, "result.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2, ensure_ascii=False)
    print(f"[oee_anomaly_detection] wrote {out_path} — {len(results)} dataset(s) analysed")


if __name__ == "__main__":
    main()
