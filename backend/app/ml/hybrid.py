def hybrid_recommend(user_id, movie_title):
    content = content_recommend(movie_title)
    content['score'] = 0.7

    return content.head(10)
