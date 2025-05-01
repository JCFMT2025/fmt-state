# 📈 FMT Core Prediction Chain (v1)

This folder contains the isolated and force-enabled YAMLs for handling a complete user-initiated FMT prediction workflow — from natural input to result output.

## 🔁 Workflow Overview

This chain is designed to:
1. Parse natural language FMT requests from users
2. Trigger a full market scan (FMS)
3. Rank predictions by probability
4. Save Top 5 + full market predictions into `fmt-state.json`
5. Provide user-facing results (with expandable "Show All Predictions" capability)

## 📂 YAML Modules

| File | Description |
|------|-------------|
| `fmt-request-parser.yml` | Parses user phrases into a structured fixture filter |
| `fmt-trigger-scan.yml` | Launches Full Market Sweep |
| `fmt-results-ranker.yml` | Sorts predictions by probability |
| `fmt-results-output.yml` | Saves results to JSON |
| `force-fmt-executor-v2.yml` | Manual fallback trigger with parameters |

## 🔒 Safety & Isolation

- All YAMLs include: `force: true`, `isolate: true`, and `tag: FMT_CORE_CHAIN`
- Fully isolated from development tracking, phase logs, and cleanup routines
