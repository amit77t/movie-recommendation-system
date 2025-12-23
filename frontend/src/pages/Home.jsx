import { useEffect, useState } from "react";
import api from "../api/api";

function Home() {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    api.get("/movies")
      .then(res => setMovies(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div className="max-w-7xl mx-auto px-6 py-10 text-blue">
      <h1 className="text-4xl font-bold mb-8">
        🔥 Trending Movies
      </h1>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
        {movies.map((movie, index) => (
          <div
            key={index}
            className="group bg-white/5 backdrop-blur border border-white/10 rounded-xl overflow-hidden shadow-lg
                       hover:scale-105 transition duration-300"
          >
            {/* Poster placeholder */}
           <img
  src="https://images.unsplash.com/photo-1489599849927-2ee91cede3ba"
  alt={movie.title}
  className="h-60 w-full object-cover"
/>


            <div className="p-4">
              <h2 className="font-semibold text-lg group-hover:text-indigo-400 transition">
                {movie.title}
              </h2>
              <p className="text-sm text-gray-400">{movie.genre}</p>
              <p className="mt-1 text-yellow-400">
                ⭐ {movie.vote_average}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Home;
