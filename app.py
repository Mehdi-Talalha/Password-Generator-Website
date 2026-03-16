from flask import Flask, render_template, request
import random
import string

# alpha_lowercase = string.ascii_lowercase
# alpha_uppercase = string.ascii_uppercase
# numbers = string.digits
# punctuation = string.punctuation
# all = string.printable

def Generate_password(length):
    # take the charcters form the string module
    CHARACTERS = "".join(char for char in string.printable if char not in set(string.whitespace))
    # return the random password
    return ''.join(random.choice(CHARACTERS) for _ in range(length))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        length = request.form.get("length")
        if length:
            try:
                length = int(length)
                password = Generate_password(length)
                return render_template("index.html", password=password, length=length)
            except ValueError:
                return render_template("index.html",   error="Please enter a valid number")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

# let this part to me 
