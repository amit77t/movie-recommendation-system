from app.ml.content_based_tmdb import content_recommend


def recommend_movie(movie_title: str):
    """
    Calls ML recommender and converts output to JSON-safe format.
    """
    df = content_recommend(movie_title)
    return df.to_dict(orient="records")
