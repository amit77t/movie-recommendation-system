import { useState } from "react";
import api from "../api/api";
import { useNavigate } from "react-router-dom";

function Register() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post("/auth/register", form);
      navigate("/login");
    } catch {
      alert("Registration failed");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-black via-slate-900 to-purple-900">
      <form
        onSubmit={handleSubmit}
        className="w-96 p-8 rounded-2xl bg-white/10 backdrop-blur-lg border border-white/20 shadow-xl animate-fadeIn"
      >
        <h2 className="text-3xl font-bold text-white mb-6 text-center">
          Create Account 🚀
        </h2>

        <input
          name="name"
          placeholder="Name"
          className="w-full mb-4 px-4 py-3 rounded bg-black/40 text-white border border-white/20"
          onChange={handleChange}
        />

        <input
          name="email"
          placeholder="Email"
          className="w-full mb-4 px-4 py-3 rounded bg-black/40 text-white border border-white/20"
          onChange={handleChange}
        />

        <input
          name="password"
          type="password"
          placeholder="Password"
          className="w-full mb-6 px-4 py-3 rounded bg-black/40 text-white border border-white/20"
          onChange={handleChange}
        />

        <button className="w-full py-3 rounded bg-purple-600 hover:bg-purple-700 transition text-white font-semibold">
          Register
        </button>
      </form>
    </div>
  );
}

export default Register;
