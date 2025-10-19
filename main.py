from fastapi import FastAPI
import time, requests
from prometheus_client import Counter, Histogram, generate_latest
from fastapi.responses import responses

app = FastAPI(title="Service B - Data Consumer")

REQUEST_COUNT = Counter("service_b_total_requests", "Total requests to Service B", ["endpoint"])
LATENCY = Histogram("service_b_latency_seconds", "Latency for each request made", ["endpoint"])
FAILURES = Counter("service_b_total_failures", "Failures calling service A")

SERVICE_A_URL = "https://service-a:8000/data"

@app.get("/")
def root():
    return {"message": "Service B is now live!"}

@app.get("/consume")
def consume_data():
    REQUEST_COUNT.labels(endpoint="/consume").inc()
    start = time.time()

    try:
        resp = requests.get(SERVICE_A_URL, timeout=2)
        resp.raise_for_status()
        LATENCY.labels(endpoint="/consume").observe(time.time() - start)
        data = resp.json()
        # request now processed by service B
        data["processed_by"] = "Service B"
        return data
    except Exception as e:
        FAILURES.inc()
        return {"error": f"Failed to reach Service A: {str(e)}"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")