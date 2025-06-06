tasks = []

def show_menu():
    print("\n1. Lägg till uppgift")
    print("2. Visa uppgifter")
    print("3. Avsluta")

while True:
    show_menu()
    choice = input("Välj: ")
    
    if choice == "1":
        task = input("Skriv uppgift: ")
        tasks.append(task)
    elif choice == "2":
        print("\nDina uppgifter:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == "3":
        print("Hej då!")
        break
    else:
        print("Ogiltigt val.")
