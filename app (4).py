import os
import gradio as gr
from helper import generate_reply

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_KEY:
    raise ValueError("🔑 Set OPENAI_API_KEY in your Space’s Secrets.")

def respond(user_message, history):
    bot_message = generate_reply(user_message)
    history = history or []
    history.append((user_message, bot_message))
    return history, ""

with gr.Blocks(css="""
    body { background-color: #f5f5f5; }
    .gradio-container { max-width: 700px; margin: auto; padding: 1rem; }
""") as demo:
    gr.Markdown("## 🤖 Your AI Companion")
    chatbot = gr.Chatbot()
    with gr.Row():
        txt = gr.Textbox(placeholder="Type here…", show_label=False, lines=1)
        send = gr.Button("Send")
    txt.submit(respond, [txt, chatbot], [chatbot, txt])
    send.click(respond, [txt, chatbot], [chatbot, txt])

if __name__ == "__main__":
    demo.launch()
