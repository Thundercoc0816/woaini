# -*- coding: utf-8 -*-
"""
Created on Wed May 17 19:20:22 2023

@author: 17745
"""

import openai
openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "tell me about jesus "}])
print(completion.choices[0].message.content)


openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
    

import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a encyclopaedia"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "智能AI")

demo.launch(share=True)

import requests

url = "http://127.0.0.1:7861"  # Replace with the URL of the local website you want to save

response = requests.get(url)

if response.status_code == 200:  # Check if the request was successful
    with open("local_website.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("Local website saved as local_website.html")
else:
    print("Error: Unable to retrieve the local website")