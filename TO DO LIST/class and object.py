# created a  class
class Task:
    def __init__(self,t:str,p:str,d:str,c:str) -> None:
        self.task = t
        self.priority = p
        self.due_date = d
        self.__completed = c

    def __str__(self) -> str:
        return (
            f"Task : {self.task}"'\n'
            f"Priority : {self.priority}"'\n'
            f"Due Date : {self.due_date}"'\n'
            f"Completed : {self.__completed}"
              )
    # print all the objects from the class
    def display(self):
        print(self)

    # right now we are not using this in next version we may add it again.
    # # changes the completion status 
    # def mark_completed(self)-> None:
    #     if self.__completed == "yes":
    #         print("Task is already completed")
        # else:
        #     self.__completed = "yes"

    # getter method to access output
    def get_completed(self) -> str:
        return self.__completed

    # setter 
    def set_completed(self,update :str) -> None:
        self.__completed = update

# loading the task from the file
def load_tasks():
    try:
        data = []
        with open("to_do_list.txt", "r") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    lists = line.split("|")
                    content = Task(t = lists[0].strip().lower(),p = lists[1].strip().lower() ,
                            d = lists[2].strip().lower(), c = lists[3].strip().lower())
                    data.append(content)
                except IndexError:
                    print("Task has only half values")
                    continue
    except FileNotFoundError:
        print("File not found.")
    return data

# # Load tasks into a list
tasks = load_tasks()

# # for testing 
# task1 = Task("learn python", "high", "12/09/2026", "no")
# task2 = Task("practice sql", "low", "13/09/2026", "no")
# task3 = Task("update resume", "low", "15/09/2026", "yes")

# tasks = [task1, task2, task3]

# Display application title
print("================")
print(f"   TO_DO_LIST   ")
print("================")

# Main function to control the program
def main(tasks):
    while True:
        display_menu()
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
def display_menu():
# printing the menu
    print("==== MENU ====")
    print(f" 1. ADD \n 2. VIEW\n 3. DELETE\n 4. EDIT\n 5. EXIT")
    print("==============\n")

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
    while True:
        try:
            n = int(input("Enter no of tasks : "))
            if n < 1:
                print("Input Error! Please enter a positive number")
                continue
            for i in range(1, n+1):
                to_do = Task(t = input(f"Enter the task{i} : ").strip().lower(),p =input("Give priority('low', 'medium', 'high'):").strip().lower() ,
                d = input("Enter Due date : ").strip().lower(), c = input("Is task completed (yes or no): ").strip().lower())
                tasks.append(to_do)
                print()
                # updating the file
                update_file(tasks)
            break
        except ValueError:
            print("Wrong input. Re-enter a number not a string")
                

# Display all tasks
def view_task(tasks):
    print()
    if tasks:
        for index, task in enumerate(tasks,start = 1):
            print(f"Task no: {index}")
            task.display()
            print()

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
                    # updating the file
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
                if 0 < index <= len(tasks):                
                    index = index - 1
                    # calling the change_attribute function
                    change_attribute(tasks,index)
                    # updating the file
                    update_file(tasks)
                    break
        
                else:
                    print("Index is out of bound so enter correct index")
            else:
                print("First you need to add task to edit something")

        except ValueError:
            print("You have to enter integer not alphabets or string")


# created a function to choose which attribute to change 
def change_attribute(tasks,index):
    while True:
        try:
            attribute_change = int(input('Which attribute you want to change("1 - task","2 - priority","3 - due_date","4 - completed"):'))
            
            if attribute_change == 1:
                new_task = input("Enter new task: ").strip().lower()
                if not new_task:
                    print("Task cannot be empty")
                    continue
                print(f"The {tasks[index].task} is replaced by {new_task}")
                tasks[index].task = new_task

            elif attribute_change == 2:
                new_priority = int(input("Enter an option (1 - low,2 - medium,3 - high): "))
                if new_priority == 1:
                    new_priority = "low"
                elif new_priority == 2:
                    new_priority = "medium"
                elif new_priority == 3:
                    new_priority = "high"
                else:
                    print("Choose a correct option ")
                    continue
                print(f"The {tasks[index].priority} is replaced by {new_priority}")
                tasks[index].priority = new_priority

            elif attribute_change == 3:
                new_due_date = input("Enter a new due date: ").strip()
                print(f"The {tasks[index].due_date} is replaced by {new_due_date}")
                tasks[index].due_date = new_due_date
            
            elif attribute_change == 4:
                
                    completed = input("Enter only 'yes' or 'no':").strip().lower()
                    if completed in ("yes" ,"no"):
                        tasks[index].set_completed(completed)
                        print("The status has been changed successfully!")
                        break  
                    else:
                        print(f"{completed} is not valid! Change it again")
                        print("The status has not changed")
            else :
                print("please enter a correct option")
                continue
            # to terminate the loop            
            stop = input("Do you want to edit another attribute? yes/no: ").strip().lower()
            if stop != "yes":
                break

        except ValueError:
                print("You have enter an string. so enter positive values from shown option! ")


# Save tasks to the file
def update_file(tasks):
    with open("to_do_list.txt","w") as f:
            for task in tasks:
                lists = task.task + "|" +  task.priority + "|" + task.due_date + "|" + task.get_completed()
                f.writelines(lists + "\n")

# calling the main function
if not tasks:
        print("List is empty.\nAdd task to the list\n")
        add_task(tasks)

main(tasks)