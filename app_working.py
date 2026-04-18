from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Password Generator</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            .container { max-width: 600px; margin: 0 auto; padding: 20px; }
            .success { color: #28a745; font-size: 24px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="success">Password Generator is Working! </h1>
            <p>If you see this, the deployment succeeded.</p>
            <p>Time: {}</p>
        </div>
    </body>
    </html>
    '''.format(os.environ.get('RAILWAY_ENVIRONMENT', 'local'))

@app.route('/health')
def health():
    return {"status": "healthy", "environment": os.environ.get('RAILWAY_ENVIRONMENT', 'local')}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
