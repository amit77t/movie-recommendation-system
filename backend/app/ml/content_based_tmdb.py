import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("../dataset/top10K-TMDB-movies.csv")

df = df[['title','genre','overview','popularity','vote_average']]
df['genre'] = df['genre'].fillna("")
df['overview'] = df['overview'].fillna("")

df['content'] = df['genre'] + " " + df['overview']

tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(df['content'])

cosine_sim = cosine_similarity(tfidf_matrix)


def content_recommend(movie_title, top_n=10):
    movie_title = movie_title.lower().strip()

    df['title_lower'] = df['title'].str.lower()

    # 🔹 Try partial match
    matches = df[df['title_lower'].str.contains(movie_title, na=False)]

    # 🔹 If no match found → return popular movies (fallback)
    if matches.empty:
        popular = df.sort_values(
            by=["vote_average", "popularity"],
            ascending=False
        )
        return popular.head(top_n)

    # 🔹 Use first matching movie
    idx = matches.index[0]

    scores = list(enumerate(cosine_sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    indices = [i[0] for i in scores[1:top_n+1]]
    return df.iloc[indices]




def trending_movies(top_n=10):
    return df.sort_values(
        by=['vote_average','popularity'],
        ascending=False
    ).head(top_n)
