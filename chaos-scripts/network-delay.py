import subprocess
import random
import time

services = ["service-a", "service-b"]

while True:
    wait = random.randint(20, 30)
    time.sleep(wait)
    target = random.choice(services)
    delay = random.randint(100, 500)  # milliseconds

    print(f"Adding {delay}ms network delay to {target} for 5s...")
    subprocess.run(f"docker exec {target} tc qdisc add dev eth0 root netem delay {delay}ms", shell=True)
    time.sleep(5)
    subprocess.run(f"docker exec {target} tc qdisc del dev eth0 root", shell=True)
    print(f"Removed network delay from {target}.")
