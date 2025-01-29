import pandas as pd           
class Cab:
    def __init__(self, cab_id, driver_name, location, available=True):
        self.cab_id = cab_id                                         
        self.driver_name = driver_name                               
        self.location = location                                     
        self.available = available                                   
    
    def update_location(self, new_location):              
        self.location = new_location                      
    
    def make_available(self):                             
        self.available = True
    
    def make_unavailable(self):                           
        self.available = False


class CabManagementSystem:
    def __init__(self):
        self.cabs = pd.DataFrame(columns=['Cab ID', 'Driver Name', 'Location', 'Available'])
        self.bookings = {}
    
    def add_cab(self, cab_id, driver_name, location, available=True):
        new_cab = Cab(cab_id, driver_name, location, available)
        self.cabs = pd.concat([self.cabs, pd.DataFrame({'Cab ID': [new_cab.cab_id],                                    
                                                         'Driver Name': [new_cab.driver_name],                         
                                                         'Location': [new_cab.location],                               
                                                         'Available': [new_cab.available]})],                          
                                                         ignore_index=True)
        print(f"Cab {cab_id} added successfully.")                                                                    
    
    def update_cab_location(self, cab_id, new_location):                                   
        cab_index = self.cabs.index[self.cabs['Cab ID'] == cab_id].tolist()               
        if cab_index:
            cab_index = cab_index[0]
            self.cabs.loc[cab_index, 'Location'] = new_location                            
            print(f"Cab {cab_id} location updated to {new_location}.")                     
        else:
            print(f"Cab {cab_id} not found.")                                              

    def update_cab_availability(self, cab_id, available):                                     
        cab_index = self.cabs.index[self.cabs['Cab ID'] == cab_id].tolist()
        if cab_index:
            cab_index = cab_index[0]
            self.cabs.loc[cab_index, 'Available'] = available                     
            print(f"Cab {cab_id} availability updated.")                                   
        else:
            print(f"Cab {cab_id} not found.")                                              
    
    
    def display_available_cabs(self):
        available_cabs = self.cabs[self.cabs['Available'] == True]
        print(available_cabs)
    
    def book_cab(self, user_id, cab_id):                                                   
        if cab_id in self.cabs['Cab ID'].values:
            if self.cabs.loc[self.cabs['Cab ID'] == cab_id, 'Available'].values[0]:
                
                self.cabs.loc[self.cabs['Cab ID'] == cab_id, 'Available'] = False
                self.bookings[user_id] = cab_id
                print(f"Cab {cab_id} booked successfully.")                                
            else:
                print(f"Cab {cab_id} is not available.")                                   
        else:
            print(f"Cab {cab_id} not found.")                                              
    
    
    def end_trip(self, user_id):                                                           
        if user_id in self.bookings:
            cab_id = self.bookings.pop(user_id)
            self.cabs.loc[self.cabs['Cab ID'] == cab_id, 'Available'] = True          
            print(f"Trip ended. Cab {cab_id} is now available.")                           
        else:
            print("No ongoing trip for this user.")
    
    def display_bookings(self):
        print("Current bookings:")
        print(self.bookings)
                                                                          
def main():
    cab_system = CabManagementSystem()
     
    while True:
        print("\nMenu:")                                                                   
        print("1. Add Cab")
        print("2. Update Cab Location")
        print("3. Update Cab Availability")
        print("4. Display Available Cabs")
        print("5. Book Cab")
        print("6. End Trip")
        print("7. Display Bookings")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':                                                                 
            cab_id = int(input("Enter Cab ID: "))
            driver_name = input("Enter Driver Name: ")
            location = input("Enter Location: ")
            cab_system.add_cab(cab_id, driver_name, location)
        elif choice == '2':                                                             
            cab_id = int(input("Enter Cab ID: "))
            new_location = input("Enter new Location: ")
            cab_system.update_cab_location(cab_id, new_location)
        elif choice == '3':                                                              
            cab_id = int(input("Enter Cab ID: "))
            available = input("Enter availability (True/False): ").lower() == 'true'
            cab_system.update_cab_availability(cab_id, available)
        elif choice == '4':                                                             
            cab_system.display_available_cabs()
        elif choice == '5':                                                              
            user_id = input("Enter User ID: ")
            cab_id = int(input("Enter Cab ID to book: "))
            cab_system.book_cab(user_id, cab_id)
        elif choice == '6':                                                              
            user_id = input("Enter User ID: ")
            cab_system.end_trip(user_id)
        elif choice == '7':                                                              
            cab_system.display_bookings()
        elif choice == '8':                                                              
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")                                   

if __name__ == "__main__":
    main()  