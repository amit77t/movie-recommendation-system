import { useState } from "react";
import api from "../api/api";
import { useNavigate } from "react-router-dom";

function Login() {
  const [form, setForm] = useState({ email: "", password: "" });
  const navigate = useNavigate();

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post("/auth/login", form);
      localStorage.setItem("token", res.data.token);
      navigate("/");
    } catch {
      alert("Invalid credentials");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-black via-slate-900 to-purple-900">
      <form
        onSubmit={handleSubmit}
        className="w-96 p-8 rounded-2xl bg-white/10 backdrop-blur-lg border border-white/20 shadow-xl animate-fadeIn"
      >
        <h2 className="text-3xl font-bold text-white mb-6 text-center">
          Welcome Back 👋
        </h2>

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={form.email}
          onChange={handleChange}
          className="w-full mb-4 px-4 py-3 rounded bg-black/40 text-white border border-white/20 focus:outline-none focus:ring-2 focus:ring-purple-600"
          required
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={form.password}
          onChange={handleChange}
          className="w-full mb-6 px-4 py-3 rounded bg-black/40 text-white border border-white/20 focus:outline-none focus:ring-2 focus:ring-purple-600"
          required
        />

        <button
          type="submit"
          className="w-full py-3 rounded bg-purple-600 hover:bg-purple-700 transition text-white font-semibold"
        >
          Login
        </button>
      </form>
    </div>
  );
}

export default Login;
