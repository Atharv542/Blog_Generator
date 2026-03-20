import axios from "axios";

const API = "http://127.0.0.1:8000";

export const generateBlog = async (topic) => {
  const res = await axios.post(`${API}/generate`, {
    topic,
  });
  return res.data;
};