from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from newspaper import Article
from newspaper import ArticleException
from urllib.parse import urlparse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Allow requests from the frontend URL
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://article-checker-0suq.onrender.com"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Example database of trusted/untrusted sources
SOURCE_CREDIBILITY = {
    "bbc.com": {"score": 95, "bias": "Center"},
    "cnn.com": {"score": 80, "bias": "Left"},
    "foxnews.com": {"score": 75, "bias": "Right"},
    "infowars.com": {"score": 20, "bias": "Conspiracy"},
}

# Utility function to extract domain from URL
def get_domain(url: str) -> str:
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.replace("www.", "")
        if not domain:
            raise HTTPException(status_code=400, detail="Invalid URL format")
        return domain
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid URL format")


# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Article Credibility API!"}

# Request model for article URL
class ArticleRequest(BaseModel):
    url: str

# Endpoint to check article credibility
@app.post("/check")
def check_article(request: ArticleRequest):
    try:
        # Download and parse the article
        article = Article(request.url)
        article.download()
        article.parse()

        # Use the utility function to extract domain name and check credibility
        domain = get_domain(request.url)
        credibility = SOURCE_CREDIBILITY.get(domain, {"score": 50, "bias": "Unknown"})

        # Preview the first 500 characters of the article
        preview_text = article.text if len(article.text) < 500 else article.text[:500]

        return {
            "source": domain,
            "score": credibility["score"],
            "bias": credibility["bias"],
            "text": preview_text,
        }
    except ArticleException:
        raise HTTPException(status_code=400, detail="Failed to parse article")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")
