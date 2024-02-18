floors = [0,'A', 'B', 'C']

#defining a class for the elevator
class elevator():
    def __init__(self, floors):
        self.current_state = 0
        self.floors = floors
        
    def transition_function(self, floors):
        if user_input == 'A':
            self.current_state += 1
        if user_input == 'B':
            self.current_state += 2
        if user_input == 'C':
            self.current_state += 3
        else:
            print("Invalid")
print("Elevator Machine Simulation")           
while True:          
    user_input = input("Enter the floor i.e A, B, C or X to exit \n")
    start = elevator(floors)

    start.transition_function(user_input.lower())

