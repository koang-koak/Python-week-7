# 1. Start with an empty list
shopping_list = []

# 2. Use a loop to show a small menu again and again
while True:
    action = input("\nChoose an action (add / remove / show / done): ").strip().lower()
    
    if action == "add":
        item = input("Enter item to add: ").strip()
        shopping_list.append(item)
        print(f"'{item}' added to the shopping list.")
        
    elif action == "remove":
        item = input("Enter item to remove: ").strip()
        # Check membership with 'in' before removing to avoid crashing
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from the shopping list.")
        else:
            print("That item is not on your list.")
            
    elif action == "show":
        if shopping_list:
            print("\nYour Shopping List:")
            for item in shopping_list:
                print(f"- {item}")
        else:
            print("Your shopping list is currently empty.")
            
    elif action == "done":
        print("Goodbye! Thank you for using Shopping List Manager.")
        break
        
    else:
        print("Invalid choice. Please choose add, remove, show, or done.")