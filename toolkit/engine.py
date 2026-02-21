import json
from toolkit.brute_force import detect_bruteforce
from toolkit.suspicious_login import detect_suspicious_login
from toolkit.constants import SEVERITY_LEVELS


def run_all_detectors(log_file, threshold, window):
    alerts = []

    alerts.extend(detect_bruteforce(log_file, threshold, window))
    alerts.extend(detect_suspicious_login(log_file, threshold, window))

    # Sort alerts by severity (highest first)
    alerts.sort(
        key=lambda x: SEVERITY_LEVELS.get(x["severity"], 0),
        reverse=True
    )

    return alerts


def save_alerts(alerts, output_file):
    if alerts:
        with open(output_file, "w") as f:
            json.dump(alerts, f, indent=4)
