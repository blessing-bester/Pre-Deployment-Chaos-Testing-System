import subprocess
import time
import random

services = ["service-b"]  # Only Service B has a DB

while True:
    wait = random.randint(30, 45)
    time.sleep(wait)
    target = services[0]

    print(f"Simulating DB failure on {target} for 5s...")
    # Rename DB to simulate failure
    subprocess.run(f"docker exec {target} mv /app/service_b.db /app/service_b.db.bak", shell=True)
    time.sleep(5)
    subprocess.run(f"docker exec {target} mv /app/service_b.db.bak /app/service_b.db", shell=True)

    print(f"DB restored on {target}.")
