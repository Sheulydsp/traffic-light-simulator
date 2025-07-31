import time
from traffic_light import TrafficLight

# Two directions: NS and EW
ns_light = TrafficLight("North-South")
ew_light = TrafficLight("East-West")

def cycle_lights():
    for _ in range(6):  # 6 cycles
        ns_light.next_state()
        ew_light.next_state()
        print(ns_light)
        print(ew_light)
        print("-" * 30)
        time.sleep(1)

if __name__ == "__main__":
    cycle_lights()
