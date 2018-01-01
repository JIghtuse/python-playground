movies = ['fountain', 'pi', 'mother!']
movies.append('pi')
movies[-1] = 'black swan'
movies.append('black swan')
movies.insert(0, 'protozoa')
print(movies)

del movies[0]
print(movies)

duplicate = movies.pop()
print(f"Duplicated movie: {duplicate}")

movies.insert(0, 'protozoa')
movies.remove('protozoa')
print(movies)

print(sorted(movies))
print(sorted(movies, reverse=True))
movies.sort()
print(movies)
movies.reverse()
print(movies)

print(f"There are {len(movies)} movies: {movies}")