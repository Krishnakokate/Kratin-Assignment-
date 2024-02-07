from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_user, UserMixin, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use SQLite for simplicity
app.config['SECRET_KEY'] = 'your_secret_key'


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    contact = db.Column(db.String(15))
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(255))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    with app.app_context():
        db.create_all()
    return app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle form submission
        username = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        contact = request.form.get('contact')
        email = request.form.get('email')
        address = request.form.get('address')
        password = request.form.get('password')

        new_user = User(
            username=username,
            age=age,
            gender=gender,
            contact=contact,
            email=email,
            address=address
        )
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully. You can now login.', 'success')
        return redirect(url_for('home'))

    # Render the signup page for both GET and POST requests
    return render_template('signup.html')


# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form.get('userName')
#     password = request.form.get('password')

#     user = User.query.filter_by(username=username).first()

#     if user and user.check_password(password):
#         flash('Login successful', 'success')
#         return redirect(url_for('dashboard'))
#     else:
        
#         flash('Invalid username or password', 'danger')
#         return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle the login form submission
        username = request.form.get('userName')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            flash('Login successful', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('home'))

    # Render the login form for GET requests
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



# @app.route('/your_info', methods=['GET', 'POST'])
# @login_required
# def your_info():
#     user = current_user
#     if request.method == 'POST':
#         user.username = request.form.get('name')
#         user.age = request.form.get('age')
#         user.gender = request.form.get('gender')
#         user.weight = request.form.get('weight')
#         user.height = request.form.get('height')
#         user.blood_group = request.form.get('blood_group')
#         db.session.commit()
#         flash('Your info has been updated successfully.', 'success')
#         return redirect(url_for('your_info'))
#     return render_template('your_info.html', user=user)


@app.route('/update_user_info', methods=['POST'])
@login_required
def update_user_info():
    # Fetch user details from the database (replace with actual user details retrieval logic)
    user = current_user

    # Update user details based on the form submission
    user.username = request.form.get('name')
    user.age = request.form.get('age')
    user.gender = request.form.get('gender')
    user.contact = request.form.get('contact')
    user.email = request.form.get('email')
    user.address = request.form.get('address')

    # Commit changes to the database
    db.session.commit()

    flash('Your info has been updated successfully.', 'success')
    return redirect(url_for('your_info'))

@app.route('/your_info')
def your_info():
    return render_template('your_info.html')

@app.route('/eating_schedule')
def eating_schedule():
    return render_template('eating_schedule.html')

@app.route('/your_reminders')
def your_reminders():
    return render_template('your_reminders.html')

@app.route('/your_exercise')
def your_exercise():
    return render_template('your_exercise.html')

if __name__ == '__main__':

    create_app().run(debug=True)
