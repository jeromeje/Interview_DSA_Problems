class Passenger:
    def __init__(self, name, age, preference):
        self.name = name
        self.age = age
        self.preference = preference
    
class Train:
    def __init__(self):
        self.total_seats = 1   #63
        self.available_seats = 1 
        self.rac_seats = 1  
        self.waiting_list_seats = 1
        self.booked_list= []
        self.waiting_list= []
        self.rac_list= []
    
    def book_ticket(self, passenger):
        if self.available_seats > 0:
            self.available_seats -= 1
            self.booked_list.append(passenger)
            print(f"Ticket booked for {passenger.name}.")
        elif self.rac_seats > 0:
            self.rac_seats -= 1
            self.rac_list.append(passenger)
            print(f"RAC ticket booked for {passenger.name}.")
        elif self.waiting_list_seats > 0:
            self.waiting_list_seats -= 1
            self.waiting_list.append(passenger)
            print(f"Waiting list ticket booked for {passenger.name}.")
        else:
            print("No available seats.")
            
    def cancel_ticket(self, passenger):
        if passenger in self.booked_list:
            self.booked_list.remove(passenger)
            self.available_seats += 1
            print(f"Ticket cancelled for {passenger.name}.")
           
            if self.rac_list:
                next_rac_passenger = self.rac_list.pop(0)
                self.book_ticket(next_rac_passenger)
                print(f"RAC ticket automatically booked for {next_rac_passenger.name}.")
                self.rac_seats += 1
            if self.waiting_list:
                next_passenger = self.waiting_list.pop(0)
                self.book_ticket(next_passenger)
                print(f"Ticket automatically booked for {next_passenger.name} from waiting list.")
                self.waiting_list_seats += 1
        elif passenger in self.rac_list:
            self.rac_list.remove(passenger)
            self.rac_seats += 1
            print(f"RAC ticket cancelled for {passenger.name}.")
            if self.waiting_list:
                next_passenger = self.waiting_list.pop(0)
                self.book_ticket(next_passenger)
                print(f"Ticket automatically booked for {next_passenger.name} from waiting list.")
                self.waiting_list_seats += 1
        elif passenger in self.waiting_list:
            self.waiting_list.remove(passenger)
            self.waiting_list_seats += 1
            print(f"Waiting list ticket cancelled for {passenger.name}.")
        else:
            print("Passenger not found.")
        
    def display_status(self):
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")
        print(f"RAC Seats: {self.rac_seats}")
        print(f"Waiting List Seats: {self.waiting_list_seats}")
        print("Booked Passengers:", [p.name for p in self.booked_list])
        print("RAC Passengers:", [p.name for p in self.rac_list])
        print("Waiting List Passengers:", [p.name for p in self.waiting_list])
        
def main(): 
    while True:
        input_choice = input("Enter 1 to book ticket, 2 to cancel ticket, 3 to display status, or 'exit' to quit: ")
        if input_choice == 'exit':
            print("Exiting the system.")
            break
        elif input_choice == '1':
            name = input("Enter passenger name: ")
            age = int(input("Enter passenger age: "))
            preference = input("Enter preference (e.g., window, aisle): ")
            passenger = Passenger(name, age, preference)
            Train.book_ticket(passenger)
        elif input_choice == '2':
            name = input("Enter passenger name to cancel ticket: ")
            passenger = next((p for p in Train.booked_list if p.name == name), None)
            if not passenger:
                passenger = next((p for p in Train.rac_list if p.name == name), None)
            if not passenger:
                passenger = next((p for p in Train.waiting_list if p.name == name), None)
            Train.cancel_ticket(passenger)
        elif input_choice == '3':
            Train.display_status()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # train = Train(total_seats=63, available_seats=63, rac_seats=20, waiting_list_seats=20)
    Train = Train()
    main()
    