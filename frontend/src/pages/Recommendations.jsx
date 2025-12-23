import { useState } from "react";
import api from "../api/api";

function Recommendations() {
    const [movie, setMovie] = useState("");
    const [results, setResults] = useState([]);
    const [loading, setLoading] = useState(false);
    const [searched, setSearched] = useState(false);

    const getRecommendations = async () => {
        if (!movie.trim()) return;

        setLoading(true);
        setSearched(true);

        try {
            const cleanMovie = encodeURIComponent(movie.trim());
            const res = await api.get(`/recommend/${cleanMovie}`);
            setResults(Array.isArray(res.data) ? res.data : []);
        } catch {
            setResults([]);
        }

        setLoading(false);
    };

    return (
        <div className="max-w-7xl mx-auto px-6 py-14 text-blue">
            <div className="text-center mb-10">
                <h1 className="text-5xl font-extrabold mb-3 bg-gradient-to-r from-indigo-400 to-pink-500 bg-clip-text text-transparent">
                    AI Movie Recommendations
                </h1>
                <p className="text-gray-400">
                    Discover movies powered by Machine Learning 🤖
                </p>
            </div>

            {/* Search */}
            <div className="flex justify-center gap-3 mb-10">
                <input
                    value={movie}
                    onChange={(e) => setMovie(e.target.value)}
                    placeholder="Type a movie name..."
                    className="w-72 px-4 py-3 rounded-lg bg-white-300 border border-blue/20
                     focus:outline-none focus:ring-2 focus:ring-indigo-500"
                />
                <button
                    onClick={getRecommendations}
                    className="px-6 py-3 rounded-lg bg-indigo-600 hover:bg-indigo-700 transition"
                >
                    Recommend
                </button>
            </div>

            {loading && (
                <p className="text-center text-indigo-400 animate-pulse">
                    AI is thinking...
                </p>
            )}

            {/* Results */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-6 mt-10">
                {results.map((m, index) => (
                    <div
                        key={index}
                        className="bg-white/5 backdrop-blur border border-white/10 rounded-xl
                       hover:scale-105 transition duration-300"
                    >
                        <img
                            src="https://images.unsplash.com/photo-1489599849927-2ee91cede3ba"
                            alt={m.title}
                            className="h-52 w-full object-cover"
                        />

                        <div className="p-4">
                            <h2 className="font-semibold">{m.title}</h2>
                            <p className="text-sm text-gray-400">{m.genre}</p>
                            <p className="text-yellow-400 mt-1">⭐ {m.vote_average}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Recommendations;
