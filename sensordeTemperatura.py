import threading
import time
import random

def sensordeTemperatura(timer_runs):
    while timer_runs.is_set():
        temperatura = random.randint(15, 30)
        print("Temperatura: " + str(temperatura)+"°")
        time.sleep(1)

timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=sensordeTemperatura, args=(timer_runs,))
t.start()

time.sleep(10)
timer_runs.clear()
print("El sensor  se detuvo")