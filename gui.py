import tkinter as tk
from tkinter import messagebox


class ElevatorSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Elevator Simulator")
        self.current_floor = 0
        self.stops = set()

         # Set window size
        self.root.geometry("400x300")  # Width x Height
        
        # Create UI elements
        self.floor_label = tk.Label(root, text="Currently at Floor: 0")
        self.floor_label.pack()

        self.floor_entry = tk.Entry(root, width=40)
        self.floor_entry.insert(0, "Enter Floor (A, B, or C)")  # Placeholder text
        self.floor_entry.bind("<FocusIn>", self.clear_placeholder)  # Clear placeholder text on focus
        self.floor_entry.bind("<FocusOut>", self.restore_placeholder)  # Restore placeholder text if empty on focus out
        self.floor_entry.pack(pady=20)
        

        self.request_button = tk.Button(root, text="Request Floor", command=self.request_floor, bg="blue", fg="white")
        self.request_button.pack(pady=5)

        self.next_stop_button = tk.Button(root, text="Alight", command=self.process_next_stop, bg="green", fg="white")
        self.next_stop_button.pack(pady=5)

    def request_floor(self):
        try:
            floor = int(self.floor_entry.get())
            if floor >= 0 and floor < 4:
                self.stops.add(floor)
                messagebox.showinfo("Request", f"Floor {floor} requested.")
            else:
                messagebox.showerror("Error", "Please enter a positive integer less than 4.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid floor number.")

    def process_next_stop(self):
        if self.current_floor in self.stops:
            self.open_door()
            self.stops.remove(self.current_floor)
        elif self.current_floor < min(self.stops):
            self.move_up()
        elif self.current_floor > max(self.stops):
            self.move_down()

    def move_up(self):
        # Logic for moving up one floor
        self.current_floor += 1
        self.update_floor_label()

    def move_down(self):
        # Logic for moving down one floor
        self.current_floor -= 1
        self.update_floor_label()

    def open_door(self):
        # Logic for opening the door
        messagebox.showinfo("Door", f"Door opened at Floor {self.current_floor}")

    def update_floor_label(self):
        self.floor_label.config(text=f"Current Floor: {self.current_floor}")
        
    def clear_placeholder(self, event):
        if self.floor_entry.get() == "Enter Floor (A, B, or C)":
            self.floor_entry.delete(0, tk.END)

    def restore_placeholder(self, event):
        if not self.floor_entry.get():
            self.floor_entry.insert(0, "Enter Floor (A, B, or C)")

if __name__ == "__main__":
    root = tk.Tk()
    app = ElevatorSimulator(root)
    root.mainloop()
