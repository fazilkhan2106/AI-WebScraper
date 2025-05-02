# AI Web Scraper

## 📖 Definition

The **AI Web Scraper** is an intelligent web scraping tool built with Python that allows users to automatically scrape, clean, and extract specific information from websites using advanced language models. It combines the power of Selenium, BeautifulSoup, LangChain, and Ollama to turn raw website content into meaningful, structured data, helping automate data extraction tasks efficiently.

## ✨ Features

- Automatic scraping of web pages  
- Extraction of clean, readable text from HTML  
- AI-driven parsing of specific user-defined information  
- User-friendly interface using Streamlit  
- Supports dynamic web pages with Selenium  
- Expandable sections to view raw and parsed data

## ⚙️ Technologies Used

- Python  
- Streamlit (frontend)  
- Selenium (for dynamic page scraping)  
- BeautifulSoup (for HTML parsing)  
- LangChain  
- Ollama LLM (deepseek, llama3.1)

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-web-scraper.git
   cd ai-web-scraper

2.Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt

🛠️ Dependencies
streamlit

selenium

beautifulsoup4

langchain

langchain_ollama

chromedriver-autoinstaller (optional, if using)

🖥️ ChromeDriver
Download the ChromeDriver matching your Chrome browser version:
https://chromedriver.chromium.org/downloads
Place chromedriver.exe in the project root directory.

🚀 How to Run
Ensure you are in the project directory.

Run the Streamlit app:

bash
Copy
Edit
streamlit run main.py
Open the provided local URL in your browser.

💡 How It Works
Enter the website URL in the input box.

Click Scrape Site to extract and clean the website content.

View the cleaned DOM content in the expandable section.

Enter a description of the data you want to extract.

Click Parse Content to get results from the AI model.

📂 Project Structure
graphql
Copy
Edit
├── main.py            # Streamlit frontend  
├── scrape.py          # Web scraping and cleaning functions  
├── parse.py           # AI parsing with LangChain + Ollama  
├── requirements.txt   # Project dependencies  
├── chromedriver.exe   # Selenium driver (ensure it matches your browser)

🙌 Credit
Techwithtim

📄 License
This project is licensed under the MIT License.
See the LICENSE file for more details.
