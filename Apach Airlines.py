# Initialize an empty dictionary to store the seat map.
seat_map = {}

# Define rows and columns for the seat map.
rows = ['A', 'B', 'C', 'D', 'E', 'F']
cols = [str(i) for i in range(1, 81)]  # Generate column labels from 1 to 80 as strings.

# Initialize all seats as free, with special designations for storage and aisles.
for row in rows:
    for col in cols:
        if row in ['D', 'E'] and (col == '78' or col == '79'):
            seat_map[row + col] = 'S'  # Mark these seats as storage area.
        elif col == 'X':
            seat_map[row + col] = 'X'  # Placeholder for future aisle handling, currently not active.
        else:
            seat_map[row + col] = 'F'  # All other seats are marked as free.

# Function to ensure the seat input is in the correct format (e.g., A1).
def normalize_seat(seat):
    seat = seat.upper()
    if seat[0].isalpha() and seat[1:].isdigit():
        return seat
    elif seat[0].isdigit() and seat[1:].isalpha():
        return seat[1] + seat[0]
    else:
        return None

# Function to check the availability of a seat.
def check_availability():
    seat = input("Enter seat (e.g., A1): ")
    seat = normalize_seat(seat)
    if seat and seat_map.get(seat) == 'F':
        print(f"Seat {seat} is available.")
    elif seat and seat_map.get(seat) == 'R':
        print(f"Seat {seat} is not available.")
    else:
        print(f"Invalid seat {seat}.")

# Function to book a seat.
def book_seat():
    seat = input("Enter seat (e.g., A1): ")
    seat = normalize_seat(seat)
    if seat and seat_map.get(seat) == 'F':
        seat_map[seat] = 'R'  # Mark the seat as reserved.
        print(f"Seat {seat} booked successfully.")
    elif seat and seat_map.get(seat) == 'R':
        print(f"Seat {seat} is already booked.")
    else:
        print(f"Invalid seat {seat}.")

# Function to free a reserved seat.
def free_seat():
    seat = input("Enter seat (e.g., A1): ")
    seat = normalize_seat(seat)
    if seat and seat_map.get(seat) == 'R':
        seat_map[seat] = 'F'  # Mark the seat as free again.
        print(f"Seat {seat} freed successfully.")
    elif seat and seat_map.get(seat) == 'F':
        print(f"Seat {seat} is already free.")
    else:
        print(f"Invalid seat {seat}.")

# Function to display the current booking state of all seats.
def show_booking_state():
    print("   A  B  C  X  D  E  F")

    for i, col in enumerate(cols):
        print(f"{col:<3}", end='')  # Print column numbers.
        for row in rows:
            print(seat_map[row + col], end='  ')  # Print seat states.
            if row == 'C':
                print("X", end='  ')  # Print an aisle marker.
        print()  # Start a new line after each column.

# Main menu loop for user interaction.
while True:
    print("\nMenu:")
    print("1. Check availability of seat")
    print("2. Book a seat")
    print("3. Free a seat")
    print("4. Show booking state")
    print("5. Exit program")

    choice = input("Enter your choice: ")  # Prompt user for a choice.
    if choice == '1':
        check_availability()
    elif choice == '2':
        book_seat()
    elif choice == '3':
        free_seat()
    elif choice == '4':
        show_booking_state()
    elif choice == '5':
        print("Exiting program.")
        break  # Exit the loop to end the program.
    else:
        print("Invalid choice. Please try again.")  # Handle invalid inputs.
