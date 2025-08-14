def recommend_books(preferred_genre):
    books = [
        {"title": "Dune", "genre": "science fiction"},
        {"title": "Pride and Prejudice", "genre": "romance"},
        {"title": "The Hobbit", "genre": "fantasy"},
        {"title": "The Da Vinci Code", "genre": "mystery"},
        {"title": "To Kill a Mockingbird", "genre": "classic"},
    ]
    recommendations = [book["title"] for book in books if book["genre"].lower() == preferred_genre.lower()]
    if recommendations:
        print(f"Recommended books in '{preferred_genre}' genre:")
        for title in recommendations:
            print("-", title)
    else:
        print(f"No recommendations found for genre: {preferred_genre}")

# Example usage:
recommend_books("classic")
recommend_books("mystery")
