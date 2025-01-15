from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI


class BasicGenerateQA:
    def __init__(self):
        load_dotenv()
        # Create a ChatOpenAI model
        model = ChatOpenAI(model="gpt-4o-mini", response_format={ "type": "json_object" })

        # Define prompt templates (no need for separate Runnable chains)
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "You are an advanced AI assistant specialized in generating interview questions and answers on given topic."),
                ("human", """ As an expert in interview preparation, your task is to: 
                 
generate well-crafted interview questions and answers based on the provided topic.
Develop a comprehensive set of Q&A pairs that cover both main and subtopics relevant to the given subject.
Ensure a balanced mix of question types, basics, intermediate, advanced and Practical/Scenario-Based Questions. 
Each question must have a corresponding, accurate answer that provides clear, concise information.
Be thorough yet concise, focusing on delivering impactful questions and answers that are informative and relevant to the topic at hand.
    
Guidelines: 
    
Each Q&A pair must have exactly two fields: "question" and "answer".
    
You must ALWAYS respond with a JSON object containing an array of Q&A pairs.
    
Return ONLY a JSON object with the specified format.

Example format:
{{
    "qa_pairs": [
        {{
            "question": "Your question here",
            "answer": "Your answer here"
        }},
        {{
            "question": "Another question here",
            "answer": "Another answer here"
        }}
    ]
}}



Topic
{topic}"""),
            ]
        )

        # Create the combined chain using LangChain Expression Language (LCEL)
        self.chain = prompt_template | model | StrOutputParser()
        # chain = prompt_template | model

    def qa_chain(self, topic):
        # Run the chain
        result = self.chain.invoke({"topic": topic})

        # Output
        return result
    

if __name__ == "__main__":
    qa_generator = GenerateQA()
    print(qa_generator.qa_chain("Artificial Intelligence"))
