# GCP Real-Time Data Pipeline

![GitHub repo size](https://img.shields.io/github/repo-size/ashutoshkumar28641/gcp-realtime-data-pipeline)
![Last Commit](https://img.shields.io/github/last-commit/ashutoshkumar28641/gcp-realtime-data-pipeline)
![GCP](https://img.shields.io/badge/GCP-PubSub%20%7C%20Dataflow%20%7C%20BigQuery-blue)

This project demonstrates a real-time data ingestion and processing pipeline on **Google Cloud Platform (GCP)** using:

- **Cloud Pub/Sub** – real-time message ingestion
- **Apache Beam (Dataflow)** – data transformation and streaming processing
- **BigQuery** – analytics and data warehousing
- **Cloud Monitoring** – alerts and metrics
- **Looker Studio** – real-time dashboards

---

## 📌 Architecture

```
[publisher.py]  --->  [Cloud Pub/Sub Topic]  --->  [Dataflow Pipeline (Apache Beam)]  --->  [BigQuery Table]  --->  [Looker Studio Dashboard]
```

## 📸 Architecture Diagram

![architecture](assets/architecture.png)

> Pub/Sub → Dataflow (Beam) → BigQuery → Looker Studio

---

## 💼 Use Cases

- Real-time transaction processing
- Fraud detection pipelines
- Sensor/IoT streaming ingestion
- Resume / interview-ready GCP project demo

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/ashutoshkumar28641/gcp-realtime-data-pipeline.git
cd gcp-realtime-data-pipeline
```

### 2. Create a Python Virtual Environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate      # For Windows
# OR
source venv/bin/activate   # For Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

### Step 1: Publish Simulated Transactions
Edit `publisher.py` with your GCP project and topic, then run:
```bash
python publisher.py
```

### Step 2: Deploy the Dataflow Pipeline
Edit `dataflow_pipeline.py` with your GCP project, region, temp/staging GCS paths, and run:
```bash
python dataflow_pipeline.py
```

### Step 3: Verify Output
- View the job in [Dataflow Console](https://console.cloud.google.com/dataflow)
- Query live results in [BigQuery](https://console.cloud.google.com/bigquery)

```sql
SELECT * FROM realtime_dataset.transactions ORDER BY timestamp DESC LIMIT 10;
```

---

## 📊 Dashboard (Optional)

- Connect BigQuery table to Looker Studio
- Create Scorecards, Pie Charts, Time Series for live transaction monitoring

---

## 📈 Monitoring & Alerts

- Set up Cloud Monitoring alerts when the pipeline stops or errors occur
- View logs in Logs Explorer: [Logs Explorer](https://console.cloud.google.com/logs/query)

---

## 📁 Files Description

| File | Description |
|------|-------------|
| `publisher.py` | Simulates real-time data and publishes to Pub/Sub |
| `dataflow_pipeline.py` | Apache Beam pipeline to read from Pub/Sub and write to BigQuery |
| `requirements.txt` | Required Python packages |
| `.gitignore` | Standard Python/.venv ignores |
| `.gcloudignore` | Exclude local files from being uploaded to GCP |
| `assets/architecture.png` | Optional image for architecture diagram |

---

## 🧠 What I Learned

- Setting up and scaling real-time pipelines using Apache Beam on GCP
- Managing Dataflow jobs with proper monitoring & alerting
- Connecting BigQuery with Looker Studio for live dashboards
- Structuring production-ready cloud code for GitHub visibility

---

## 📄 Author
- **Ashutosh Kumar**
- Project: GCP Real-Time Data Engineering
- LinkedIn: (https://www.linkedin.com/in/ashutosh-kumar-996b56169/)
- Email: ashutoshkumar28641@gmail.com

---

> Built with ❤️ by [Ashutosh Kumar](mailto:ashutoshkumar28641@gmail.com)  
> [LinkedIn](https://www.linkedin.com/in/ashutosh-kumar-996b56169/) • [GitHub](https://github.com/ashutoshkumar28641)

---

## 🏁 Ready to Deploy
Once deployed and monitored, this project can be presented as:
- Real-time streaming pipeline demo in interviews
- Technical case study on GitHub or LinkedIn
- Foundation for more advanced pipelines (e.g., fraud detection, ML-based processing)

---
