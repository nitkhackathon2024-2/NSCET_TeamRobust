from flask import Flask, request, render_template, jsonify
from document_processor import process_document

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    result = process_document(file)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
