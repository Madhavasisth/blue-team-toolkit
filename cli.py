import argparse
from colorama import Fore, Style, init
from toolkit.engine import run_all_detectors, save_alerts

# Initialize colorama
init(autoreset=True)


def color_by_severity(severity):
    if severity == "CRITICAL":
        return Fore.MAGENTA
    elif severity == "HIGH":
        return Fore.RED
    elif severity == "MEDIUM":
        return Fore.YELLOW
    elif severity == "LOW":
        return Fore.BLUE
    return Fore.WHITE


def print_alert(alert):
    color = color_by_severity(alert["severity"])

    print(color + "=" * 60)
    print(color + f"[{alert['severity']}] {alert['alert_type']}")
    print(color + f"Module       : {alert['module']}")
    print(color + f"Attacker IP  : {alert.get('attacker_ip', 'N/A')}")

    # Print additional metadata dynamically
    for key, value in alert.items():
        if key not in ["severity", "alert_type", "module", "attacker_ip"]:
            print(color + f"{key.replace('_', ' ').title():14}: {value}")

    print(color + "=" * 60)
    print(Style.RESET_ALL)


def main():
    parser = argparse.ArgumentParser(description="Blue Team Toolkit")
    parser.add_argument("--log", required=True, help="Path to log file")
    parser.add_argument("--threshold", type=int, default=5, help="Failed attempts threshold")
    parser.add_argument("--window", type=int, default=60, help="Time window in seconds")
    parser.add_argument("--output", default="alerts.json", help="Output file")

    args = parser.parse_args()

    alerts = run_all_detectors(args.log, args.threshold, args.window)

    if alerts:
        save_alerts(alerts, args.output)

        print("\n🚨 Threats Detected:\n")

        for alert in alerts:
            print_alert(alert)
    else:
        print(Fore.GREEN + "✅ No threats detected.\n")


if __name__ == "__main__":
    main()
