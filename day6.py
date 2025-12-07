fav_sports = ["powerlifting" , "football" ,"basketball" ,"swimming" ,"boxing"]
print(fav_sports)
print(fav_sports [0])
print(fav_sports [-1])
print(fav_sports [-2])
fav_sports[0] = "MMA"
fav_sports[-1] = "judo"
print(fav_sports)
fav_sports.append("kickboxing")
fav_sports.insert(3, "tennis")
print(fav_sports)
fav_sports.remove("football")
fav_sports.pop(0)
del fav_sports[-1]
print(fav_sports)
for i, sport in enumerate (fav_sports, start=1):
    print(f"{i}. {sport}")


film1 = input("what's your top 1 movie? ")
film2 = input("top 2? ")
film3 = input("top 3? ")
film4 = input("top 4? ")
film5 = input("top 5? ")
fav_movies = [film1 , film2 , film3 , film4 , film5]
print(fav_movies)
print(fav_movies[0])  
print(fav_movies[-1])
fav_movies[2] = "inception"
fav_movies.append("interstellar")
del fav_movies[1]
print(fav_movies)
print(50*"*", "here's your movies", 50*"*")
for i, movie in enumerate(fav_movies, start=1):
    print(f"Top {i}: {movie}")
print(50*"*", "Thank you", 50*"*")



playlist = ["born to die", "star shopping", "nuts", "freak", "high by the beach"]
print("🎶 Your playlist: ")
for i, song in enumerate(playlist, start=1):
    print(f"{i}. {song}")