#Task 1 - To Do List
import os

#Display list 
def display_list():
    with open("todolist.txt","r") as f:
        lst=f.readlines()
        if not lst:
            print("The List is empty!")
        else:
            print("*********** TO DO LIST ***********")
            print("\n")

            for i,item in enumerate(lst,1):
                print(i,". ", item.strip())

            print("\n**********************************")

#Create item
def add_item():
    new_item=input("Enter the new to do task: ")
    with open("todolist.txt", "a") as f:
        f.writelines(new_item + "\n")
        print(new_item, "added to your list.\n")  


#Update item
def update_item():
    display_list()
    item_num=int(input("Enter the number of the item to be updated: "))
    with open("todolist.txt","r") as fr:
        lst=fr.readlines()
        if 1<=item_num<=len(lst):
            mod_item=input("Enter the updated item: ")
            lst[item_num - 1]= mod_item
            with open("todolist.txt","w") as fw:
                fw.writelines(lst)
                print("Item number ",item_num," updated to: ", mod_item)
        else:
            print("Please enter valid item number!")

#Delete item
def delete_item():
    display_list()
    delete_item_number=int(input("Enter the item number of the task that you want to remove: "))
    with open("todolist.txt","r")as fr:
        lst=fr.readlines()
        if 1<=delete_item_number<=len(lst):
            poped_item=lst.pop(delete_item_number - 1)
            with open("todolist.txt","w")as fw:
                fw.writelines(lst)
                print(delete_item_number, ". ", poped_item, " is removed from the list.")
        else:
            print("Enter the valid item number!")


#Main 
while True:
    print("\n*************TO DO LIST APPLICATION*************\n")
    print("\n==================OPTIONS=================\n")
    print("1. Display To Do List\n")
    print("2. Add a new To Do item\n")
    print("3. Update a To Do item\n")
    print("4. Remove a To Do item\n")
    print("5. Exit")
    print("\n==========================================\n")
    choise=int(input("Please enter your choise from the above options(1/2/3/4/5): "))
    if 1<=choise<=5:
        match choise:
            case 1:
                display_list()
            case 2:
                add_item()
            case 3:
                update_item()
            case 4:
                delete_item()
            case 5:
                print("Goodbye!")
                break
    else:
        print("Please enter the valid option in numbers.")





