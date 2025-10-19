import subprocess
import random
import time

services = ["service-a", "service-b"]

while True:
    wait = random.randint(15, 25)
    print(f"Waiting {wait}s before killing a service...")
    time.sleep(wait)

    target = random.choice(services)
    print(f"Killing service {target} for 5 seconds...")

    # Stop the container
    subprocess.run(f"docker stop {target}", shell=True)
    time.sleep(5)
    subprocess.run(f"docker start {target}", shell=True)

    print(f"Service {target} restarted.")
