from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/englishToFrench', methods=['POST'])
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    english_text = request.form['text']
    french_text = machinetranslation.englishToFrench(english_text)
    return french_text

@app.route('/frenchToEnglish', methods=['POST'])
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    french_text = request.form['text']
    english_text = machinetranslation.englishToFrench(english_text)
    return english_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
