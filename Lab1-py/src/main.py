def show_menu():
    print("=== HEADER B ===")
    print("1. Start")
    print("2. Help")
    print("3. Exit")

def main():
    show_menu()
    choice = input("Wybierz opcję: ")
    if choice == "1":
        print("Uruchamianie programu...")
    elif choice == "2":
        print("To jest pomoc.")
    elif choice == "3":
        print("Do widzenia!")
    else:
        print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    main()

