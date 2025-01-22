from flask import Flask, request, jsonify
import pickle
from bs4 import BeautifulSoup
import re
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from flask_cors import CORS 
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize the Flask app
app = Flask(__name__)
CORS(app)

with open('tfidf.pkl', 'rb') as file:
    tfidf = pickle.load(file)

# Load the trained classifier
with open('clf.pkl', 'rb') as file:
    clf = pickle.load(file)

# Load the top tags
with open('top_tags.pkl', 'rb') as file:
    loaded_top_tags = pickle.load(file)

# Define helper functions
def clean_text(sentence):
    soup = BeautifulSoup(sentence, "html.parser")  # Remove HTML tags
    sentence = soup.get_text()
    sentence = sentence.lower()  # Lowercase the text
    sentence = re.sub(r"[^c\#|c\+\+|f\#|asp\.net|vb\.net|node\.js|objective\-c|\w\s]", "", sentence)  # Remove special characters
    sentence = re.sub(r'\d+', '', sentence)  # Remove all numbers
    sentence = ' '.join([word for word in sentence.split() if '_' not in word and word.isascii() and not any(char.isdigit() for char in word)])  # Remove unwanted words
    sentence = re.sub(r'\s+', ' ', sentence).strip()  # Remove extra whitespace
    return sentence

def tokenize_text(cleaned_sentence):
    tokenizer = RegexpTokenizer(r"(c\#|c\+\+|f\#|asp\.net|vb\.net|node\.js|objective\-c|\w+)")
    return tokenizer.tokenize(cleaned_sentence)

stop_w = set(stopwords.words('english'))
def stop_word_filter(list_words):
    return [w for w in list_words if w not in stop_w and len(w) >= 2]

lemmatizer = WordNetLemmatizer()
def lemma_words(list_words):
    return [lemmatizer.lemmatize(w, pos='v') for w in list_words]

def preprocess_bow(desc_text):
    cleaned = clean_text(desc_text)
    tokens = tokenize_text(cleaned)
    filtered = stop_word_filter(tokens)
    lemmatized = lemma_words(filtered)
    return lemmatized

# API endpoint for tag prediction
@app.route('/predict-tags', methods=['POST'])
def predict_tags():
    try:
        # Get the input text from the request
        data = request.get_json()
        if 'text' not in data:
            return jsonify({"error": "Missing 'text' field in request"}), 400

        input_text = data['text']

        # Preprocess the input text
        processed_text = preprocess_bow(input_text)
        processed_text_str = ' '.join(processed_text)

        # Transform the text using Tfidf
        input_tfidf = tfidf.transform([processed_text_str])

        # Predict the tags
        predicted_tags = clf.predict(input_tfidf)

        # Map the binary vector to tag names
        predicted_tag_names = [loaded_top_tags[i] for i in range(len(predicted_tags[0])) if predicted_tags[0][i] == 1]

        # Return the predicted tags as a JSON response
        return jsonify({"predicted_tags": predicted_tag_names})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
