import { useState } from "react";
import InputBox from "../components/InputBox";
import BlogPreview from "../components/BlogPreview";
import Loader from "../components/Loader";

import { generateBlog } from "../api/blogApi";

export default function Home() {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);

  const handleGenerate = async (topic) => {
    if (!topic) return;

    setLoading(true);
    setData(null);

    try {
      const res = await generateBlog(topic);
      console.log("🔥 API RESPONSE:", res);
      setData(res);
    } catch (err) {
      console.error(err);
      alert("Error generating blog");
    }

    setLoading(false);
  };

  return (
    <div className="h-screen flex bg-gray-100">

      {/* 🔥 LEFT SIDEBAR */}
      <div className="w-[350px] bg-white border-r p-6 flex flex-col justify-between">

        <div>
          <h1 className="text-2xl font-bold mb-6">
            Blog AI 🚀
          </h1>

          <InputBox onGenerate={handleGenerate} />

          {loading && <Loader />}
        </div>

      </div>

      {/* 🔥 RIGHT PREVIEW */}
      <div className="flex-1 overflow-y-auto p-8">

        {!data && !loading && (
          <div className="text-center mt-20 text-gray-400">
            <h2 className="text-2xl font-semibold">
              Your generated blog will appear here 👀
            </h2>
          </div>
        )}

        {loading && <Loader />}

        {data && <BlogPreview data={data} setData={setData}  />}
      </div>
    </div>
  );
}
