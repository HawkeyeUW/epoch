import os
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')

def get_epoch():
    result = int(time.time())
    return str(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6725))
    app.run(host='0.0.0.0', port=port)
    print(get_epoch())
