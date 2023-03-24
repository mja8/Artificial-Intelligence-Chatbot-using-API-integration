import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "Mrityunjay's AI"},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Hello, sir what you like me to do for you?")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Hi this AI chatbot is developed by Mrityunjay Kumar",
             description="Made on API",
             theme="compact").launch(share=True)