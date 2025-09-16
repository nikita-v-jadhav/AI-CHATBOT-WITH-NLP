# CODTECH INTERNSHIP

**COMPANY**: CODTECH IT SOLUTIONS  
**NAME**: [Nikita Vijay Jadhav]  
**INTERN ID**: [CT04DY2366]  
**DOMAIN**: [Python Programming]  
**DURATION**: 4 Weeks  
**MENTOR**: [Neela Santosh Kumar]  

TASK 3 - AI Chatbot with NLP

## Project Description

The goal of this project was to build an AI Chatbot using Natural Language Processing (NLP) libraries such as NLTK in Python. The chatbot was designed to understand user queries and respond appropriately, simulating a conversational experience.

I started the project by installing and setting up the NLTK (Natural Language Toolkit) library, which is one of the most widely used NLP frameworks in Python. First, I downloaded essential datasets and resources like tokenizers, stopwords, and WordNet.

The chatbot was developed using the Chat class from NLTK’s nltk.chat.util module. To enable conversation, I defined a set of patterns and responses. These patterns used regular expressions to detect user inputs such as greetings, questions, or specific keywords. Depending on the input, the chatbot selected a suitable response from its knowledge base.

For example, when the user typed "hello", the bot responded with greetings. Similarly, if the user asked "what is your name?", the bot replied with its assigned name. By adding more patterns, the chatbot could answer questions like date, time, and general knowledge queries.

The chatbot works in a loop, continuously taking user input until the user types an exit command such as "quit". This structure makes it interactive and gives users a feel of real-time conversation.

Through this task, I learned important NLP concepts:

Tokenization: Splitting text into words or sentences.

Reflections: Using a dictionary of simple word mappings (e.g., "I am" → "you are").

Pattern Matching: Using regular expressions to detect user intent.

Rule-based Conversations: Predefined rules for generating responses.

This project was an excellent introduction to NLP and how chatbots work behind the scenes. It also highlighted the importance of designing scalable knowledge bases for real-world AI chatbots such as those used in customer service, education, and healthcare.

## Features

Interactive rule-based chatbot

Built using Python and NLTK

Supports greetings, FAQs, and simple queries

Uses pattern matching and reflections

Runs in terminal/command line interface

## How to Run

Install Python 3.x.

Install the required library:

pip install nltk

## Output 

Run the script:

python chatbot.py

Start chatting with the bot! Type quit to exit.
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/8ce0a6b8-98a6-4536-a9bf-4daaafe534c0" />
