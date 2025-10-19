from fastapi import fastapi
import time, random
from prometheus_client import Counter, Histogram, generate_latest
from fastapi.respones import Response 

app = FastAPI(title="Service A - Data Provider")

# Prometheus metrics
REQUEST_COUNT = Counter("service_a_total_requests", "Total requests to Service A", ["endpoint"])
LATENCY = Histogram("service_a_latency_seconds", "Latency  for each request", ["endpoint"])

@app.get("/")
def root():
    return {"message:" "Service A is now live!"}

@app.get("/data")
def get_data():
    REQUEST_COUNT.labels(endpoint="/data").inc()
    start = time.time()

    # variable latency (100ms-2s)
    delay = random.uniform(0.1, 2.0)
    time.sleep(delay)

    LATENCY.labels(endpoint="/data").observe(time.time() - start)

    sample_data = {
        "id": random.randint(1, 100)
        "value": random.choice(["one", "two", "three", "four"])
        "delay": round(delay, 3)
    }
    return sample_data

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")


    