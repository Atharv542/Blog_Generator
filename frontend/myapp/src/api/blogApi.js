import axios from "axios";

const API = "https://blog-generator-w5rl.onrender.com";

export const generateBlog = async (topic) => {
  const res = await axios.post(`${API}/generate`, {
    topic,
  });
  return res.data;
};
