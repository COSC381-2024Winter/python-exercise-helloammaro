from movies import Movies

def show_menu():
    print("Menu:")
    print("Enter list to list all movies")
    print("Enter search to search movies")
    print("q. Quit")

def list_all_movies(movies):
    print("Movie list:")
    for idx, movie_name in enumerate(movies.list_movie_names(), start=1):
        print(f"{idx}. {movie_name}")

def search_movies(movies, query):
    print(f"Searching for movies with '{query}':")
    results = movies.search_movies_by_name(query)
    if results:
        for movie_name in results:
            print(movie_name)
    else:
        print("No movies were found.")

def main():
    movies = Movies('./movies.txt') 

    while True:
        show_menu()
        choice = input("Choose from the following menu options: ").strip().lower()

        if choice == 'q':
            print("Exiting program.")
            break
        elif choice == 'list':
            list_all_movies(movies)
        elif choice == 'search':
            query = input("Enter a word to search movies: ").strip()
            search_movies(movies, query)
        else:
            print("Invalid option. Try again")

if __name__ == "__main__":
    main()
