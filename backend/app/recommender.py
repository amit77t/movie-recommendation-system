from app.ml.content_based_tmdb import content_recommend


def recommend_movie(movie_title):
    return content_recommend(movie_title).head(10)
