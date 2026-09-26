pets = [" "]  # starts empty — the user adds pets as the program runs

def display_menu():
    # print the menu, return the user's choice
    print("=== Pet Adoption Records ===")
    choice = input("Choose One")
    print("1. Add Pet")
    print("2. View all Pets")
    print("3. Count available vs adopted")
    print("4. Find a pet by name")
    print("5. Exit")

print(f"You chose: {choice}")

def add_pet(pet_list):
    # ask for name, animal type, status — build the string, add to the list
    pass

def view_pets(pet_list):
    # loop through and print every pet — handle empty list
    pass

def count_available_adopted(pet_list):
    # loop through, count Available vs Adopted, return both
    pass

def find_pet(pet_list):
    # ask for a name, search the list, print result or "not found"
    
    pass

# BONUS (optional)
def remove_pet(pet_list):
    # your code here
    pass

def main():
    running = True
    while running:
        choice = display_menu()
        break;
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit      
main()    
       