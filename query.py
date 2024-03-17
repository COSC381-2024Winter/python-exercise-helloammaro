from movies import Movies

movies = Movies('./movies.txt')
def show_menu():
    print("Menu:")
    print("q. Quit")

def main():
    movies = Movies('./movies.txt') 

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip().lower()

        if choice == 'q':
            print("Exiting program...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
