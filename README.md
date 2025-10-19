# Chaos-Resilient Pre-Deployment Simulator

Chaos-Resilient Pre-Deployment Simulator is an end-to-end chaos simulation platform that tests microservices’ resilience *before* deployment.  
It creates a mini production-like environment, injects real-world failures (network delays, crashes, CPU spikes, DB errors), and visualizes how the system recovers — all inside CI/CD.

---

##  Features

 **Two Realistic Microservices**
- **Service A** → API orchestrator that depends on Service B  
- **Service B** → Worker service with SQLite database and compute logic  
- Simulated state, delays, and inter-service calls  

 **Chaos Engineering**
- Random service kills and restarts  
- Network latency injection  
- CPU and memory spikes  
- Temporary database failures  
- Error propagation across services  

 **Observability**
- Prometheus metrics (requests, latency, errors)  
- Grafana dashboards  
- Optional Python Dash web dashboard for quick local visualization  

 **CI/CD Integration**
- Pre-deployment chaos tests run automatically in GitHub Actions  
- Generates resilience reports in `/reports`  

---

##  Architecture

```text
+--------------------------+
|      GitHub Actions      |
|  (Pre-Deployment Chaos)  |
+-----------+--------------+
            |
            v
+--------------------------+
| Docker Compose Orchestrator |
+-----------+--------------+
            |
+-------------------+     +-------------------+
| Service A (API)   |<--->| Service B (Worker)|
| - Flask           |     | - Flask + SQLite  |
| - Calls B         |     | - Simulated DB    |
+-------------------+     +-------------------+
            |
            v
+-------------------+
| Chaos Scripts     |
| - Kill services   |
| - Network delay   |
| - CPU/mem spikes  |
| - DB failures     |
+-------------------+
            |
            v
+-------------------+
| Observability     |
| - Prometheus      |
| - Grafana/Dash    |
+-------------------+
