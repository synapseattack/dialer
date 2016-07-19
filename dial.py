from twilio import twiml
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def root():
    dialednumber = str(request.values.get('To'))
    resp = twiml.Response()
    resp.dial(dialednumber)
    # resp.dial(dialednumber)
    return str(resp)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

