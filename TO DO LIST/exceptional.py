tasks = []
print("================")
print(f"   TO_DO_LIST   ")
print("================")

# main funtion to manage all the functions
def main(tasks):
    while True:
        display_menu(tasks)
        menu_option = userchoice()
        if menu_option == 1:
            add_task(tasks)
        elif menu_option == 2:
            view_task(tasks)
        elif menu_option == 3:
            delete_task(tasks)
        elif menu_option ==4:
            edit_task(tasks)
        elif menu_option == 5:
            break

# fuction helps to display the task menu 

def display_menu(tasks):
    if len(tasks) == 0:
        print("List is empty.\nAdd a task to the list\n")
        print()

# printing the menu

    print("==== MENU ====")
    print(f" 1. ADD \n 2. VIEW\n 3. DELETE\n 4. EDIT\n 5. EXIT")
    print("= ========== =\n")

# funtion to choose a option for the user

def userchoice():
    try:
        user_option = int(input("Select a number from the menu: "))
        return user_option
    except ValueError as e:
        print(f"{type(e).__name__}, so enter a real value")
    
# function to add the taks into list

def add_task(tasks):
    print("""You have four options please choose any of them to add
1. Jogging, 2. Excersice, 3. Freshup and Breakfast 4. Learning Python\n""")
        
    a = input("Enter a task from the given options to add into the list: ").strip().lower()
    print()
    if a in tasks:
        print(f"{a} is already in the task choose another option to add\n")
    else:
        tasks.append(a)

# function to display the list 

def view_task(tasks):
    print()
    print(f"TO_DO_LIST : {tasks}")
    if tasks:
        i = 1
        for task in tasks:
            print(f"{i}.",task)
            i += 1
    else:
        print("The list empty!")

# function to delete a task from the list

def delete_task(tasks):
    while True:
        try:
            if tasks:
                d = int(input("choose a number to be delete the task: "))
                if d <= 0:
                    print("invalid value, enter positive values\n")

                elif d > len(tasks):
                    print(f"you have entered beyond the index, the range of the list is {len(tasks)}\n")  

                else:
                    tasks.pop(d-1) 
                    break
            else:
                print("No tasks available to delete.")
                break
        except ValueError as e:
            print(f"{type(e).__name__}, you must enter a number")

# funtion to edit a task in the list 
def edit_task(tasks):
    while True:
        try:
            view_task(tasks)
            if tasks:
                index = int(input("which index do you want to edit? : "))
                if index <= len(tasks) and index > 0:
                    new_task = input("Enter new task: ").strip().lower()
                    
                    if new_task and new_task.isalpha():
                        index = index - 1
                        if new_task in tasks:
                            print("The task is already exist and list is unchanged!")
                        else:
                            print(f"The {tasks[index]} is replaced by {new_task}")
                            tasks[index] = new_task
                            stop = input("Do you want to edit anything? enter 'yes'").lower()
                            if stop == "yes":
                                continue
                            else:
                                break
                    else:
                        print("There is no new_task. so enter a task")
        
                else:
                    print("Index is out of bound so enter correct index")
            else:
                print("First you need to add task to edit something")

        except ValueError:
            print("You have to enter integer not alphabets or string")
main(tasks)

