from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Simple HTML without templates
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Password Generator</title>
    </head>
    <body>
        <h1>Password Generator</h1>
        <p>App is working!</p>
    </body>
    </html>
    """
    return html

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
