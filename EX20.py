list = []

while True:
    choice = input("add / remove / show / quit ")

    if choice == "add":
        item = input("Enter item: ")
        list.append(item)
        print("Item added")

    elif choice == "remove":
        item = input("Enter item to remove: ")
        list.remove(item)
        print("Item removed")

    elif choice == "show":
        print("Shopping list:", list)

    elif choice == "quit":
        
        break

    else:
        print("Invalid choice")
