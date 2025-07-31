import tkinter as tk
from traffic_light import TrafficLight

class TrafficLightGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Light Controller")
        self.root.geometry("450x450")
        self.canvas = tk.Canvas(root, width=450, height=400, bg="#f0f0f0")
        self.canvas.pack()

        self.running = False

        self.ns_light = TrafficLight("NS")
        self.ew_light = TrafficLight("EW")

        # Draw boxes around light groups
        self.canvas.create_rectangle(50, 30, 150, 190, outline="#333", width=2, fill="#ddd")
        self.canvas.create_rectangle(250, 130, 350, 290, outline="#333", width=2, fill="#ddd")

        # Titles
        self.canvas.create_text(100, 20, text="North-South Traffic", font=("Arial", 14, "bold"))
        self.canvas.create_text(300, 120, text="East-West Traffic", font=("Arial", 14, "bold"))

        # Draw traffic lights
        self.ns_lights = self.draw_light(80, 50)
        self.ew_lights = self.draw_light(280, 150)

        # Pedestrian lights with emojis inside circles
        self.ns_ped_light = self.canvas.create_oval(80, 210, 110, 240, fill="grey", width=2)
        self.ns_ped_emoji = self.canvas.create_text(95, 225, text="🚶‍♂️", font=("Arial", 20))

        # New position outside box to the right
        self.ew_ped_light = self.canvas.create_oval(370, 270, 400, 300, fill="grey", width=2)
        self.ew_ped_emoji = self.canvas.create_text(385, 285, text="🚶‍♂️", font=("Arial", 20))
        #self.canvas.create_text(385, 310, text="EW Pedestrian Signal", font=("Arial", 10))


        # Pedestrian labels below lights
        self.canvas.create_text(95, 250, text="NS Pedestrian Signal", font=("Arial", 10))
        self.canvas.create_text(385, 310, text="EW Pedestrian Signal", font=("Arial", 10))

        # Buttons with better layout
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(btn_frame, text="▶ Start Simulation", command=self.start_simulation, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.start_btn.pack(side="left", padx=10)

        self.pause_btn = tk.Button(btn_frame, text="⏸ Pause Simulation", command=self.pause_simulation, bg="#f44336", fg="white", font=("Arial", 12))
        self.pause_btn.pack(side="left", padx=10)

        # Legend
        self.canvas.create_rectangle(10, 350, 440, 395, outline="#333", width=1, fill="#eee")
        self.canvas.create_text(220, 360, text="Legend:", font=("Arial", 12, "bold"), anchor="nw")
        self.canvas.create_oval(40, 370, 70, 400, fill="red")
        self.canvas.create_text(80, 385, text="Red/ Don't Walk", font=("Arial", 10), anchor="w")
        self.canvas.create_oval(200, 370, 230, 400, fill="green")
        self.canvas.create_text(240, 385, text="Green / Walk", font=("Arial", 10), anchor="w")

    def draw_light(self, x, y):
        red = self.canvas.create_oval(x, y, x + 30, y + 30, fill="grey", width=2)
        yellow = self.canvas.create_oval(x, y + 40, x + 30, y + 70, fill="grey", width=2)
        green = self.canvas.create_oval(x, y + 80, x + 30, y + 110, fill="grey", width=2)
        return {"RED": red, "YELLOW": yellow, "GREEN": green}

    def set_light_color(self, lights, active):
        for state, circle in lights.items():
            color = state.lower() if state == active else "grey"
            self.canvas.itemconfig(circle, fill=color)

    def update_gui(self):
        if self.running:
            self.ns_light.next_state()
            self.ew_light.next_state()

            self.set_light_color(self.ns_lights, self.ns_light.state)
            self.set_light_color(self.ew_lights, self.ew_light.state)

            self.update_pedestrian_lights()

        self.root.after(1000, self.update_gui)

    def update_pedestrian_lights(self):
        # Pedestrian walks when traffic light is RED
        ns_color = "green" if self.ns_light.state == "RED" else "red"
        ew_color = "green" if self.ew_light.state == "RED" else "red"

        self.canvas.itemconfig(self.ns_ped_light, fill=ns_color)
        self.canvas.itemconfig(self.ew_ped_light, fill=ew_color)

        # Change pedestrian emoji color to match the fill color using text color trick
        # Tkinter canvas text doesn't support color change for emojis, so we keep emoji same
        # Could replace emoji with image for more control if needed

    def start_simulation(self):
        self.running = True

    def pause_simulation(self):
        self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficLightGUI(root)
    app.update_gui()
    root.mainloop()
