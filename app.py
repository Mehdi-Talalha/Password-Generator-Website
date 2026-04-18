from flask import Flask, render_template, request
import random
import string
import os

def Generate_password(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))

# to run the server ==> flask --app app.py run --debug --port 5001

app = Flask(__name__)

CHARACTER_MAP = {
    "digits" : string.digits,
    "ascii_letters" : string.ascii_letters,
    "punctuation" : string.punctuation
}

char_key = ['digits', 'ascii_letters','punctuation']
char_value = [string.digits, string.ascii_letters, string.punctuation]

@app.route("/", methods=["GET", "POST"])
def index():    
    if request.method == "POST":
        length = int(request.form.get("length"))
        
        characters = ""

        for i in range(len(char_key)):
            if request.form.get(char_key[i]):
                characters += char_value[i]
                
        if not characters:
            # trmember to remove whitespaces
            characters = string.printable
            
        # handle if the length exist and not agreed
        if length:
            try:
                if length < 8:
                    return render_template("index.html", error="Length should be greater than 8")
                elif length > 50:
                    return render_template("index.html", error="Length should be shorter than 50.")
                else:
                    password = Generate_password(length, characters)
                    return render_template("index.html", password=password, length=length)
            except ValueError:
                return render_template("index.html",error="Please enter a number.")
        else:
            # handle if the length doesn't exist
            return render_template("index.html", error="Please enter the length.")
    # return the default website of they are no length recived
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)