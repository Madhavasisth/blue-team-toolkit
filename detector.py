import re
import json
from collections import defaultdict

LOG_FILE = "sample_logs.txt"
ALERT_FILE = "alerts.json"
THRESHOLD = 5


def detect_bruteforce():
    failed_attempts = defaultdict(int)
    alerts = []

    with open(LOG_FILE, "r") as file:
        for line in file:
            if "Failed password" in line:
                match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                if match:
                    ip = match.group(1)
                    failed_attempts[ip] += 1

    for ip, count in failed_attempts.items():
        if count >= THRESHOLD:
            alert = {
                "alert_type": "SSH Brute Force Detected",
                "attacker_ip": ip,
                "failed_attempts": count
            }
            alerts.append(alert)

    if alerts:
        with open(ALERT_FILE, "w") as f:
            json.dump(alerts, f, indent=4)
        print("🚨 ALERT: Brute force detected!")
        print(json.dumps(alerts, indent=4))
    else:
        print("✅ No brute force detected.")


if __name__ == "__main__":
    detect_bruteforce()
