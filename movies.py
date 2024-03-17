class Movies:
    def __init__(self, movies_file):
        self._movies = []
        with open(movies_file, encoding="utf-8") as file:
            row_idx = 0
            for line in file:
                if row_idx % 3 == 0:
                    movie_name = line.rstrip()
                if row_idx % 3 == 1:
                    movie_cast = line.rstrip().split(',')
                if row_idx % 3 == 2:
                    self._movies.append(
                        {
                            'name': movie_name,
                            'cast': movie_cast
                        }
                    )
                    movie_name = None
                    movie_cast = None
                row_idx += 1

        if movie_name and movie_cast:
            self._movies.append(
                {
                    'name': movie_name,
                    'cast': movie_cast
                }
            )

    def list_movie_names(self):
        return [movie['name'] for movie in self._movies]

    def search_movies_by_name(self, keyword):
        keyword = keyword.lower()
        results = [movie['name'] for movie in self._movies if keyword in movie['name'].lower()]
        return results

if __name__ == "__main__":
    movies = Movies('./movies.txt')
    for idx, name in enumerate(movies.list_movie_names(), start=1):
        print(f"{idx}. {name}")
    print(movies.search_movies_by_name('keyword'))
