import pandas as pd
import random
import gradio as gr

# Load the CSV
df = pd.read_csv("cornell_conversations.csv")

# Chatbot logic
def chatbot_response(user_input):
    matches = df[df['Input'].str.lower() == user_input.lower()]
    if not matches.empty:
        return random.choice(matches['Response'].tolist())
    else:
        return random.choice(df['Response'].tolist())

# Gradio interface
iface = gr.Interface(
    fn=chatbot_response,
    inputs="text",
    outputs="text",
    title="🎬 Cornell Movie Chatbot",
    description="Chat with a bot trained on real movie dialogues!"
)

iface.launch()