import os
from flask import send_from_directory
# Import the required modules in your Python file:
from flask import Flask, render_template, redirect, request, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user


def method_name():
    pass


# Create a Flask app object:
app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key_here'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(
            app.root_path,
            'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon')

# Define a user model


class User(UserMixin):
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"<User: {self.id}"

# Create a list of users for testing purposes


users = {'1': {'username': 'john', 'password': 'password'}}

# Create a login manager and initialize it with the app:

login_manager = LoginManager()
login_manager.init_app(app)

# Define a function to load users by ID


@login_manager.user_loader


def load_user(user_id):
    return User(user_id)

# Define a login route


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = None
        for id, data in users.items():
            if data['username'] == username and data['password'] == password:
                user = User(id)
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page or url_for('home'))
        if not user:
            return "Invalid username or password"
    return render_template('login.html')

# Add authentication to specific routes using the @login_required decorator


@app.route('/')
@login_required
def profile():
    return f"Hello, {user.id}!"

# Define a logout route


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

# Define a home route that requires login:


@app.route('/')
@login_required
def home():
    return "Welcome, you are logged in!"


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        id = str(int(max(users.keys())) + 1)
        users[id] = {'username': username, 'password': password}
        user = User(id)
        login_user(user)
        return redirect('/')
    return render_template('register.html')

# Update the login route to redirect to the previous page after login
# Ren the app.

if __name__ == '__main__':
    app.run(debug=True)
