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

2. Set up a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r backend/requirements.txt

3. Run the backend server:
uvicorn backend:app --reload

The server will start running at http://127.0.0.1:8000.

### Frontend Setup
1. Navigate to the frontend directory:
cd frontend

2. Install the required npm packages:
npm install

3. Start the frontend server:
npm start

The frontend will be running at http://localhost:3000.

## Usage
1. Open your browser and go to http://localhost:3000.
2. Enter an article URL in the input box and click the "Check" button.
3. The application will display the credibility score, political bias, and a preview of the article.

## Contributing
Feel free to fork the repository, make changes, and create pull requests. Please follow these steps:

## Fork the repository.
Create a new branch (git checkout -b feature-name).
Make your changes and commit them (git commit -am 'Add feature').
Push to your branch (git push origin feature-name).
Create a new pull request.

If you encounter any issues or have questions, feel free to open an issue on GitHub or contact me directly.
