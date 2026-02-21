import argparse
import json
from toolkit.engine import run_all_detectors, save_alerts


def main():
    parser = argparse.ArgumentParser(description="Blue Team Toolkit")
    parser.add_argument("--log", required=True)
    parser.add_argument("--threshold", type=int, default=5)
    parser.add_argument("--window", type=int, default=60)
    parser.add_argument("--output", default="alerts.json")

    args = parser.parse_args()

    alerts = run_all_detectors(args.log, args.threshold, args.window)

    if alerts:
        save_alerts(alerts, args.output)
        print("🚨 Threats detected:")
        print(json.dumps(alerts, indent=4))
    else:
        print("✅ No threats detected.")


if __name__ == "__main__":
    main()
