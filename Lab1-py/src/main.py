def show_menu():
    print("=== HEADER A + B ===")
    print("1. Start")
    print("3. Exit")
    print("4. Info")

def main():
    show_menu()
    choice = input("Wybierz opcję: ")
    if choice == "1":
        print("Uruchamianie programu...")
    elif choice == "3":
        print("Do widzenia!")
    else:
        print("Nieprawidłowy wybór.")
    elif choice == "4":
        print("Wersja 1.1 – prosty system menu.")


if __name__ == "__main__":
    main()

