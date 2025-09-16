import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources (run once)
nltk.download('punkt')
nltk.download('wordnet')

# Sample corpus (knowledge base for the chatbot)
corpus = """
Hello! I am an AI chatbot. 
I can answer your queries related to Artificial Intelligence, Python, and NLP.
Natural Language Processing (NLP) is a field of AI that helps computers understand human language.
Python is a popular programming language used for AI, machine learning, and data science.
Machine learning is a subset of AI that enables systems to learn from data.
Artificial Intelligence is the simulation of human intelligence in machines.
"""

# Tokenize the corpus
sent_tokens = nltk.sent_tokenize(corpus)
word_tokens = nltk.word_tokenize(corpus)

# Lemmatizer
lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token.lower()) for token in tokens if token not in string.punctuation]

# Normalize text
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower()))

# Greeting inputs and responses
GREETING_INPUTS = ("hello", "hi", "hey", "greetings", "what's up")
GREETING_RESPONSES = ["Hi there!", "Hello!", "Hey!", "Greetings!", "How can I help you?"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Response generator
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)

    vectorizer = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = vectorizer.fit_transform(sent_tokens)

    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if req_tfidf == 0:
        robo_response = "I'm sorry, I don't understand you."
    else:
        robo_response = sent_tokens[idx]

    sent_tokens.remove(user_response)
    return robo_response

# Main chatbot loop
print("AI Chatbot: I am your chatbot. Type 'bye' to exit.")

while True:
    user_response = input("You: ").lower()
    if user_response == 'bye':
        print("AI Chatbot: Goodbye! Have a nice day.")
        break
    elif greeting(user_response) is not None:
        print("AI Chatbot:", greeting(user_response))
    else:
        print("AI Chatbot:", response(user_response))
