import re
from collections import defaultdict
from datetime import datetime


def parse_timestamp(log_line):
    match = re.match(r'(\w+\s+\d+\s+\d+:\d+:\d+)', log_line)
    if match:
        return datetime.strptime(match.group(1), "%b %d %H:%M:%S")
    return None


def detect_bruteforce(log_file, threshold=5, time_window=60):
    attempts = defaultdict(list)
    alerts = []

    with open(log_file, "r") as file:
        for line in file:
            if "Failed password" in line:
                timestamp = parse_timestamp(line)
                ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)

                if timestamp and ip_match:
                    ip = ip_match.group(1)
                    attempts[ip].append(timestamp)

    for ip, times in attempts.items():
        times.sort()

        for i in range(len(times)):
            window = [t for t in times if 0 <= (t - times[i]).total_seconds() <= time_window]

            if len(window) >= threshold:
                alert = {
                    "module": "brute_force",
                    "alert_type": "SSH Brute Force Detected",
                    "attacker_ip": ip,
                    "failed_attempts": len(window),
                    "time_window_seconds": time_window
                }
                alerts.append(alert)
                break

    return alerts
