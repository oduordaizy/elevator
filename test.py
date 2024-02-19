import tkinter as tk
from tkinter import messagebox


class ElevatorSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Elevator Simulator")
        self.current_floor = 0
        self.stops = set()

        # Create frames
        self.floor_frame = tk.Frame(root)
        self.floor_frame.pack(pady=10)

        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=10)

       # Create UI elements for floor frame
        self.floor_label = tk.Label(self.floor_frame, text=" 00", font=("Comic Sans MS", 24, "bold", "italic"))
        self.floor_label.grid(row=0, column=0, columnspan=2, padx=10)

        self.floor_entry = tk.Entry(self.floor_frame, width=30)
        self.floor_entry.insert(0, "Enter Floor (0, 1, 2, or 3)")  # Placeholder text
        self.floor_entry.bind("<FocusIn>", self.clear_placeholder)  # Clear placeholder text on focus
        self.floor_entry.bind("<FocusOut>", self.restore_placeholder)  # Restore placeholder text if empty on focus out
        self.floor_entry.grid(row=1, column=0, padx=(10, 5), pady=5)  # Adjust padx for entry

        self.floor_buttons = []
        floor_button = tk.Button(self.floor_frame, text="0", command=lambda: self.select_floor(0))
        floor_button.grid(row=1, column=1, padx=(0, 5), pady=5)  # Decrease padx for button 0
        self.floor_buttons.append(floor_button)

        for i in range(0, 4):
            if i == 0:
                floor_button = tk.Button(self.floor_frame, text=str(i), command=lambda i=i: self.select_floor(i))
                floor_button.grid(row=1, column=1, padx=(0, 5), pady=5)  # Decrease padx for button 0
            else:
                floor_button = tk.Button(self.floor_frame, text=str(i), command=lambda i=i: self.select_floor(i))
                floor_button.grid(row=1 + (i-1) // 2, column=(i-1) % 2 + 2, padx=5, pady=5)  # Use default padx for other buttons
            self.floor_buttons.append(floor_button)

        # Create UI elements for control frame
        self.request_button = tk.Button(self.control_frame, text="GO", command=self.request_floor, bg="blue", fg="white")
        self.request_button.pack(side=tk.LEFT, padx=5)

        self.next_stop_button = tk.Button(self.control_frame, text="OPEN DOOR", command=self.process_next_stop, bg="green", fg="white")
        self.next_stop_button.pack(side=tk.LEFT, padx=5)
        
        self.request_button = tk.Button(self.control_frame, text="-->", command=self.move_up, bg="green", fg="white")
        self.request_button.pack(side=tk.LEFT, padx=5)
        
        self.request_button = tk.Button(self.control_frame, text="<--", command=self.move_down, bg="green", fg="white")
        self.request_button.pack(side=tk.LEFT, padx=5)

    def select_floor(self, floor):
        self.floor_entry.delete(0, tk.END)
        self.floor_entry.insert(0, str(floor))

    def request_floor(self):
        try:
            floor = int(self.floor_entry.get())
            if floor >= 0 and floor < 4:
                self.stops.add(floor)
                messagebox.showinfo("Request", f"Floor {floor} requested.")
            else:
                messagebox.showerror("Error", "Please enter a floor between 0 and 3.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid floor number.")

    def process_next_stop(self):
        if self.current_floor in self.stops:
            self.open_door()
            self.stops.remove(self.current_floor)
        elif self.stops:  # Check if there are any floors requested
            if self.current_floor < min(self.stops):
                self.move_up()
            elif self.current_floor > max(self.stops):
                self.move_down()
        else:
            messagebox.showinfo("No Stops", "No floors requested.")

    def move_up(self):
        self.current_floor += 1
        self.update_floor_label()

    def move_down(self):
        self.current_floor -= 1
        self.update_floor_label()

    def open_door(self):
        messagebox.showinfo("Door", f"Door opened at Floor {self.current_floor}")

    def update_floor_label(self):
        self.floor_label.config(text=f"Currently at Floor: {self.current_floor:02}")

    def clear_placeholder(self, event):
        if self.floor_entry.get() == "Enter Floor (0, 1, 2, or 3)":
            self.floor_entry.delete(0, tk.END)

    def restore_placeholder(self, event):
        if not self.floor_entry.get():
            self.floor_entry.insert(0, "Enter Floor (0, 1, 2, or 3)")


if __name__ == "__main__":
    root = tk.Tk()
    app = ElevatorSimulator(root)
    root.mainloop()
