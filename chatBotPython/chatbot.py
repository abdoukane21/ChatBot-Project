import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

# Initialize WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Load intents and other necessary files
intents = {}
words = []
classes = []
model = None

def load_chatbot_data():
    global intents, words, classes, model
    intents = json.load(open(r'C:\Users\pc\OneDrive\Documents\CERTIFICATE\chatBotPython\intents.json'))
    words = pickle.load(open('words.pkl', 'rb'))
    classes = pickle.load(open('classes.pkl', 'rb'))
    model = load_model('chatbot_model.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow_ = bow(sentence)  # Avoid variable name conflict
    res = model.predict(np.array([bow_]))[0]
    ERROR_THRESHOLD = 0.25  # Fix the threshold
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list):
    tag = intents_list[0]['intent']
    for intent in intents['intents']:
        if intent['tag'] == tag:
            result = random.choice(intent['responses'])
            break
    return result

# Load chatbot data when the script is imported
load_chatbot_data()
