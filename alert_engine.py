import json
import datetime

# Define "redline"
MAX_ALLOWED_AVG_LATENCY_MS = 200.0
MAX_ALLOWED_ERROR_COUNT = 10

# Load cleaned_metrics
with open("json/cleaned_metrics.json", "r") as f:
    data = json.load(f)

# Extract summary and flagged_errors
summary = data["summary"]
flagged_errors = data["flagged_errors"]

# count total errors
total_errors_counts = len(flagged_errors)

# Initialize health_report_dict and empty active_alerts array
health_report_dict = {
    "timestamp": datetime.datetime.now().isoformat(),
    "status": "HEALTHY",
}
active_alerts = []

# evaluate health policies: High Latency
if summary["Average Response time"] > MAX_ALLOWED_AVG_LATENCY_MS:
    active_alerts.append(
        {
            "severity": "CRITICAL",
            "rule": "High Latency Volume",
            "message": f"Average response time ({summary['Average Response time']}) exceeded threshold (200ms)",
        }
    )
# evaluate health policies: High Error
if total_errors_counts > MAX_ALLOWED_ERROR_COUNT:
    active_alerts.append(
        {
            "severity": "CRITICAL",
            "rule": "High Error Volume",
            "message": f"Total errors ({total_errors_counts}) exceeded threshold ({MAX_ALLOWED_ERROR_COUNT})",
        }
    )

# evaluate health policies: WARNING
request = 0
for log in flagged_errors:
    if log["response_time_in_ms"] > 800:
        request = request + 1
if request > 0:
    active_alerts.append(
        {
            "severity": "WARNING",
            "rule": "Severe Latency Spike Detected",
            "message": f"Found {request} requests with response time > 800ms",
        }
    )

# attach active_alerts to health_report_dict and updated health_report_dict
if active_alerts:
    health_report_dict['status'] = 'UNHEALTHY'
    health_report_dict['active_alerts'] = active_alerts


# Save health_report_dict in health_report.json
with open("json/health_report.json", "w") as f:
    json.dump(health_report_dict, f, indent=4)
