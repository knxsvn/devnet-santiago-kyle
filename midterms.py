pets = ["jumbo rat "]  # starts empty — the user adds pets as the program runs

def display_menu():
    # print the menu, return the user's choice
    print("1. Add Pet")
    print("2. View all Pets")
    print("3. Count available vs adopted")
    print("4. Find a pet by name")
    print("5. Exit")
    print("Choose a number: ")
    
def add_pet(pet_list):
    # ask for name, animal type, status — build the string, add to the list
    name = input("Enter your pets name:")
    print(f"Hello {name}")
    type = input("What is your pets type?: ")
    status = input("What is your pets status?: ")
    print(f"Hello1{name}I see that you're a {type} with a{status} status")

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
       # use if/elif to call the right function based on choice
              # set running = False when the user picks Exit     
display_menu()
    try: 
    
    choice = int(input("Choose a number: "))
    if  input == 1:
        add_pet(pets)
    elif input == 2:
        view_pets(view_pets)
    elif input == 3:
        count_available_adopted(count_available_adopted)
    elif input == 4:
        find_pet(find_pet)
    else: 
        print(f"You chose: {choice} Exit.")    
        
    except ValueError:
         print("Enter a valid number")
    
main()    