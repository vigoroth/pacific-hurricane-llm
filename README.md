### Pacific Hurricane Data Extractor
This project utilizes Large Language Models (LLMs), web scraping, and vector databases to extract structured information about hurricanes from HTML content.

#Project Overview

The project:
- Scrapes HTML data using BeautifulSoup.
- Creates embeddings using OpenAI's text-embedding-3-small model.
- Stores embeddings in a Chroma vector database.
- Queries the vector database using semantic similarity.
- Uses GPT-4o to generate structured responses to specific queries.

#Installation

#Clone Repository

```bash
git clone https://github.com/your-username/pacific-hurricane-llm
cd pacific-hurricane-llm
```

#Setup Environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#API Keys

```bash
Create a <mark>.env</mark> file in the root directory:
```

#Directory Structure

```bash
pacific-hurricane-llm/
├── db/
│   └── chroma_db/
├── html/
│   └── test.txt
├── output/
│   └── hurricanes_1975-gpt-04.txt
├── src/
│   ├── scraper.py
│   ├── embedding_store.py
│   ├── query_llm.py
│   └── utils.py
├── .env
├── requirements.txt
└── README.md
```

#Requirements

<mark>requirements.txt</mark>

```bash
langchain
langchain-community
langchain-openai
beautifulsoup4
chromadb
python-dotenv
pandas
```

#Running the Project

##Step 1: Prepare HTML data

Place your HTML data inside <mark>html/test.txt</mark> .

#Step 2: Initialize the Vector Store

Run:

```bash
python src/embedding_store.py
```

##Step 3: Query LLM for Data Extraction

Run:

```bash
python src/query_llm.py
```
The extracted data will be saved in:

```bash
output/hurricanes_1975-gpt-04.txt
```


#Customization

Adjust your queries in query_llm.py to extract different types of data.

#Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss your proposal.

License

MIT

