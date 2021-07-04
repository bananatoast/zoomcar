from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from markupsafe import escape
import sys
import wiringpi as pi

GPIO_F_LEFT = 17
GPIO_F_RIGHT = 27
GPIO_B_LEFT = 18
GPIO_B_RIGHT = 24

app = Flask(__name__)
CORS(app)

pi.wiringPiSetupGpio()
for gpio in [GPIO_F_LEFT, GPIO_F_RIGHT, GPIO_B_LEFT, GPIO_B_RIGHT]:
    pi.pinMode(gpio, 1)
    pi.softPwmCreate(gpio, 0, 100)

@app.route("/move/<command>", methods = ["POST"])
def move(command):
  cmd = escape(command)
  if cmd == "forward":
    sys.stdout.write("command accepted: {}".format(cmd))
    pi.softPwmWrite(GPIO_F_LEFT,100)
    pi.softPwmWrite(GPIO_F_RIGHT,100)
  elif cmd == "back":
    sys.stdout.write("command accepted: {}".format(cmd))
    pi.softPwmWrite(GPIO_B_LEFT,70)
    pi.softPwmWrite(GPIO_B_RIGHT,70)
  elif cmd == "left":
    sys.stdout.write("command accepted: {}".format(cmd))
    pi.softPwmWrite(GPIO_F_LEFT,40)
    pi.softPwmWrite(GPIO_F_RIGHT,100)
  elif cmd == "right":
    sys.stdout.write("command accepted: {}".format(cmd))
    pi.softPwmWrite(GPIO_F_LEFT,100)
    pi.softPwmWrite(GPIO_F_RIGHT,40)
  elif cmd == "stop":
    sys.stdout.write("command accepted: {}".format(cmd))
    pi.softPwmWrite(GPIO_F_LEFT,0)
    pi.softPwmWrite(GPIO_F_RIGHT,0)
    pi.softPwmWrite(GPIO_B_LEFT,0)
    pi.softPwmWrite(GPIO_B_RIGHT,0)
  else:
    return { "message": "command not found: {}".format(cmd) }, 400
  return "", 204

@app.route("/health", methods=["GET"])
def health():
  return { "message": "OK" }

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)