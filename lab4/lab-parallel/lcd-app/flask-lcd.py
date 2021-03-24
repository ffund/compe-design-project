from flask import Flask, request, render_template
import virtualhat

app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_text():
    text = request.form['text']
    print(text)
    virtualhat.string_to_lcd(text)
    return render_template('index.html')

if __name__ == "__main__":
    virtualhat.setup()
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)

