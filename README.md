# 🎬 AI-Driven Movie Recommendation System

An end-to-end **AI-powered movie recommendation system** built using **FastAPI, React, and Machine Learning**.  
The system provides **personalized movie recommendations** using **Content-Based Filtering** with TF-IDF and Cosine Similarity, deployed on modern cloud platforms.

---

## 🚀 Live Demo

- **Frontend (Vercel):**  
  https://movie-recommendation-system-six-tawny.vercel.app/

- **Backend API (Render):**  
  https://movie-recommendation-system-6gt8.onrender.com/docs

---

## 🧠 Key Features

- 🔐 JWT-based Authentication (Login & Register)
- 🎥 Browse top movies from TMDB dataset
- ⭐ Movie rating system
- 🤖 AI-powered movie recommendations
- 🧊 Cold-start handling (popular movies)
- ⏳ Lazy-loaded ML model (memory efficient)
- 🌐 Fully deployed (Frontend + Backend)
- 📱 Responsive UI (Desktop & Mobile)

---

## 🏗️ Tech Stack

### Frontend
- React.js (Vite)
- Tailwind CSS
- Axios
- React Router
- Deployed on **Vercel**

### Backend
- FastAPI
- REST APIs
- JWT Authentication
- MongoDB (users & history)
- Deployed on **Render**

### Machine Learning
- Python
- Pandas, NumPy
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- Lazy model loading for production

---

## 📊 Dataset

- **Top 10K TMDB Movies Dataset**
- Fields:
  - title
  - genre
  - overview
  - popularity
  - vote_average
  - vote_count

---

## 🤖 How Recommendation Works

1. Movie overviews are converted into **TF-IDF vectors**
2. **Cosine Similarity** finds similar movies
3. Top-N similar movies are returned
4. Model loads only when `/recommend` endpoint is called (lazy loading)

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|------|---------|-------------|
| POST | `/auth/register` | Register user |
| POST | `/auth/login` | Login user |
| GET | `/movies` | Get movies |
| GET | `/recommend/{movie}` | Get AI recommendations |
| POST | `/rate-movie` | Rate movie |
| GET | `/user/history` | Watch history |

---




## 🔐 Environment Variables

Backend uses environment variables for security.


MONGO_URI=your_mongodb_uri
SECRET_KEY=your_secret_key

---

## 🚀 Deployment

- Backend deployed on **Render**
- Frontend deployed on **Vercel**
- CORS configured for cross-domain access
- Optimized for free-tier hosting (single worker, lazy ML load)

---

## 🧪 Challenges Solved

- Cold-start latency on ML endpoints
- CORS issues between Vercel & Render
- Dataset path resolution in production
- Memory optimization for ML models

---

## 📌 Future Enhancements

- Collaborative Filtering
- Hybrid Recommendation System
- Movie posters using TMDB API
- User-specific recommendations
- Admin dashboard

---

## 👨‍💻 Author

**Amit Chaurasia**  
B.Tech | Full-Stack & AI Enthusiast


