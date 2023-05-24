from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/engtofr")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    f= translator.engtofr(textToTranslate)
    print(f)
    # Write your code here
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    m = translator.frtoeng(textToTranslate)
    print(m)
    # Write your code here
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)