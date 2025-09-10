'''


To-Do List App (Console Based)

Use a Python list to store tasks.

Features: Add, remove, update, mark as done.

Example: tasks = ["Buy milk", "Complete Assignment"]

'''




# todo = []
# donetask = []
# while True: 
#     task = input("\n Enter Your Task : ") # To Complete 1 DSA Question 

#     value = int(input("1-Add, 2-Remove, 3-Update, 4-Mark As Done \n"))
#     if value == 1:
#         todo.append(task)
#         print("To Do Tasks: ", todo)

#     elif value == 2:
#         todo.pop()
#         print("To Do Tasks: ", todo)
#     elif value == 3:
#         todo[-1] = input("\n Enter Your Updated Task : ") #Update the task (you are editting it)
#         print("To Do Tasks: ", todo)
#     else:
#         donetask.extend(list(todo.pop()))
#         print("Done Task : ", donetask)
#         print("To Do Tasks: ", todo)


    





# Try - 2

import time 
todo = []
mark_done = []
while True:
    time.sleep(1)
    print("\n\n ---------------------------------------------------------------")
    value = int(input("\n ------------------ To Do App : Choose One Option :-------------- \n 0 - Show Tasks \n 1 - Add \n 2 - Remove \n 3 - Update \n 4 - Mark As Done \n 5 - Quit \n\n "))
    time.sleep(2)

    if value == 0:
        if todo == []:
            print("Current Tasks : ","No Tasks Yet!")
        else: 
            print("Current Tasks : ",todo)
        
    elif value == 1:
        task = input("\n Enter Your Task : ")
        todo.append(task)
        time.sleep(1)
        print("Task Added Successfully!")
    elif value == 2: 
        print("Current Tasks : ",todo)
        time.sleep(1)
        task_delete = input("Type the task that you wanna delete it : ")
        todo.remove(task_delete)
        time.sleep(2)
        print("Task Deleted Successfully!")

    elif value == 3:
        print("Current Tasks : ",todo)
        task_update = input("Type the Task that you want to Update It : ") #element
        for index in range(len(todo)):
            if todo[index] == task_update:
                myindex = index
                break 
        todo[myindex] = input("Enter Updated Task : ")
        print("Task Updated!")
    elif value == 4:
        print("Current Tasks : ",todo)
        task_done = input("Type the Task that you want to Mark As Done : ") #element
        todo.remove(task_done)
        mark_done.append(task_done)
        print("\nMark As Done Tasks :",mark_done)
        print("\nTasks to To Do :",todo)
    elif value == 5:
        print("Thanks for using application!")
        break
    else:
        print("Invalid Choice")
        break


    # break