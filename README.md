# 📰 News Headlines CLI Application

A command-line news application built with Python that fetches the latest headlines from **NewsAPI**. Users can choose a news category, view the number of available articles, and decide how many headlines to display through an interactive CLI interface.

---

## 🚀 Features

- Browse news by category
- View the number of available articles before reading
- Choose how many articles to display
- Displays:
  - Title
  - Author
  - Source
  - Published Date
  - Description
  - Article URL
- Input validation for user selections
- Graceful error handling for API and network issues
- Secure API key management using environment variables (`.env`)

---

## 🛠️ Technologies Used

- Python 3
- Requests
- Python Dotenv
- REST API
- JSON

---

## 📂 Project Structure

```
News_in_python/
│
├── News_Program.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/JunaidSyed-dev/News_in_python.git
```

### 2. Navigate to the project

```bash
cd News_in_python
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure the API Key

This project uses **NewsAPI**.

Create a `.env` file in the project directory and add your API key:

```env
NEWS_API_KEY=your_api_key_here
```

You can obtain a free API key from:

https://newsapi.org/

---

## ▶️ Run the Application

```bash
python News_Program.py
```

---

## 💻 Sample Workflow

```
Available Categories

1. Business
2. Entertainment
3. General
4. Health
5. Science
6. Sports
7. Technology

Choose a category (1-7): 6

Fetching latest news...

✅ 15 article(s) available.

How many articles would you like to read? (1-15): 5
```

The application then displays the requested number of articles, including the title, author, source, publication date, description, and article URL.

---

## ⚙️ Error Handling

The application handles:

- Invalid menu selections
- Invalid number inputs
- Empty news responses
- Network connectivity issues
- API request failures

---

## 📚 What I Learned

This project helped me gain practical experience with:

- Working with REST APIs
- Sending HTTP GET requests using the `requests` library
- Parsing JSON responses
- Secure API key management using environment variables
- Building interactive command-line applications
- Input validation and exception handling
- Writing clean, modular Python code

---

## 🔮 Future Improvements

- Search news by keyword
- Support multiple countries
- Save articles to a text or CSV file
- Open articles directly in the browser
- Add a menu-driven interface
- Display publication dates in a more user-friendly format

---

## 👨‍💻 Author

**Junaid Syed**

If you found this project interesting, feel free to star ⭐ the repository.
