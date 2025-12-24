import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import os
# Lazy-loaded globals
df = None
tfidf = None
cosine_sim = None


def load_ml():
    """
    Load dataset and ML objects only once (lazy loading).
    Prevents high memory usage during server startup.
    """
    global df, tfidf, cosine_sim

    if df is None:
        print("📥 Loading ML dataset and model...")

        # df = pd.read_csv("dataset/top10K-TMDB-movies.csv")
         

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        DATASET_PATH = os.path.join(BASE_DIR, "dataset", "top10K-TMDB-movies.csv")

        df = pd.read_csv(DATASET_PATH)

        # Combine text features
        df["combined"] = (
            df["title"].fillna("") + " " +
            df["genre"].fillna("") + " " +
            df["overview"].fillna("")
        )

        tfidf = TfidfVectorizer(stop_words="english")
        tfidf_matrix = tfidf.fit_transform(df["combined"])

        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

        print("✅ ML loaded successfully")


def content_recommend(title: str):
    load_ml()  # 👈 LAZY LOAD HERE

    title = title.lower()
    df["title_lower"] = df["title"].str.lower()

    # Cold start fallback
    if title not in df["title_lower"].values:
        return df.sort_values("vote_average", ascending=False).head(10)

    idx = df[df["title_lower"] == title].index[0]

    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:11]

    movie_indices = [i[0] for i in similarity_scores]

    return df.iloc[movie_indices][["title", "genre", "vote_average"]]
