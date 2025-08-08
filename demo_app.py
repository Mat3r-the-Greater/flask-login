from flask import Flask, render_template_string
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.secret_key = 'super-secret-key-123'  # Intentionally weak for demo

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def home():
    return '<h1>Flask-Login Demo</h1><a href="/login">Login</a>'

@app.route('/login')
def login():
    user = User(1)
    login_user(user)
    return '<h1>Logged in!</h1><a href="/protected">Go to protected page</a>'

@app.route('/protected')
@login_required
def protected():
    return f'<h1>Protected Page</h1><p>Hello user {current_user.id}!</p><a href="/logout">Logout</a>'

@app.route('/logout')
def logout():
    logout_user()
    return '<h1>Logged out!</h1><a href="/">Home</a>'

if __name__ == '__main__':
    print("Starting Flask-Login Demo on http://localhost:5000")
    app.run(debug=True)