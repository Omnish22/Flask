# since we are using oauth locally so we have to set some environments
import os 
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
#=======================================================

from flask import Flask, redirect, url_for, render_template 
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret he'

blueprint = make_google_blueprint(client_id='60701671321-o44st9pjfemmj41b1bp3a857j4k9ll0s.apps.googleusercontent.com',client_secret='nulzJgremX-dZxNRgOIxPiy4',offline=True,scope = ['profile','email'])

app.register_blueprint(blueprint,url_prefix='/login')

@app.route('/')
def index():
    return render_template('home.html')



@app.route('/welcome')
def welcome():
    # Return error internal server error if not logged in
    resp = google.get('/oauth2/v2/userinfo')
    print('response',resp)
    assert resp.ok, resp.text
    print('resp.ok and resp.text: ',end='') 
    print(resp.ok, resp.text)
    email = resp.json()['email']
    return render_template('welcome.html',email=email)

@app.route('/login/google')# when we connect to google blueprint it will not throw an error
def login():
    if not google.authorized:
        return render_template(url_for('google.login')) # google.login is in google imported from flask_dance and it is used for login page of google 
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text 
    email = resp.json()['email'] 
    return render_template('welcome.html',email=email)




if __name__=="__main__":
    app.run()