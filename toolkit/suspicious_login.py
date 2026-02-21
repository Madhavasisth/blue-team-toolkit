import re
from collections import defaultdict
from datetime import datetime


def parse_timestamp(log_line):
    match = re.match(r'(\w+\s+\d+\s+\d+:\d+:\d+)', log_line)
    if match:
        return datetime.strptime(match.group(1), "%b %d %H:%M:%S")
    return None


def detect_suspicious_login(log_file, threshold=5, time_window=120):
    failed_attempts = defaultdict(list)
    successful_logins = defaultdict(list)
    alerts = []

    with open(log_file, "r") as file:
        for line in file:
            timestamp = parse_timestamp(line)
            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)

            if timestamp and ip_match:
                ip = ip_match.group(1)

                if "Failed password" in line:
                    failed_attempts[ip].append(timestamp)

                elif "Accepted password" in line:
                    successful_logins[ip].append(timestamp)

    for ip in successful_logins:
        if ip in failed_attempts:
            for success_time in successful_logins[ip]:
                recent_failures = [
                    fail_time for fail_time in failed_attempts[ip]
                    if 0 <= (success_time - fail_time).total_seconds() <= time_window
                ]

                if len(recent_failures) >= threshold:
                    alert = {
                        "module": "suspicious_login",
                        "alert_type": "Brute Force Followed by Successful Login",
                        "attacker_ip": ip,
                        "failed_attempts_before_success": len(recent_failures),
                        "time_window_seconds": time_window,
                        "severity": "HIGH"
                    }
                    alerts.append(alert)
                    break

    return alerts
