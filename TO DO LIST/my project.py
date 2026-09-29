tasks = ["python","css","java"]
print("================")
print(f"   TO_DO_LIST   ")
print("================")

# main funtion to manage all the functions
def main(tasks):
    while True:
        display_menu(tasks)
        menu_option = userchoice()
        if menu_option == 4:
            break

# fuction helps to display the task menu 
def display_menu(tasks):
    if len(tasks) == 0:
        print("List is empty.\nAdd a task to the list\n")
    print()
# asking user to selecrt an option
    print("==== MENU ====")
    print(f" 1. ADD \n 2. VIEW\n 3. DELETE\n 4. EXIT")
    print("= ========== =\n")
# funtion to choose a option for the user
def userchoice():
    user_option = int(input("Select a number from the menu: "))
    if user_option == 1:
        add_task(tasks)
    elif user_option == 2:
        view_task(tasks)
    elif user_option == 3:
        delete_task(tasks)
    elif user_option == 4:
        return user_option
    else:
        print("Invalid! Please choose option from the menu\n")

# function to add the taks into list
def add_task(tasks):
    print("""You have four options please choose any of them to add
1. Jogging, 2. Excersice, 3. Freshup and Breakfast 4. Learning Python\n""")
        
    a = input("Enter a task from the given options to add into the list: ").strip().lower()
    if a in tasks:
        print(f"{a} is already in the task choose another option to add\n")
    else:
        tasks.append(a)

# function to display the list 
def view_task(tasks):
    print()
    print(f"TO_DO_LIST : {tasks}")
    i = 1
    for task in tasks:
        print(f"{i}.",task)
        i += 1
# function to delete a task from the list
def delete_task(tasks):
    if tasks:
        d = int(input("choose a number to be delete the task: "))
        if d <= 0:
            print("invalid value,please enter correct value!\n")

        elif d > len(tasks):
            print("you have entered beyond the index, so please select a number which is eqaul to the length of list\n")  

        else:
            tasks.pop(d-1) 
    else:
        print("No tasks available to delete.")

main(tasks)
