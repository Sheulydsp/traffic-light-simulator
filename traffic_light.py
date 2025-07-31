class TrafficLight:
    STATES = ["RED", "GREEN", "YELLOW"]

    def __init__(self, direction):
        self.direction = direction
        self.state = "RED"
        self.timer = 0

    def next_state(self):
        if self.state == "RED":
            self.state = "GREEN"
        elif self.state == "GREEN":
            self.state = "YELLOW"
        elif self.state == "YELLOW":
            self.state = "RED"

    def __str__(self):
        return f"{self.direction} Light: {self.state}"
