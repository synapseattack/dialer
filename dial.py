import twilio
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def root():
    dialednumber = request.values.get('to')
    resp = twilio.twiml.Response()
    resp.dial(dialednumber)
    return str(resp)


if __name__ == '__main__':
    app.run()

