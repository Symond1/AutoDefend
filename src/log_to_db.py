import json, sqlite3, os

DB_FILE = "../data/alerts.db"
SCORED_FILE = "../data/scored_alerts.json"

# Load alerts from the scored JSON file
def load_alerts():
    with open(SCORED_FILE, "r") as f:
        return json.load(f)

# Initialize the SQLite database and create table if not exists
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            ip TEXT,
            score INTEGER,
            action TEXT,
            reputation TEXT,
            reports INTEGER,
            source TEXT
        )
    """)
    conn.commit()
    conn.close()

# Insert alerts into the database
def insert_alerts(alerts):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    for alert in alerts:
        enrich = alert.get("enrichment", {})
        cur.execute("""
            INSERT INTO alerts (type, ip, score, action, reputation, reports, source)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            alert.get("type", "unknown"),
            alert.get("ip", "N/A"),
            alert.get("score", 0),
            alert.get("recommended_action", "LOG_ONLY"),
            enrich.get("reputation", "unknown"),
            enrich.get("reports", 0),
            enrich.get("source", "N/A")
        ))
    conn.commit()
    conn.close()

# Main function to load, create, and insert
def main():
    if not os.path.exists(SCORED_FILE):
        print("⚠️ No scored_alerts.json found. Run Step 3 first.")
        return

    alerts = load_alerts()
    init_db()
    insert_alerts(alerts)
    print(f"✅ Inserted {len(alerts)} alerts into {DB_FILE}")

if __name__ == "__main__":
    main()
