# LLM Chatbot Project

A LangChain-based chatbot implementation using OpenAI's GPT models for analyzing hospital patient reviews and answering healthcare-related questions.

## Project Structure

```
LLM_Chatbot/
├── langchain_intro/          # Main application code
│   ├── chatbot.py           # Core chatbot functionality with prompts
│   ├── chatbot_runner.py    # Main script to run the chatbot
│   ├── create_retriever.py  # Creates vector database from CSV data
│   ├── tools.py            # Custom tools and utilities
│   └── chroma_data/        # Vector database storage (auto-generated)
├── data/                    # Data files
│   └── reviews.csv         # Hospital patient reviews dataset
├── venv/                    # Virtual environment (ignored by git)
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (ignored by git)
├── .env.example            # Template for environment variables
└── README.md               # This file
```

## Features

- **Healthcare-focused chatbot** that answers questions about hospital experiences
- **Vector-based retrieval** using ChromaDB for contextual responses
- **Patient review analysis** from CSV data
- **Prompt engineering** with system and human message templates
- **OpenAI GPT integration** for intelligent responses

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Abhinav-SU/Langchain-chatbot.git
   cd LLM_Chatbot
   ```

2. **Create and activate virtual environment**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key to `.env`:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. **Create vector database (first time only)**
   ```powershell
   cd langchain_intro
   python create_retriever.py
   ```

## Usage

### Run the Chatbot
```powershell
cd langchain_intro
python chatbot_runner.py
```

### Create/Update Vector Database
```powershell
cd langchain_intro
python create_retriever.py
```

## Dependencies

- `langchain>=0.1.0` - LangChain framework for LLM applications
- `openai>=1.7.2` - OpenAI API client
- `langchain-openai>=0.0.2` - OpenAI integration for LangChain
- `langchain-community>=0.0.12` - Community tools and document loaders
- `langchainhub>=0.1.14` - Pre-built prompts and chains
- `python-dotenv>=1.0.0` - Environment variable management
- `chromadb` - Vector database for embeddings storage

## How It Works

1. **Data Loading**: CSV file with patient reviews is loaded using LangChain's CSVLoader
2. **Embeddings**: Reviews are converted to vector embeddings using OpenAI's embedding models
3. **Storage**: Embeddings are stored in ChromaDB for fast similarity search
4. **Query Processing**: User questions are processed through carefully crafted prompts
5. **Retrieval**: Relevant reviews are retrieved based on semantic similarity
6. **Response**: GPT model generates responses using retrieved context

## Project Components

### Core Files
- `chatbot.py` - Contains prompt templates and chatbot chain setup
- `chatbot_runner.py` - Main execution script for running the chatbot
- `create_retriever.py` - Sets up vector database from review data

### Data
- `data/reviews.csv` - Hospital patient reviews with columns: review_id, visit_id, review, physician_name, hospital_name, patient_name
- `chroma_data/` - Auto-generated vector database files (not tracked in git)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is open source and available under the MIT License.