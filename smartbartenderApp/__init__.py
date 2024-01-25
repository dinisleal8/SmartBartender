from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def open_firefox_kiosk():
    os.system('sudo /home/smartbartender/smartbartender.sh')
    return 'Opening Firefox in kiosk mode'

if __name__ == '__main__':
    app.run()
