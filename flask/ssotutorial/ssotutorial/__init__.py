from datetime import datetime

from flask import Flask, session, redirect
from flask_sso import SSO

app = Flask('SSOTutorial')
ext = SSO(app=app)

SSO_ATTRIBUTE_MAP = {
    'ADFS_LOGIN': (True, 'nickname'),
}
app.config['SSO_LOGIN_URL'] = '/login'
app.config['SSO_ATTRIBUTE_MAP'] = SSO_ATTRIBUTE_MAP
def time_string():
    t = datetime.now().time()
    return '{0:02d}:{1:02d}:{2:02d}'.format(t.hour, t.minute, t.second)



def wsgi(*args, **kwargs):
    return create_app()(*args, **kwargs)


@ext.login_handler
def login_callback(user_info):
    """Store information in session."""
    session['user'] = user_info

@app.route('/')
def index():
    t = time_string()
    user = session['user'] if 'user' in session else "No one"
    return '<h1>Hello, World!</h1><h2>Server time: {0}</h2> <h2>User: {1}</h2>'.format(t,user)

@app.route('/login')
def login():
    """Display user information or force login."""
    if 'user' in session:
        return redirect('/')
    return redirect(app.config['SSO_LOGIN_URL'])