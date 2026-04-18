from flask import Flask, render_template, request
import random
import string
import os

app = Flask(__name__)

def Generate_password(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))

char_key = ['digits', 'ascii_letters','punctuation']
char_value = [string.digits, string.ascii_letters, string.punctuation]

@app.route("/", methods=["GET", "POST"])
def index():    
    if request.method == "POST":
        length_str = request.form.get("length")
        
        characters = ""
        for i in range(len(char_key)):
            if request.form.get(char_key[i]):
                characters += char_value[i]
                
        if not characters:
            characters = string.printable
            
        if length_str:
            try:
                length = int(length_str)
                if length < 4:
                    return render_template("simple.html", error="Length should be at least 4")
                elif length > 50:
                    return render_template("simple.html", error="Length should be shorter than 50.")
                else:
                    password = Generate_password(length, characters)
                    return render_template("simple.html", password=password, length=length)
            except ValueError:
                return render_template("simple.html", error="Please enter a number.")
        else:
            return render_template("simple.html", error="Please enter the length.")
    
    return render_template("simple.html")

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
