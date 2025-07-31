from traffic_light import TrafficLight

def test_initial_state():
    light = TrafficLight("NS")
    assert light.state == "RED"

def test_state_sequence():
    light = TrafficLight("NS")
    light.next_state()
    assert light.state == "GREEN"
    light.next_state()
    assert light.state == "YELLOW"
    light.next_state()
    assert light.state == "RED"
