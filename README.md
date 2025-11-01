## 🛡️ AutoDefend — Incident Response Dashboard

AutoDefend is a **mini-SOAR (Security Orchestration, Automation, and Response)** dashboard built to simulate a Security Operations Center (SOC) analyst’s workflow.
It automatically **collects, enriches, scores, and visualizes** security alerts in real time.

---

### 🚀 Features

* 📊 **Interactive Dashboard** – Visualizes alerts with filters for alert type, action, and risk score.
* ⚙️ **Automation Ready** – Simulates real-world incident response workflows.
* 🌐 **Threat Intelligence Integration** – Uses reputation data from sources like AbuseIPDB.
* 🧠 **Smart Scoring System** – Assigns risk levels and actions (LOG, NOTIFY, BLOCK) based on severity.
* 🧰 **SOC Simulation** – Mimics a Tier 1 Analyst environment for training and demonstrations.

---
### 📸 Preview

#### Main Dashboard

<img width="1844" height="799" alt="Screenshot 2025-11-02 014157" src="https://github.com/user-attachments/assets/3ed5afa7-0d25-4db1-abb0-28aa7a7d4f69" />


#### Quick Summary View

<img width="1521" height="786" alt="Screenshot 2025-11-02 014205" src="https://github.com/user-attachments/assets/552a5375-3ef0-4ede-b57c-0d7de580aa86" />

#### Filtered Alerts

<img width="1840" height="424" alt="Screenshot 2025-11-02 014222" src="https://github.com/user-attachments/assets/2e8db6e1-985a-42da-9190-b0b94ad47837" />

---

### 🧩 Tech Stack

| Component               | Technology                           |
| ----------------------- | ------------------------------------ |
| **Frontend**            | Streamlit                            |
| **Backend**             | Python (Flask / Streamlit Functions) |
| **Data**                | JSON (alerts.json)                   |
| **Threat Intelligence** | AbuseIPDB API                        |

---

### ⚡ How It Works

1. The app loads **alerts.json** containing mock or real security alerts.
2. Each alert is scored based on severity and enriched using external sources.
3. Data is visualized using dynamic filters and summary charts.
4. Analysts can interactively filter alerts by type, score, or action.

---

### 📂 Folder Structure

```
AutoDefend/
│
├── main.py       # Streamlit dashboard
├── data          # security alert dataset
├── docs          # Documentation (this file)
└── src
└── README.md
└── env           # API Keys
```

---

### 💻 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/Symond1/AutoDefend.git

# 2. Navigate to the project folder
cd AutoDefend

# 3. Install dependencies

# 4. Run the dashboard
streamlit run main.py
```

---
