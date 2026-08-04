# LogSentinel 🛡️

A multi-language telemetry ETL pipeline that generates mock server logs, processes performance metrics, validates data contracts at runtime, and triggers SLA violation alerts.

## 📐 System Architecture Flow

```text
[1. generate_logs.py]   --> Produces raw telemetry events
        │
[2. process_logs.py]    --> Aggregates & cleans metrics -> json/cleaned_metrics.json
        │
[3. validate_metrics.ts]--> Enforces TypeScript / Zod runtime schema contracts
        │
[4. alert_engine.py]    --> Evaluates SLA thresholds -> json/health_report.json

```

**Master Orchestrator:** `run_pipeline.py` executes all four stages sequentially, tracking sub-second execution benchmarks and enforcing fail-fast pipeline halting upon errors.

---

## 🛠️ Tech Stack & Dependencies

* **Python 3.x:** Data generation, ETL aggregation, SLA alert engine, and pipeline orchestration.
* **TypeScript & Node.js:** Runtime data contract validation.
* **Zod:** Strict schema enforcement for boundary JSON data.

---

## 🚀 Local Setup & Installation

### 1. Prerequisites

Ensure you have **Python 3.10+** and **Node.js 18+** installed on your system.

### 2. Clone Repository & Setup Virtual Environment

```bash
git clone (https://github.com/radio4444/log-sentinel.git)
cd log-sentinel

# Create and activate Python virtual environment
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate

```

### 3. Install Dependencies

```bash
# Initialize Node project (if setting up from scratch)
npm init -y

# Install Node development dependencies
npm install -D typescript ts-node @types/node

# Install Zod schema validation library
npm install zod
```

---

## ⚡ Execution

To execute the entire end-to-end pipeline with single-command orchestration:

```bash
python src/run_pipeline.py
```

### Example Output

```text
Starting LogSentinel Pipeline...
[1/4] Running generate_logs.py... Completed in 0.27s
[2/4] Running process_logs.py... Completed in 0.35s
[3/4] Running validate_metrics.ts... Completed in 0.68s
[4/4] Running alert_engine.py... Completed in 0.26s

PIPELINE EXECUTION SUCCESSFUL
Total Duration: 1.6s
```

