from flask import Flask, redirect
import virtualhat

app = Flask(__name__, static_folder='')

@app.route("/")
def hello():
    return app.send_static_file('index.html')

@app.route('/led/<int:action>')
def blink_led(action):
    if action==0:
        virtualhat.led_off()
    if action==1:
        virtualhat.led_on()
    return redirect("/")

if __name__ == "__main__":

    virtualhat.setup()
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)

