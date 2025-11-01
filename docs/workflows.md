This is the basic workflow for Incident Response Automation project. It shows how alerts are processed, analyzed, and acted on automatically.

---

### 1. Ingest

The system starts by collecting alerts — either from Splunk or from my sample file `alerts.json`.
Each alert contains basic info like alert type, time, IP, hostname, or file hash.

---

### 2. Normalize & Validate

All alerts are converted into a standard format so the system can treat them the same way.
Missing or incomplete alerts are flagged for manual review.

---

### 3. Enrich

The system checks each indicator (IP, domain, file hash) against external sources like **AbuseIPDB** or **VirusTotal** to find out if they’re known to be malicious.
If API keys aren’t available, the system uses basic checks (like whether an IP is public or private).

---

### 4. Score & Prioritize

Every alert gets a **risk score (0–100)** based on its type and the enrichment results.
High-risk alerts are moved for quick action; low-risk ones are just logged.

---

### 5. Respond

Depending on the score:

* **High risk:** Auto-block the IP or isolate the host
* **Medium:** Send notification to analyst (Slack/email)
* **Low:** Store for review later

Every action is logged and reversible.

---

### 6. Log & Report

All results — enrichment, scores, and actions — are saved in a local SQLite database.
This allows easy review and audit of what the system did and why.

---

### 7. Dashboard

A small Streamlit dashboard shows recent alerts, enrichment info, actions taken, and allows analysts to review or undo automated actions.

---

### 8. Safety

The system avoids over-automation:

* Has a **threshold** before auto-blocking
* Maintains a **whitelist** for critical systems
* Records every change for transparency

---