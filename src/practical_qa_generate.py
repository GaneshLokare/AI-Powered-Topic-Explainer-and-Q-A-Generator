from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI


class PracticalGenerateQA:
    def __init__(self):
        load_dotenv()
        # Create a ChatOpenAI model
        model = ChatOpenAI(model="gpt-4o-mini", response_format={ "type": "json_object" })

        # Define prompt templates (no need for separate Runnable chains)
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("human", """ You are an expert interviewer and coach, skilled at preparing candidates for success. Generate a comprehensive and well-structured answer to an interview question on the following topic: {Topic}.

Ensure that the response:

Starts with a concise introduction or overview of the topic to demonstrate foundational knowledge.
Includes key points or concepts relevant to the topic, supported by examples, statistics, or real-world applications where applicable.
Addresses potential follow-up questions or nuances to showcase depth of understanding.
Maintains a professional tone and uses clear, concise language suitable for a job interview setting.
Ends with a confident conclusion or takeaway that reinforces the candidate's expertise and readiness to contribute in a professional role.
Example Format:

Introduction: Provide a brief explanation of the topic.
Key Points: Highlight 3-5 critical aspects, including examples or evidence.
Challenges/Solutions: Discuss potential challenges and how to address them (if applicable).
Conclusion: Summarize the key message and relate it to the interview context.
    
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
"""),
            ]
        )

        # Create the combined chain using LangChain Expression Language (LCEL)
        self.chain = prompt_template | model | StrOutputParser()
        # chain = prompt_template | model

    def qa_chain(self, Topic):
        # Run the chain
        result = self.chain.invoke({"Topic": Topic})

        # Output
        return result
    

if __name__ == "__main__":
    qa_generator = GenerateQA()
    print(qa_generator.qa_chain("Artificial Intelligence"))
