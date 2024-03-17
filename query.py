from movies import Movies

def show_menu():
    print("Menu:")
    print("Enter list to list all movies")
    print("Enter search to search movies by name")
    print("Enter cast to search movies by cast")
    print("q. Quit")

def list_all_movies(movies):
    print("Movie list:")
    for idx, movie_name in enumerate(movies.list_movie_names(), start=1):
        print(f"{idx}. {movie_name}")

def search_movies_by_name(movies, query):
    print(f"Searching for movies with '{query}' in the name:")
    results = movies.search_movies_by_name(query)
    if results:
        for movie_name in results:
            print(movie_name)
    else:
        print("No movies were found.")

def search_movies_by_cast(movies, query):
    print(f"Searching for movies with '{query}' in the cast:")
    results = movies.search_movies_by_cast(query)
    if results:
        for movie_name, cast in results:
            print(f"{movie_name}: {', '.join(cast)}")
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
            query = input("Enter a word to search movies by name: ").strip()
            search_movies_by_name(movies, query)
        elif choice == 'cast':
            query = input("Enter a word to search movies by cast: ").strip()
            search_movies_by_cast(movies, query)
        else:
            print("Invalid option. Try again")

if __name__ == "__main__":
    main()
