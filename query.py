from movies import Movies

def show_menu():
    print("Menu:")
    print("Enter list to list all movies")
    print("q. Quit")

def list_all_movies(movies):
    print("Movie list:")
    for idx, movie_name in enumerate(movies.list_movie_names(), start=1):
        print(f"{idx}. {movie_name}")

def main():
    movies = Movies('./movies.txt') 

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip().lower()

        if choice == 'q':
            print("Exiting program...")
            break
        elif choice == 'list':
            list_all_movies(movies)
        else:
            print("Invalid option. Enter again")

if __name__ == "__main__":
    main()
