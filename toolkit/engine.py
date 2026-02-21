import json
from toolkit.brute_force import detect_bruteforce


def run_all_detectors(log_file, threshold, window):
    alerts = []

    # Module 1
    alerts.extend(detect_bruteforce(log_file, threshold, window))

    return alerts


def save_alerts(alerts, output_file):
    if alerts:
        with open(output_file, "w") as f:
            json.dump(alerts, f, indent=4)
