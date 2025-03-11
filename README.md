# Article Credibility Checker

This project is a web application that checks the credibility of an article's source. The backend is powered by **FastAPI** and **Newspaper3k** for article scraping and parsing, while the frontend is built with **React**.

## Features

- Check the credibility of articles by providing a URL.
- Preview the first 500 characters of the article.
- Return the source credibility score and political bias.
- FastAPI backend with CORS enabled to interact with the frontend.
- React frontend for user-friendly interaction.

## Technologies Used

### Backend:
- **FastAPI**: For building the API.
- **Newspaper3k**: For scraping and parsing articles.
- **CORS Middleware**: To allow requests from the frontend.
  
### Frontend:
- **React**: For building the interactive frontend.

### Database:
- **In-memory database (SOURCE_CREDIBILITY)**: A mock database for storing the credibility score and bias of various sources.

## Installation

### Prerequisites

- Python 3.7 or higher
- Node.js and npm
- Git

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/article-checker.git
   cd article-checker
