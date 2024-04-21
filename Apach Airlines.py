import random
import string

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
# Define a dictionary to store booking details
booking_details = {}


# Function to ensure the seat input is in the correct format (e.g., A1).
def normalize_seat(seat):
    seat = seat.upper()
    if seat[0].isalpha() and seat[1:].isdigit():
        return seat
    elif seat[0].isdigit() and seat[1:].isalpha():
        return seat[1] + seat[0]
    else:
        return None


# Function to generate a random booking reference
def generate_booking_reference(existing_references):
    # Continuously generate new references until a unique one is found
    while True:
        # Generate a random string of 8 characters, choosing from uppercase letters and digits
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

        # Check if the generated reference is not already in the list of existing references
        if reference not in existing_references:
            # If the reference is unique, return it and break out of the loop
            return reference


# Function to check seat availability
def check_availability():
    seat = input("Enter seat (e.g., A1): ")
    seat = normalize_seat(seat)
    if seat and seat_map.get(seat) == 'F':
        print(f"Seat {seat} is available.")
    elif seat and seat_map.get(seat) in booking_details:
        print(f"Seat {seat} is already booked with reference {seat_map[seat]}.")
    else:
        print(f"Invalid seat {seat}.")


def book_seat():
    seat = input("Enter seat (e.g., A1): ")
    seat = normalize_seat(seat)
    if seat and seat_map.get(seat) == 'F':
        booking_ref = generate_booking_reference(booking_details.keys())  # Generate a booking reference
        # Store booking reference and customer data
        booking_details[booking_ref] = {
            'seat': seat,
            'passport_number': input("Enter passport number: "),
            'first_name': input("Enter first name: "),
            'last_name': input("Enter last name: ")
        }
        seat_map[seat] = booking_ref  # Update seat status with booking reference
        print(f"Seat {seat} booked successfully with reference {booking_ref}.")
    elif seat and seat_map.get(seat) != 'F':
        print(f"Seat {seat} is already booked.")
    else:
        print(f"Invalid seat {seat}.")


# Function to free a reserved seat.
def free_seat():
    seat = input("Enter seat (e.g., A1): ")
    seat = normalize_seat(seat)
    if seat and seat_map.get(seat) in booking_details:
        del booking_details[seat_map[seat]]  # Remove booking details
        seat_map[seat] = 'F'  # Free the seat
        print(f"Seat {seat} freed successfully.")
    elif seat and seat_map.get(seat) != 'R':
        print(f"Seat {seat} is already free.")
    else:
        print(f"Invalid seat {seat}.")


# Function to display the current booking state of all seats.
def show_booking_state():
    print("   A  B  C  X  D  E  F")

    for i, col in enumerate(cols):
        print(f"{col:<3}", end='')  # Print column numbers.
        for row in rows:
            seat = row + col
            if seat_map[seat] == 'F' or seat_map[seat] == 'S':
                print(seat_map[seat], end='  ')  # Print seat states as 'F' or 'S'.
            else:
                print('R', end='  ')  # Print 'R' for reserved/booked seats.
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

