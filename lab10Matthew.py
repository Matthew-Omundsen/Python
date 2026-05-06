#Author: Matthew Omundsen
#Date: 11/4/24
#Program description: grocery list

#GROCERY LIST PROGRAM
#Prompt user to enter items from a grocery list and store them in a list
#Allow user to add or remove items from shopping list before 'going shopping'
#Prompt user to say 'done' after each item is found

#ALGORITHM
#grocery_list = []
#while grocery_item != 'done':
    #grocery_item = input('enter item')
    #grocery_list += [grocery_item]
    #grocery_item = input('enter item')
#print('your list is',grocery_list,end='')
#user_choice = input('add, remove, or shop?')
#if user_choice == 'add':
    #grocery_list while loop
#elif user_choice == 'remove':
    #remove_item = input('what do u want to remove')
    #grocery_list.remove(remove_item)
#elif user_choice == 'shop':
    #for item in grocery_list:
    #print('Go get",grocery_list[item])
    #done = input('type done when u got the item')

#********************************
#*************MAIN***************
#********************************

print("Welcome to the grocery list program!")

#Prompts user to enter first grocery item
grocery_item = input("Enter your first item(type done when finished): ")
grocery_list = []#grocery list
while grocery_item != 'done': #continues adding items until user says 'done'
    grocery_list += [grocery_item]
    grocery_item = input("Enter your next item(type done when finished): ")
print("\nYour grocery list consists of:")
for item in grocery_list:
    print(item) #prints grocery list in a neat way
print("\nWould you like to add items, remove items, or begin shopping?")
user_choice = input("Type add to add more items, remove to get rid \nof"
                    " items, or shop to begin shopping. ")

while user_choice != 'shop': #repeats as long as user doesnt select shop
    if user_choice == 'add':
        grocery_item = input("Enter your next item(type done when finished): ")
        while grocery_item != 'done': #continues adding items until user says 'done'
            grocery_list += [grocery_item]
            grocery_item = input("Enter your next item(type done when finished): ")
        print("\nYour grocery list consists of:")
        for item in grocery_list:
            print(item) #prints grocery list in a neat way
        print("\nWould you like to add items, remove items, or begin shopping?")
        user_choice = input("Type add to add more items, remove to get rid \nof"
            " items, or shop to begin shopping. ")
    elif user_choice == 'remove':
        remove = input("Which item would you like to remove?")
        grocery_list.remove(remove)
        print("\nYour grocery list consists of:")
        for item in grocery_list:
            print(item) #prints grocery list in a neat way
        print("\nWould you like to add items, remove items, or begin shopping?")
        user_choice = input("Type add to add more items, remove to get rid \nof"
                    " items, or shop to begin shopping. ")
    else:
        print("Command unknown.")
        user_choice = input("Type add to add more items, remove to get rid \nof"
                    " items, or shop to begin shopping. ")
        
for item in grocery_list:#prints items one at a time and asks user to grab them
    done = 0 #sets done equal to something so while loop isn't broken
    while done != 'done':
        print("Go get:",item)
        done = input("Type done when you get the item. ")#user types done when they get the item
print("Thanks for using the Grocery List program!")#Outro
        
    




