import { useState } from "react";
export default function InputBox({ onGenerate }) {
  const [topic, setTopic] = useState("");

  return (
    <div className="flex flex-col gap-4">
      <input
        type="text"
        placeholder="e.g. AI in Healthcare"
        className="p-3 rounded-lg border focus:outline-none focus:ring-2 focus:ring-black"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />

      <button
        onClick={() => onGenerate(topic)}
        className="bg-black text-white p-3 rounded-lg hover:opacity-80"
      >
        Generate 🚀
      </button>
    </div>
  );
}