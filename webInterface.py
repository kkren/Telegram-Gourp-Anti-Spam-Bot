from flask import Flask, request, render_template
import requests
# from bot import allow_user
import json
import configparser
# from redisInstance import redis_instance

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)

## "http://test.dev/?session=xxx"
@app.route('/', methods=['GET','POST'])
def recaptcha():
    session = request.args.get('session')
    if session == '':
        return "<p>Missing session key.</p>", 400
    x_forwarded_for = request.headers.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        real_ip = x_forwarded_for.split(',')[0]
    else:
        real_ip = request.headers.get('REMOTE_ADDR')
    if request.method == "POST": 
        captcha_response = request.args['response']
        payload = {'response':captcha_response, 'secret':app.config['reCAPTCHA_SCRECT_KEY']}
        response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
        response_text = json.loads(response.text)
    return render_template('index.html', key=config['BOT']['reCAPTCHA_SITE_KEY'])


@app.errorhandler(404)
def page_not_found(e):
    return "<p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run()