# AUTHOR: Kamil Agdere
# CLASS: C104
# PROJECT: Secret Manager

# THERE IS MADE USE OF CHATGPT AND OTHER WEBSITES

# Import necessary modules and packages
from flask import Blueprint, render_template, flash, g, redirect, request, session, url_for, Flask, request
import mysql.connector as mysql
from datetime import datetime
from .db import *
from argon2 import PasswordHasher
import pytz

# Create a Flask application
app = Flask(__name__)

# Create a Blueprint named "home"
bp = Blueprint("home", __name__)

# Create instance for argon2 hashing
ph = PasswordHasher()

# Route for the home page
@bp.route("/")
def index():
    return render_template("home/index.html")

# Route for the about me page
@bp.route("/about", methods=["GET"])
def about_me():
    return render_template("home/about.html")

# Route for user profile
@bp.route("/profile", methods=["GET"])
def profile():
    # Check if the user is logged in
    if 'loggedin' in session:
        user_id = session['id']

        # Fetch user information from the database
        with db_connection() as db:
            with db.cursor() as cursor:
                cursor.execute("SELECT * FROM User WHERE id = %s", (user_id,))
                user = cursor.fetchone()

                last_login_prev = user[5]

        return render_template("home/profile.html", user=user, last_login_prev=last_login_prev)
    else:
        return redirect(url_for('home.login'))

# Route for handling user login
@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['upsw']

        try:
            with db_connection() as db:
                with db.cursor() as cursor:
                    cursor.execute("SELECT * FROM User WHERE username=%s", (username,))
                    user = cursor.fetchone()

                    if user and ph.verify(user[2], password):
                        # If user is found and password is correct, create a session and log them in
                        session['loggedin'] = True
                        session['id'] = user[0]
                        session['username'] = username

                        # Update last login timestamp
                        timezone_amsterdam = pytz.timezone('Europe/Amsterdam')
                        cursor.execute("UPDATE User SET last_login_prev = last_login, last_login = %s WHERE id = %s", (datetime.now(timezone_amsterdam), user[0]))
                        db.commit()

                        return redirect(url_for('home.index'))
                    else:
                        flash("Invalid username or password", "error")

        except Exception as e:
            return f"An error occurred: {str(e)}"

    return render_template('home/login.html')

# Route for user logout
@bp.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('home.login'))

# Route for registration form manual
@bp.route("/register-manual", methods=["GET"])
def register_manual():
    return render_template("home/register-manual.html")

# Route for user registration
@bp.route("/registreren", methods=["GET", "POST"])
def register():
    # set up a database connection
    db = db_connection()

    if request.method == 'POST':
        username = request.form['gebruikersnaam']
        password = request.form['psw']
        email    = request.form['email']

        # Hash the password for secure storage
        hashed_password = ph.hash(password)

        try:
            cursor = db.cursor()
            cursor.execute("INSERT INTO User (username, password_hash, email) VALUES (%s, %s, %s)", (username, hashed_password, email))
            db.commit()
            cursor.close()
            return redirect(url_for('home.login'))
        except mysql.connector.IntegrityError as ErrorLogin:
            ErrorLogin = "Gebruiker al in gebruik"
    return render_template('home/registreren.html')


# Route for the contact page
@bp.route("/contact", methods=["GET"])
def contact():
    return render_template("home/contact.html")

# Route for displaying the user's secrets
@bp.route("/my-secrets", methods=["GET"])
def my_secrets():
    if 'loggedin' in session:
        user_id = session['id']

        # Pagination logic where only 9 secrets at a time can be displayed
        page = request.args.get('page', 1, type=int)
        per_page = 9
        
        offset = (page - 1) * per_page

        # Fetch the user's secrets from the database
        with db_connection() as db:
            with db.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM Secret WHERE id IN (SELECT secret_id FROM SecretAccess WHERE user_id = %s)", (user_id,))
                total_secrets = cursor.fetchone()[0]

                total_pages = (total_secrets + per_page - 1) // per_page

                # Check if there is a next page
                has_next_page = page < total_pages

                # Check if there is a previous page
                has_prev_page = page > 1

                cursor.execute("SELECT * FROM Secret WHERE id IN (SELECT secret_id FROM SecretAccess WHERE user_id = %s) LIMIT %s OFFSET %s", (user_id, per_page, offset))
                secrets = cursor.fetchall()
        return render_template('home/my-secrets.html', secrets=secrets, page=page, total_pages=total_pages, has_next_page=has_next_page, has_prev_page=has_prev_page)
    else:
        return redirect(url_for('home.login'))


# Route for adding a new secret
@bp.route("/add-secret", methods=["GET", "POST"])
def add_secret():
    # set up a database connection
    db = db_connection()
    if 'loggedin' in session:
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            username = session['username']
            user_id = session['id']
            timezone_amsterdam = pytz.timezone('Europe/Amsterdam')
            upload_time = datetime.now(timezone_amsterdam)
            try:
                cursor = db.cursor()
                cursor.execute("INSERT INTO Secret (name, info, user_name, user_id, upload_date, author_id) VALUES (%s, %s, %s, %s, %s, %s)", (title, content, username, user_id, upload_time, user_id))
                db.commit()
                secret_id = cursor.lastrowid
                cursor.execute("INSERT INTO SecretAccess (user_id, secret_id) VALUES (%s, %s)", (user_id, secret_id))
                db.commit()
                cursor.close()
                return redirect(url_for('home.my_secrets'))
            except:
                return redirect(url_for('home.add_secret'))
    else:
        return redirect(url_for('home.login'))
    return render_template('home/add-secret.html')

# Route for deleting a secret
@bp.route("/delete-secret/<int:secret_id>", methods=["POST"])
def delete_secret(secret_id):
    if 'loggedin' in session:
        user_id = session['id']
        with db_connection() as db:
            with db.cursor() as cursor:
                cursor.execute("SELECT * FROM Secret WHERE id = %s AND user_id = %s", (secret_id, user_id))
                secret = cursor.fetchone()

                if secret:
                    cursor.execute("DELETE FROM Secret WHERE id = %s", (secret_id,))
                    db.commit()
                    flash("Secret deleted successfully", "success")
                else:
                    flash("Secret not found or you don't have permission to delete it", "error")

        return redirect(url_for('home.my_secrets'))
    else:
        return redirect(url_for('home.login'))

# Route for editing a secret
@bp.route("/edit-secret", methods=["GET", "POST"])
def edit_secret():
    secret_id = request.args.get('secret_id')
    if 'loggedin' in session:
        user_id = session['id']
        with db_connection() as db:
            with db.cursor() as cursor:
                cursor.execute("SELECT * FROM Secret WHERE id = %s AND user_id = %s", (secret_id, user_id))
                secret = cursor.fetchone()

                if secret:
                    return render_template('home/edit-secret.html', secret=secret)
                else:
                    flash("Secret not found or you don't have permission to edit it", "error")

        return redirect(url_for('home.my_secrets'))
    else:
        return redirect(url_for('home.login'))

@bp.route("/update-secret/<int:secret_id>", methods=["POST"])
def update_secret(secret_id):
    if 'loggedin' in session:
        user_id = session['id']
        title = request.form['title']
        content = request.form['content']

        with db_connection() as db:
            with db.cursor() as cursor:
                cursor.execute("UPDATE Secret SET name = %s, info = %s WHERE id = %s AND user_id = %s", (title, content, secret_id, user_id))
                db.commit()
                flash("Secret updated successfully", "success")

        return redirect(url_for('home.my_secrets'))
    else:
        return redirect(url_for('home.login'))

# Route for inviting users to secrets
@bp.route("/invite-user/<int:secret_id>", methods=["GET", "POST"])
def invite_user(secret_id):
    if 'loggedin' in session:
        user_id = session['id']
        # Haal de auteur van het geheim op
        with db_connection() as db:
            with db.cursor() as cursor:
                cursor.execute("SELECT author_id FROM Secret WHERE id = %s", (secret_id,))
                author_id = cursor.fetchone()[0]
                if user_id == author_id:  # Controleer of de huidige gebruiker de auteur is
                    if request.method == 'POST':
                        invited_username = request.form['invited_username']

                        cursor.execute("SELECT * FROM User WHERE username = %s", (invited_username,))
                        invited_user = cursor.fetchone()
                        if invited_user:
                            invited_user_id = invited_user[0]
                            
                            # Voeg een entry toe aan SecretAccess om toegang te verlenen
                            cursor.execute("INSERT INTO SecretAccess (user_id, secret_id) VALUES (%s, %s)", (invited_user_id, secret_id))
                            db.commit()
                            flash(f"Gebruiker {invited_username} heeft nu toegang tot het geheim.", "success")
                            return redirect(url_for('home.my_secrets'))
                        else:
                            flash("Deze gebruiker bestaat niet.", "error")
                else:
                    flash("Je hebt geen toestemming om deze actie uit te voeren.", "error")
                    return redirect(url_for('home.my_secrets'))
    else:
        return redirect(url_for('home.login'))
    return render_template('home/invite-user.html', secret_id=secret_id)

# Route for deleting an account
@bp.route("/delete-account", methods=["GET", "POST"])
def delete_account():
    if 'loggedin' in session:
        if request.method == 'POST':
            password = request.form['password']
            username = session['username']
            
            try:
                with db_connection() as db:
                    with db.cursor() as cursor:
                        cursor.execute("SELECT * FROM User WHERE username = %s", (username,))
                        user = cursor.fetchone()

                        if user and ph.verify(user[2], password):
                            cursor.execute("DELETE FROM User WHERE id = %s", (user[0],))
                            db.commit()

                            session.pop('loggedin', None)
                            session.pop('id', None)
                            session.pop('username', None)

                            flash("Je account is succesvol verwijderd.", "success")
                            return redirect(url_for('home.index'))
                        else:
                            flash("Het ingevoerde wachtwoord is onjuist. Probeer opnieuw.", "error")

            except Exception as e:
                return f"An error occurred: {str(e)}"
        
        return render_template("home/delete-account.html")
    else:
        return redirect(url_for('home.login'))


# Route for changing password
@bp.route("/change-password", methods=["GET", "POST"])
def change_password():
    if 'loggedin' in session:
        if request.method == 'POST':
            user_id = session['id']
            current_password = request.form['current_password']
            new_password = request.form['new_password']

            # Fetch user information from the database
            with db_connection() as db:
                with db.cursor() as cursor:
                    cursor.execute("SELECT * FROM User WHERE id = %s", (user_id,))
                    user = cursor.fetchone()

                    # If current password is correct, update password
                    if user and ph.verify(user[2], current_password):
                        hashed_password = ph.hash(new_password)
                        cursor.execute("UPDATE User SET password_hash = %s WHERE id = %s", (hashed_password, user_id))
                        db.commit()

                        flash("Password changed successfully", "success")
                        return redirect(url_for('home.profile'))
                    else:
                        flash("Invalid current password", "error")

        return render_template('home/change-password.html')
    else:
        return redirect(url_for('home.login'))
    

if __name__ == '__main__':
    app.run(debug=True)