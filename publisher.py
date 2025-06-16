import json
import time
import random
import os
from google.cloud import pubsub_v1

# ✅ Update path to your service account JSON key in Downloads
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Ashutosh kumar\Desktop\gcp-realtime-project\publisher-key.json"

project_id = "realtime-pipeline-463110"
topic_id = "transactions-topic"
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

def generate_transaction():
    return {
        "user_id": f"user{random.randint(1000, 9999)}",
        "amount": round(random.uniform(10, 1000), 2),
        "location": random.choice(["Delhi", "Mumbai", "Bangalore"]),
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ')
    }

while True:
    txn = generate_transaction()
    data = json.dumps(txn).encode("utf-8")
    publisher.publish(topic_path, data=data)
    print("Published:", txn)
    time.sleep(2)
