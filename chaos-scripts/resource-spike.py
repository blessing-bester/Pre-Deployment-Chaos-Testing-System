import subprocess
import random
import time

services = ["service-a", "service-b"]

while True:
    wait = random.randint(25, 35)
    time.sleep(wait)
    target = random.choice(services)
    chaos_type = random.choice(["cpu", "memory"])
    duration = random.randint(5, 10)

    if chaos_type == "cpu":
        print(f"Spiking CPU on {target} for {duration}s...")
        subprocess.run(f"docker exec {target} python -c \"[x**2 for x in range(10**7)]; import time; time.sleep({duration})\"", shell=True)
    else:
        print(f"Spiking memory on {target} for {duration}s...")
        subprocess.run(f"docker exec {target} python -c \"a = [' ' * 10**6]*200; import time; time.sleep({duration})\"", shell=True)

    print(f"{chaos_type.capitalize()} spike ended for {target}.")
