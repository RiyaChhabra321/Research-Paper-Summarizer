#   Research Paper Summarizer

This project is a web-based tool designed to automatically summarize lengthy AI research papers or academic PDFs using GPT-4 via LangChain. It makes it easier for researchers and students to understand complex papers quickly.

## Features

- Upload research papers in PDF format
- Extracts and summarizes content intelligently
- Powered by LangChain + GPT-4
- User-friendly interface built with Streamlit
  
## Tech Stack

- **LangChain** – For prompt handling and LLM integration  
- **PyMuPDF** – To extract text from uploaded PDFs  
- **Streamlit** – For building the web app interface  
- **GPT-4** – To generate meaningful, concise summaries  



## Project Structure

- `app.py` – Main Streamlit application  
- `summarizer.py` – Contains GPT-4 summarization logic  
- `pdf_reader.py` – Extracts text from uploaded PDFs  
- `requirements.txt` – List of Python dependencies  
- `README.md` – Project overview and documentation 


## Installation

1. **Clone the repository**
   
   git clone https://github.com/your-username/research-paper-summarizer.git
   cd research-paper-summarizer
   
2. **Install required packages**

    pip install -r requirements.txt

3. **Run the application**

    streamlit run app.py

## Deployment

- Deploy it using Streamlit Cloud (recommended)
- Or any Python hosting platform like Replit / PythonAnywhere

## Team Members and Roles

1. Sanaya – Project Manager & Documentation
2. Riya – Deployment & Streamlit Engineer
3. Yashvi – Frontend Developer
4. Anjika – GPT-4 & LangChain Integrator
5. Khushboo – Backend Developer
6. Himank – Tester & Debugger


## Testing

- Upload various PDFs (long, short, complex)
- Check accuracy of summaries
- Ensure layout works on different devices


## Future Enhancements

- Add multi-language summarization
- Export summary as PDF or .txt
- Add login and save history

  ## License
  
 **This project is for educational use only.**
