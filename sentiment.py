from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import nltk
import string
import re
from nltk.corpus import stopwords
nltk.download('stopwords')


def remove_extras(sentence: str) -> str:
    sentence = re.sub(r'http\S+', " ", sentence)    # remove urls
    sentence = re.sub(r'@\w+',' ', sentence)         # remove mentions
    sentence = re.sub(r'#\w+', ' ', sentence)       # remove hastags
    sentence = re.sub(r'<.*?>',' ', sentence)       # remove html tags
    return sentence

punctuations = string.punctuation  #"""!.',?#@;+)-(/:"&$"""
def remove_stopwords(sentence: str) -> str:
  sentence = remove_extras(sentence)
  stop_words = stopwords.words("english")
  words = sentence.split()
  words = " ".join([word for word in words if word not in stop_words])
  for punctuation in punctuations:
    words = words.replace(punctuation, '')
  return words


def encode_input(msg, word_dict):
  msg = msg.lower().split(" ")
  encoded = [[word_dict[word] for word in msg if word in word_dict.keys()]]
  return pad_sequences(encoded, maxlen=100, truncating='post', padding='post')


def remember_words():
  f = open("vocabulary.txt", 'r')
  vocab = eval(f.read())
  return vocab

def final_encoder(msg):
  vocab = remember_words()
  return encode_input(remove_stopwords(msg), vocab)

def mood(message):
  feelings = ['anger', 'fear', 'happy', 'love', 'sadness', 'surprise']
  model = load_model('SentiBot.h5')
  sentiment = model.predict(final_encoder(message))
  return feelings[sentiment]

