import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="sticky top-0 z-50 backdrop-blur bg-black/40 border-b border-white/10">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
        
        <h1 className="text-2xl font-extrabold text-white tracking-wide">
          🎬 MovieAI
        </h1>

        <div className="flex space-x-10 text-gray-300 font-medium">
          <Link className="hover:text-white transition" to="/">Home</Link>
          <Link className="hover:text-white transition" to="/recommend">AI Recommend</Link>
          <Link className="hover:text-white transition" to="/login">Login</Link>
          <Link className="hover:text-white transition" to="/register">Register</Link>
        </div>

      </div>
    </nav>
  );
}

export default Navbar;
