import { useState } from "react";

export default function ArticleChecker() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const checkArticle = async () => {
    setLoading(true);
    setResult(null);
    try {
      const response = await fetch("http://127.0.0.1:8000/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Error checking article:", error);
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Article Credibility Checker</h1>
      <input
        type="text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter article URL"
      />
      <button onClick={checkArticle} disabled={loading}>
        {loading ? "Checking..." : "Check Article"}
      </button>
      {result && (
        <div>
          <h2>Results:</h2>
          <p><strong>Source:</strong> {result.source}</p>
          <p><strong>Credibility Score:</strong> {result.score}</p>
          <p><strong>Bias:</strong> {result.bias}</p>
          <p><strong>Article Preview:</strong> {result.text}</p>
        </div>
      )}
    </div>
  );
}
