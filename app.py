from flask import Flask, render_template, request
import random
import string

def Generate_password(length):
    # take the charcters form the string module
    CHARACTERS = "".join(char for char in string.printable if char not in set(string.whitespace))
    # return the random password
    return ''.join(random.choice(CHARACTERS) for _ in range(length))

# to run the server: Type this command in the terminal ==> flask --app app.py run --debug --port 5001

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        length = request.form.get("length")
        # handle if the length exist and not agreed
        if length:
            try:
                length = int(length)
                password = Generate_password(length)
                return render_template("index.html", password=password, length=length)
            except ValueError:
                return render_template("index.html",error="Please enter a valid number")
        else:
            # handle if the length doesn't exist
            return render_template("index.html", error="Please enter the length of the number")
    # return the default website of they are no length recived
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)