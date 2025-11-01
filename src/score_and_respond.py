import json, random

ENRICHED_FILE = "../data/enriched_alerts.json"
OUTPUT_FILE = "../data/scored_alerts.json"

# Load enriched alerts from JSON
def load_alerts():
    with open(ENRICHED_FILE, "r") as f:
        return json.load(f)

# Save final scored alerts to JSON
def save_alerts(data):
    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=2)

# Assign a simple risk score based on alert type and reputation
def score_alert(alert):
    base_score = 20  # start low
    
    # Increase score for known bad IPs
    enrichment = alert.get("enrichment", {})
    rep = enrichment.get("reputation", 0)
    if isinstance(rep, int):
        base_score += rep // 2
    
    # Increase score if alert type is severe
    if "malware" in alert.get("type", "").lower():
        base_score += 30
    elif "phishing" in alert.get("type", "").lower():
        base_score += 20
    elif "port-scan" in alert.get("type", "").lower():
        base_score += 10
    
    # Add a little randomness to simulate variable context
    base_score += random.randint(0, 10)
    
    # Keep it within 0–100
    return min(base_score, 100)

# Decide what to do based on risk score
def decide_action(score):
    if score >= 75:
        return "BLOCK_IP"
    elif score >= 40:
        return "NOTIFY_ANALYST"
    else:
        return "LOG_ONLY"

# Run scoring and response logic
def main():
    alerts = load_alerts()
    scored_alerts = []
    
    for alert in alerts:
        score = score_alert(alert)
        action = decide_action(score)
        alert["score"] = score
        alert["recommended_action"] = action
        scored_alerts.append(alert)
        print(f"Alert: {alert.get('type','unknown')} | Score: {score} | Action: {action}")
    
    save_alerts(scored_alerts)
    print(f"✅ Scored {len(scored_alerts)} alerts saved to {OUTPUT_FILE}")

# Run the script
if __name__ == "__main__":
    main()
