import json, os, requests
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
ABUSEIPDB_KEY = os.getenv("ABUSEIPDB_KEY")
VT_KEY = os.getenv("VT_KEY")

ALERTS_FILE = "../data/alerts.json"
OUTPUT_FILE = "../data/enriched_alerts.json"

# Load alerts from JSON file
def load_alerts():
    with open(ALERTS_FILE, "r") as f:
        return json.load(f)

# Save enriched alerts back to JSON
def save_alerts(data):
    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=2)

# Check IP reputation using AbuseIPDB or return dummy data
def enrich_ip(ip):
    if not ABUSEIPDB_KEY:
        return {"ip": ip, "reputation": "unknown", "reports": 0, "source": "local"}
    
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {"Key": ABUSEIPDB_KEY, "Accept": "application/json"}
    params = {"ipAddress": ip, "maxAgeInDays": 90}
    
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=8)
        if resp.status_code == 200:
            data = resp.json().get("data", {})
            return {
                "ip": ip,
                "reputation": data.get("abuseConfidenceScore", 0),
                "reports": data.get("totalReports", 0),
                "country": data.get("countryCode", "N/A"),
                "source": "AbuseIPDB"
            }
    except Exception as e:
        print(f"Error checking {ip}: {e}")
    return {"ip": ip, "reputation": "error", "reports": 0, "source": "AbuseIPDB"}

# Enrich each alert with IP reputation info
def enrich_alert(alert):
    enriched = alert.copy()
    if "ip" in alert:
        enriched["enrichment"] = enrich_ip(alert["ip"])
    else:
        enriched["enrichment"] = {"status": "no IOC found"}
    return enriched

# Main function to run enrichment on all alerts
def main():
    alerts = load_alerts()
    enriched_alerts = [enrich_alert(a) for a in alerts]
    save_alerts(enriched_alerts)
    print(f" Enriched {len(enriched_alerts)} alerts saved to {OUTPUT_FILE}")

# Run the script
if __name__ == "__main__":
    main()
