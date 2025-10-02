# LLM Chatbot Project

A LangChain-based chatbot implementation using OpenAI's GPT models.

## Project Structure

```
LLM_Chatbot/
├── langchain_intro/          # Main application code
│   ├── chatbot.py           # Core chatbot functionality
│   ├── chat_interpreter.py  # Chat interpreter script
│   ├── create_retriever.py  # Document retriever setup
│   ├── tools.py            # Custom tools and utilities
│   └── Prompt_detailed.py  # Detailed prompt examples
├── data/                    # Data files (ignored by git)
├── venv/                    # Virtual environment (ignored by git)
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (ignored by git)
└── README.md               # This file
```

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
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
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

### Basic Chat
```powershell
cd langchain_intro
python chat_interpreter.py
```

### Prompt Examples
```powershell
cd langchain_intro
python Prompt_detailed.py
```

## Dependencies

- `langchain` - LangChain framework
- `openai` - OpenAI API client
- `langchain-openai` - OpenAI integration for LangChain
- `langchain-community` - Community tools and integrations
- `langchainhub` - Pre-built prompts and chains
- `python-dotenv` - Environment variable management

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

[Add your license information here]