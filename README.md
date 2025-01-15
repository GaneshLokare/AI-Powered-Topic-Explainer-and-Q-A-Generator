# AI-Powered Topic Explainer and Q&A Generator

An interactive web application that generates explanations and Q&A pairs for any given topic using AI. The application features a user-friendly interface built with Gradio and leverages language models to provide comprehensive topic explanations and both basic and practical interview questions.

## Features

### 1. Topic Explanation
- Generates detailed explanations for any given topic
- User-friendly interface with example topics
- Interactive text input with instant results

### 2. Basic Q&A Generation
- Creates fundamental question and answer pairs
- Presents results in an organized table format
- Allows downloading Q&A pairs as CSV
- Includes common example topics

### 3. Practical Q&A Generation
- Generates practical, application-focused questions and answers
- Presents results in an organized table format
- Allows downloading Q&A pairs as CSV
- Provides real-world example topics

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment:
```bash
python -m venv qaenv
source qaenv/bin/activate  # On Windows: qaenv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install gradio pandas python-dotenv langchain langchain-openai
```

## Project Structure

```
project/
├── src/
│   ├── __init__.py
│   ├── basic_qa_generate.py
│   ├── practical_qa_generate.py
│   └── explanation.py
├── app.py
└── README.md
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to the provided local URL (typically http://127.0.0.1:7860)

3. Choose from three main features:
   - **Explanation**: Get detailed explanations of any topic
   - **Basic Q&A**: Generate fundamental question-answer pairs
   - **Practical Q&A**: Generate practical interview questions

4. Enter your desired topic and click the corresponding button to generate content

5. Download results as CSV files for future reference

## Example Topics
- Artificial Intelligence
- Python Programming
- Data Structures
- Machine Learning

## Environment Variables

Create a `.env` file in the project root directory with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Technical Details

- **Frontend**: Gradio (Web Interface)
- **Backend**: Python
- **AI Integration**: LangChain with OpenAI
- **Data Processing**: Pandas
- **File Handling**: Temporary file storage for CSV exports
