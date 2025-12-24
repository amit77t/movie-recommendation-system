import axios from "axios";

const api = axios.create({
  baseURL: "https://movie-recommendation-system-6gt8.onrender.com",
});

export default api;
