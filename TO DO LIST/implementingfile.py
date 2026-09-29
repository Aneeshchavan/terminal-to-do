# loading the task from the file
def load_tasks():
    data = []
    with open("to_do_list.txt", "r") as f:
        for line in f:
            content = line.strip().lower()
            if content:
                data.append(content)

    return data
# Load tasks into a list
tasks = load_tasks()

# Display application title
print("================")
print(f"   TO_DO_LIST   ")
print("================")

# Main function to control the program
def main(tasks):
    while True:
        display_menu(tasks)
        menu_option = get_user_choice()
        # replaced if-else with match case
        match menu_option:
            case 1 : 
                add_task(tasks)
            case 2 : 
                view_task(tasks)
            case 3 : 
                delete_task(tasks)
            case 4: 
                edit_task(tasks)
            case 5 : 
                break

# fuction helps to display the task menu 
def display_menu(tasks):
    if not tasks:
        print("List is empty.\nAdd a task to the list\n")
# printing the menu
    print("==== MENU ====")
    print(f" 1. ADD \n 2. VIEW\n 3. DELETE\n 4. EDIT\n 5. EXIT")
    print("= ========== =\n")

# Get user's menu choice
def get_user_choice():
    while True:
        try:
            user_option = int(input("Select a number from the menu: "))
            if user_option >= 1 and user_option <= 5:
                return user_option
            elif user_option > 5: 
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue
            elif user_option <= 0:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue

        except ValueError as e:
            print(f"{type(e).__name__}, so enter a interger value")

    
# Add a new task
def add_task(tasks):

        
        a = input("Enter a task to add into your list: ").strip().lower()
        print()
        if a == "":
            print("we cannot take empty task, so enter a task!")
        elif a in tasks:
            print(f"{a} is already in the task choose another option to add\n")
        else:
            tasks.append(a)
            update_file(tasks)
            

# Display all tasks
def view_task(tasks):
    print()
    print(f"TO_DO_LIST : {tasks}")
    if tasks:
        for index, task in enumerate(tasks,start = 1):
            print(f"{index}.",task)
    else:
        print("The list empty!")

# Delete a task
def delete_task(tasks):
    while True:
        try:
            view_task(tasks)
            if tasks:
                d = int(input("choose a number to be delete the task: "))
                if d <= 0:
                    print("invalid value, enter positive values\n")

                elif d > len(tasks):
                    print(f"you have entered beyond the index, the range of the list is {len(tasks)}\n")  

                else:
                    tasks.pop(d-1)
                    update_file(tasks)
                    break
            else:
                print("No tasks available to delete.")
                break
        except ValueError as e:
            print(f"{type(e).__name__}, you must enter a number")

# Edit an existing task 
def edit_task(tasks):
    while True:
        try:
            view_task(tasks) # user can view which task is in list 
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
                            update_file(tasks)
                            stop = input("Do you want to edit anything? enter 'yes': ").lower()
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

# Save tasks to the file
def update_file(tasks):
    with open("to_do_list.txt","w") as f:
            f.writelines("\n".join(tasks))

# calling the main function
main(tasks)



