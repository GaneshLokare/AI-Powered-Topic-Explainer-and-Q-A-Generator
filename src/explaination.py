from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI


class Explaination:
    def __init__(self):
        load_dotenv()
        # Create a ChatOpenAI model
        model = ChatOpenAI(model="gpt-4o-mini")

        # Define prompt templates (no need for separate Runnable chains)
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("human", """ I am having difficulty learning {Topic}. Help me to undertand it better by using first principle thinking. """),
            ]
        )

        # Create the combined chain using LangChain Expression Language (LCEL)
        self.chain = prompt_template | model | StrOutputParser()
        # chain = prompt_template | model

    def explain_chain(self, Topic):
        # Run the chain
        result = self.chain.invoke({"Topic": Topic})

        # Output
        return result
