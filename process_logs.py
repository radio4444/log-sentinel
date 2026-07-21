import pandas as pd
import json

logs = pd.read_json("server_logs.json")
# Inspect the data
logs.info()
print(logs.head())
# Clean the data: Match proper datatype for each column and Drop NaN value

logs["status_code"] = pd.to_numeric(logs["status_code"], errors="coerce")
clean_logs = logs.dropna()
clean_logs['timestamp'] = clean_logs['timestamp'].astype(str)
clean_logs['status_code'] = clean_logs['status_code'].astype(int)

clean_logs.info()
print(clean_logs.head())
# Analyze the data
error_logs = clean_logs[
    (clean_logs["log_level"] == "ERROR") & (clean_logs["status_code"] == 500)
].to_dict(orient='records')


summary = {
    "total_valid_logs": len(clean_logs),
    "Average Response time": float(clean_logs["response_time_in_ms"].mean().round(1)),
    "total_error_counts": len(error_logs),
}


metrics_dict = {
    "summary": summary,
    "flagged_errors": error_logs,
}

print(clean_logs.dtypes)


with open("cleaned_metrics.json", "w") as f:
    json.dump(metrics_dict, f, indent=4)
