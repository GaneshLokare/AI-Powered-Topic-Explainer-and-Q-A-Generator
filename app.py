import gradio as gr
import json
import pandas as pd
import tempfile, os
from src.basic_qa_generate import BasicGenerateQA
from src.practical_qa_generate import PracticalGenerateQA
from src.explaination import Explaination

def explain_topic(Topic):
    try:
        # Initialize the Explaination model
        explainer = Explaination()
        
        # Get the JSON string result
        result = explainer.explain_chain(Topic)

        
        return result
    
    except Exception as e:
        return None

def basic_generate_qa(topic):
    try:
        # Initialize the QA generator
        qa_generator = BasicGenerateQA()
        
        # Get the JSON string result
        result = qa_generator.qa_chain(topic)
        
        # Parse the JSON string into a Python dictionary
        qa_pairs = json.loads(result)
        
        # Create a DataFrame for table display
        df = pd.DataFrame(qa_pairs["qa_pairs"])
        
        # Add a column for question numbers
        df.index = df.index + 1
        df.index.name = "No."
        
        # Create temporary CSV file
        temp_dir = tempfile.gettempdir()
        csv_path = os.path.join(temp_dir, f"{topic.replace(' ', '_').lower()}_qa_pairs_basics.csv")
        df.to_csv(csv_path, index=True)
        
        return df, csv_path
    
    except Exception as e:
        return None, None
    
def practical_generate_qa(topic):
    try:
        # Initialize the QA generator
        qa_generator = PracticalGenerateQA()
        
        # Get the JSON string result
        result = qa_generator.qa_chain(topic)
        
        # Parse the JSON string into a Python dictionary
        qa_pairs = json.loads(result)
        
        # Create a DataFrame for table display
        df = pd.DataFrame(qa_pairs["qa_pairs"])
        
        # Add a column for question numbers
        df.index = df.index + 1
        df.index.name = "No."
        
        # Create temporary CSV file
        temp_dir = tempfile.gettempdir()
        csv_path = os.path.join(temp_dir, f"{topic.replace(' ', '_').lower()}_qa_pairs_practical.csv")
        df.to_csv(csv_path, index=True)
        
        return df, csv_path
    
    except Exception as e:
        return None, None

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# AI-Powered Topic Explainer and Q&A Generator")
    # gr.Markdown("Generate questions and answers for any topic.")

    with gr.Tabs():
        with gr.TabItem("Explaination"):
            with gr.Row():
                # Input field for the topic
                topic_input = gr.Textbox(
                    label="Enter Topic Name",
                    placeholder="Enter a topic (e.g., 'Artificial Intelligence', 'Python Programming')",
                    interactive=True
                )

            with gr.Row():
                explain_btn = gr.Button("Explain", variant="primary")
                explaination_output = gr.Textbox(
                    label="Explanation",
                    interactive=False,
                    # lines=10
                )

            # Examples section
            gr.Examples(
                examples=[
                    ["Artificial Intelligence"],
                    ["Python Programming"],
                    ["Data Structures"],
                    ["Machine Learning"],
                ],
                inputs=topic_input,
            )

            # Explanation button handler
            explain_btn.click(
                fn=explain_topic,
                inputs=topic_input,
                outputs=[explaination_output]
            )

        with gr.TabItem("Basic Q&A Generation"):
    
            with gr.Row():
                topic_input = gr.Textbox(
                    label="Enter Topic",
                    placeholder="Enter a topic (e.g., 'Artificial Intelligence', 'Python Programming')",
                )
                generate_btn = gr.Button("Generate Q&A", variant="primary")
            
            with gr.Row():
                # Table output
                output_table = gr.Dataframe(
                    headers=["question", "answer"],
                    label="Generated Q&A Pairs",
                    wrap=True,
                    
                )
            
            # File output for CSV download
            csv_output = gr.File(label="Download Q&A Pairs as CSV")
            
            # Examples
            gr.Examples(
                examples=[
                    ["Artificial Intelligence"],
                    ["Python Programming"],
                    ["Data Structures"],
                    ["Machine Learning"],
                ],
                inputs=topic_input,
            )
            
            # Handle generate button click
            generate_btn.click(
                fn=basic_generate_qa,
                inputs=topic_input,
                outputs=[output_table, csv_output]
            )

        with gr.TabItem("Practical Q&A Generation"):
            with gr.Row():
                topic_input = gr.Textbox(
                    label="Enter Topic",
                    placeholder="Enter a topic (e.g., 'Artificial Intelligence', 'Python Programming')",
                )
                generate_btn = gr.Button("Generate Q&A", variant="primary")
            
            with gr.Row():
                # Table output
                output_table = gr.Dataframe(
                    headers=["question", "answer"],
                    label="Generated Q&A Pairs",
                    wrap=True,
                    
                )
            
            # File output for CSV download
            csv_output = gr.File(label="Download Q&A Pairs as CSV")
            
            # Examples
            gr.Examples(
                examples=[
                    ["Artificial Intelligence"],
                    ["Python Programming"],
                    ["Data Structures"],
                    ["Machine Learning"],
                ],
                inputs=topic_input,
            )
            
            # Handle generate button click
            generate_btn.click(
                fn=practical_generate_qa,
                inputs=topic_input,
                outputs=[output_table, csv_output]
            )
        



if __name__ == "__main__":
    demo.launch(share=True)