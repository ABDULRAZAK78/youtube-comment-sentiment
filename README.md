# 💬 YouTube Comment Sentiment Analysis — AI Powered

<div align="center">

![YouTube Sentiment Banner](https://via.placeholder.com/900x200/FF0000/ffffff?text=YouTube+Comment+Sentiment+Analysis)

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![AI](https://img.shields.io/badge/AI-Groq%20LLM-F55036?style=for-the-badge)](https://groq.com/)
[![YouTube](https://img.shields.io/badge/YouTube-API-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://developers.google.com/youtube)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

**Scrape YouTube comments and analyze sentiment using the power of AI & LLM.**

</div>

---

## 📌 Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Author](#author)
- [License](#license)

---

## 📖 About

YouTube Comment Sentiment Analysis is an AI-powered Python application that scrapes comments from any YouTube video and uses a **Large Language Model (LLM) via Groq** to perform deep sentiment analysis — classifying comments as positive, negative, or neutral with intelligent AI insights beyond basic keyword matching.

---

## ✨ Features

- 🎯 **YouTube Comment Scraping** — Automatically fetches comments from any YouTube video URL
- 🤖 **AI-Powered Sentiment Analysis** — Uses Groq LLM for intelligent, context-aware analysis
- 📊 **Sentiment Classification** — Positive, Negative, and Neutral categorization
- 📁 **CSV Export** — Save scraped comments and results to CSV
- 🖥️ **Interactive UI** — Clean web interface built with Streamlit
- ⚡ **Fast Processing** — Groq's ultra-fast LLM inference

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.x |
| AI / LLM | Groq API |
| Scraping | YouTube Data API |
| Frontend | Streamlit |
| Data | Pandas, CSV |

---

## 📁 Project Structure

```
youtube-comment-sentiment/
├── app.py                        # Main Streamlit application
├── Senti.py                      # Sentiment analysis logic
├── YoutubeCommentScrapper.py     # YouTube comment scraper
├── requirements.txt              # Python dependencies
├── LOGO.png                      # App logo
└── VNVkz_I-O9Y.csv              # Sample scraped comments CSV
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Groq API Key → [console.groq.com](https://console.groq.com)
- YouTube Data API Key → [console.cloud.google.com](https://console.cloud.google.com)

---

### Installation

```bash
# Clone the repo
git clone https://github.com/Abdul-razak98/youtube-comment-sentiment.git
cd youtube-comment-sentiment

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

### Configuration

Open `app.py` and add your API keys:

```python
GROQ_API_KEY = "your_groq_api_key_here"
YOUTUBE_API_KEY = "your_youtube_api_key_here"
```

---

### Run the App

```bash
streamlit run app.py
# Opens at http://localhost:8501
```

---

## 👨‍💻 Author

**Abdul Razak**

[![GitHub](https://img.shields.io/badge/GitHub-Abdul--razak98-181717?style=flat&logo=github)](https://github.com/Abdul-razak98)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-abdulrazak27-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/abdulrazak27/)
[![Instagram](https://img.shields.io/badge/Instagram-abdulrazak27__-E4405F?style=flat&logo=instagram)](https://www.instagram.com/abdulrazak27_/)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">
  Made with ❤️ by Abdul Razak
</div>
