def most_popular_genre(movies):
    max_rating = 0
    best_genre = ''
    average_rating = {}

    for movie in movies:
        genre = movie["genre"]
        rating = movie["rating"]

        if genre not in average_rating:
            average_rating[genre] = {"total": rating, "count": 1}
           
        else:
            average_rating[genre]["total"] += rating
            average_rating[genre]["count"] += 1

    for genre, stats in average_rating.items():
        avg = stats["total"] / stats["count"]
        if avg > max_rating:
            max_rating = avg
            best_genre = genre

    return best_genre

movies = [
    {"title": "Inception",
     "genre": "Science Fiction",
     "rating": 8.8
    },
    {"title": "The Matrix", 
     "genre": "Science Fiction",
     "rating": 8.7
    },
    {"title": "Pride and Prejudice", 
     "genre": "Romance",
     "rating": 7.8
    },
    {"title": "Sense and Sensibility", 
     "genre": "Romance",
     "rating": 7.7
    }
]

print(most_popular_genre(movies))