import json
import datetime

# In a real setup, you’d parse logs or metrics
report = {
    "timestamp": str(datetime.datetime.now()),
    "services": {
        "service-a": {"uptime": "checked in logs", "errors": "tracked via Prometheus"},
        "service-b": {"uptime": "checked in logs", "errors": "tracked via Prometheus"},
    },
    "chaos_injected": ["kill_service", "network_delay", "resource_spike", "db_failure"]
}

with open("reports/chaos_report.json", "w") as f:
    json.dump(report, f, indent=4)

print("Chaos report generated at reports/chaos_report.json")
