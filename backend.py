from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from newspaper import Article

app = FastAPI()

# Example database of trusted/untrusted sources
SOURCE_CREDIBILITY = {
    "bbc.com": {"score": 95, "bias": "Center"},
    "cnn.com": {"score": 80, "bias": "Left"},
    "foxnews.com": {"score": 75, "bias": "Right"},
    "infowars.com": {"score": 20, "bias": "Conspiracy"},
}

class ArticleRequest(BaseModel):
    url: str

@app.post("/check")
def check_article(request: ArticleRequest):
    try:
        article = Article(request.url)
        article.download()
        article.parse()

        # Extract domain name
        domain = request.url.split("/")[2].replace("www.", "")
        credibility = SOURCE_CREDIBILITY.get(domain, {"score": 50, "bias": "Unknown"})

        return {
            "source": domain,
            "score": credibility["score"],
            "bias": credibility["bias"],
            "text": article.text[:500],  # Preview of article text
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
