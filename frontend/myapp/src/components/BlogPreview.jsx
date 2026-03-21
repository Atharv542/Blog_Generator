import { useState } from "react";

export default function BlogPreview({ data, setData }) {
  const [selectedText, setSelectedText] = useState("");
  const [loadingEdit, setLoadingEdit] = useState(false);

  if (!data) return null;

  // 🔥 Capture selected text
  const handleSelection = () => {
    const selection = window.getSelection().toString();
    setSelectedText(selection);
  };

  // 🔥 Replace text in HTML
  const replaceText = (oldText, newText) => {
    const updatedHTML = data.content_html.replace(oldText, newText);

    setData({
      ...data,
      content_html: updatedHTML,
    });
  };

  // 🔥 Call AI editor
  const handleEdit = async (instruction) => {
    if (!selectedText) {
      alert("Please select text first!");
      return;
    }

    setLoadingEdit(true);

    try {
      const res = await fetch("https://blog-generator-w5rl.onrender.com/edit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: selectedText,
          instruction,
        }),
      });

      const result = await res.json();

      replaceText(selectedText, result.edited_text);

    } catch (err) {
      console.error(err);
    }

    setLoadingEdit(false);
    setSelectedText("");
  };

  return (
    <div className="w-full max-w-6xl mx-auto px-6">

      {/* HERO */}
      <div className="mb-10">
        <h1 className="text-5xl font-bold mb-4">
          {data?.title}
        </h1>
        <p className="text-gray-500 text-lg">
          {data?.meta_description}
        </p>
      </div>

      {/* 🔥 AI EDIT TOOLBAR */}
      {selectedText && (
        <div className="mb-4 flex flex-wrap gap-3 bg-gray-100 p-3 rounded-lg shadow">
          <span className="text-sm text-gray-600">
            Selected: "{selectedText.slice(0, 50)}..."
          </span>

          <button
            onClick={() => handleEdit("Make it simpler")}
            className="bg-black text-white px-3 py-1 rounded"
          >
            ✨ Simpler
          </button>

          <button
            onClick={() => handleEdit("Make it more engaging")}
            className="bg-purple-600 text-white px-3 py-1 rounded"
          >
            🚀 Engaging
          </button>

          <button
            onClick={() => handleEdit("Add examples")}
            className="bg-green-600 text-white px-3 py-1 rounded"
          >
            📚 Examples
          </button>

          {loadingEdit && (
            <span className="text-sm text-gray-500 animate-pulse">
              Editing...
            </span>
          )}
        </div>
      )}

      {/* 🔥 BLOG CONTENT (Selectable) */}
      <div
        onMouseUp={handleSelection}
        className="prose prose-slate lg:prose-xl max-w-none mb-10 cursor-text"
      >
        <div
          dangerouslySetInnerHTML={{
            __html: data?.content_html || "<p>No content</p>"
          }}
        />
      </div>

      {/* 🔥 WEBSITE PREVIEW
      <h2 className="text-2xl font-bold mb-4">
        🌐 Live Website Preview
      </h2>

      <iframe
        srcDoc={data?.preview_html}
        className="w-full h-[700px] border rounded-xl shadow-lg bg-white"
      /> */}
    </div>
  );
}
