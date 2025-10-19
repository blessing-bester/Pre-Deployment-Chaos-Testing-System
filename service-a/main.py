from fastapi import fastapi
import time, random
from prometheus_client import Counter, Histogram, generate_latest
from fastapi.respones import Response 

app = FastAPI(title="Service A - Data Provider")

# Prometheus metrics
REQUEST_COUNT = Counter("service_a_total_requests", "Total requests to Service A", ["endpoint"])
LATENCY = Histogram("service_a_latency_seconds", "Latency  for each request", ["endpoint"])

