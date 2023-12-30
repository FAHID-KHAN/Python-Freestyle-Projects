"""
A chatbot is a computer program that understands the intent of your query to answer with a solution. Chatbots are the most popular applications of Natural Language Processing in the industry. So, if you want to build an end-to-end chatbot, this article is for you. In this article, I will take you through how to create an end-to-end chatbot using Python.

What is an End to End Chatbot?
An end-to-end chatbot refers to a chatbot that can handle a complete conversation from start to finish without requiring human assistance. To create an end-to-end chatbot, you need to write a computer program that can understand user requests, generate appropriate responses, and take action when necessary. This involves collecting data, choosing a programming language and NLP tools, training the chatbot, and testing and refining it before making it available to users. 

Once deployed, users can interact with the chatbot by sending it multiple requests and the chatbot can handle the entire conversation itself. To create an end-to-end chatbot using Python, we can follow the steps mentioned below:

Define Intents
Create training data
Train the chatbot
Build the chatbot
Test the chatbot
Deploy the chatbot
I hope you now have understood what an end-to-end chatbot is and the process of creating an end-to-end chatbot. In the section below, I’ll walk you through how to build an end-to-end chatbot using Python.


    """

import os 
import nltk 
import ssl 
import streamlit as st 
import random 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

intents = [
    {
        "tag": "greeting",
        "patterns": ["Hi", "Hello", "Hey", "How are you", "What's up"],
        "responses": ["Hi there", "Hello", "Hey", "I'm fine, thank you", "Nothing much"]
    },
    {
        "tag": "goodbye",
        "patterns": ["Bye", "See you later", "Goodbye", "Take care"],
        "responses": ["Goodbye", "See you later", "Take care"]
    },
    {
        "tag": "thanks",
        "patterns": ["Thank you", "Thanks", "Thanks a lot", "I appreciate it"],
        "responses": ["You're welcome", "No problem", "Glad I could help"]
    },
    {
        "tag": "about",
        "patterns": ["What can you do", "Who are you", "What are you", "What is your purpose"],
        "responses": ["I am a chatbot", "My purpose is to assist you", "I can answer questions and provide assistance"]
    },
    {
        "tag": "help",
        "patterns": ["Help", "I need help", "Can you help me", "What should I do"],
        "responses": ["Sure, what do you need help with?", "I'm here to help. What's the problem?", "How can I assist you?"]
    },
    {
        "tag": "Moyen",
        "patterns": ["Tell Me something about Mr Moyen?", "What's your age"],
        "responses": ["Mr. Moyen, he's the kind of guy who would bring a ruler to bed to see how long he slept. If you need someone to break the ice at a party, don't worry, Mr. Moyen's already talking to it, trying to persuade it that it's not cool enough. He's a real legend in his own mind, and we're all just living in it. Seriously, he’s the only person I know who could make a cup of coffee nervous. But, let's be honest, we all need a Mr. Moyen in our lives – life's more interesting when you're never quite sure if he’s using a GPS to find his way out of a roundabout", "Age is just a number for me."]
    },
    {
        "tag": "Ben",
        "patterns": ["Tell me something about Mr Ben?", "How's it can be a easier death for Mr Ben?"],
        "responses": ["Ah, Ben, the only guy I know who can trip over a wireless internet connection. He’s the kind of person who could get lost on an escalator. But honestly, we love Ben – he’s unique. He’s like a software update in the middle of a workday: you know it’s necessary, but you can’t help but think, ‘Not now, Ben!"]
    },
    {
        "tag": "budget",
        "patterns": ["How can I make a budget", "What's a good budgeting strategy", "How do I create a budget"],
        "responses": ["To make a budget, start by tracking your income and expenses. Then, allocate your income towards essential expenses like rent, food, and bills. Next, allocate some of your income towards savings and debt repayment. Finally, allocate the remainder of your income towards discretionary expenses like entertainment and hobbies.", "A good budgeting strategy is to use the 50/30/20 rule. This means allocating 50% of your income towards essential expenses, 30% towards discretionary expenses, and 20% towards savings and debt repayment.", "To create a budget, start by setting financial goals for yourself. Then, track your income and expenses for a few months to get a sense of where your money is going. Next, create a budget by allocating your income towards essential expenses, savings and debt repayment, and discretionary expenses."]
    },
    {
        "tag": "credit_score",
        "patterns": ["What is a credit score", "How do I check my credit score", "How can I improve my credit score"],
        "responses": ["A credit score is a number that represents your creditworthiness. It is based on your credit history and is used by lenders to determine whether or not to lend you money. The higher your credit score, the more likely you are to be approved for credit.", "You can check your credit score for free on several websites such as Credit Karma and Credit Sesame."]
    }
]


vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0,max_iter=10000)

tags =[]
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x,y)

def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response
        

counter = 0

def main():
    global counter
    st.title("Chatbot")
    st.write("Welcome to the chatbot. Please type a message and press Enter to start the conversation.")

    counter += 1
    user_input = st.text_input("You:", key=f"user_input_{counter}")

    if user_input:
        response = chatbot(user_input)
        st.text_area("Chatbot:", value=response, height=100, max_chars=None, key=f"chatbot_response_{counter}")

        if response.lower() in ['goodbye', 'bye']:
            st.write("Thank you for chatting with me. Have a great day!")
            st.stop()

if __name__ == '__main__':
    main()
