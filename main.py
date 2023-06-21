import random

from flask import Flask, render_template, redirect



app = Flask(__name__)

# Main Route
@app.route('/')
@app.route('/index.html')
def main():

    return render_template('index.html')

# Register Route
@app.route('/register')
def register():
    return render_template('register.html')
    # return "<title>Arlen's BackEnd - Register</title><h1>Register</h1><input type='text' placeholder='Username'><br><input type='text' placeholder='Email'><br><input type='password' placeholder='Password'><br><br><a href='/home'><button>Register</button>   </a><a href='/'><button>Back</button></a>"

# Login Route
@app.route('/login')
def login():
    return render_template('login.html')
    # return "<title>Arlen's BackEnd - Login</title><h1>Login</h1><input type='text' placeholder='Username/Email'><br><input type='password' placeholder='Password'><br><br><a href='/home'><button>Login</button></a>     <a href='/'><button>Back</button></a>"

# Home Route
@app.route('/home')
def home():
    return render_template('home.html')
    # return "<title>Arlen's BackEnd - Home</title> <h1>Arlen's BackEnd</h1><a href='https://roblox.com'><button>Roblox</button></a>   <a href='https://client.cortexnodes.com'><button>CortexNodes</button></a><br><br><a href='/contact'><button>Contact Us</button></a>   <a href='/blog'><button>Blog</button></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><a href='/'><button>Logout</button></a>"

# Contact Route
@app.route('/home/contact')
def contact():
    user = {
        "name":"Arlen",
        "username":"Arl#8192",
        "age":12
    }
    return render_template('contact.html', user=user)
    # return "<title>Arlen's BackEnd - Contact Us</title> <h1>Contact Us!</h1><h3>Name: Arlen</h3><br><h3>Last Name: Haghighat Jou</h3><br><h3>Phone Number: </h3><a href='+77026520094'><h3>+77026520094</h3></a>"

# Blog Route
@app.route('/home/blog')
def blog():
    return render_template('blog.html')
    # return "<title>Arlen's BackEnd - Blog</title> <h1>Blog</h1><h3>Yes.</h3><br>"

# Test Route
@app.route('/test')
def test():
    return render_template('test.html')
    # return "<title>Arlen's BackEnd - Blog</title> <h1>Blog</h1><h3>Yes.</h3><br>"

# Schedule Route
@app.route('/home/schedule')
def schedule():
    return render_template('schedule.html')
    # return "<title>Arlen's BackEnd - Blog</title> <h1>Blog</h1><h3>Yes.</h3><br>"

# Form Route
@app.route('/home/form')
def form():
    user = {
        "name": "Arlen",
        "age": "11",
        "status": "Pre-Teen"
    }
    return render_template('form.html', user=user)
    # return "<title>Arlen's BackEnd - Blog</title> <h1>Blog</h1><h3>Yes.</h3><br>"

@app.route('/home/base')
def base():
    return render_template('base.html')
    # return "<title>Arlen's BackEnd - Blog</title> <h1>Blog</h1><h3>Yes.</h3><br>"

@app.route('/home/image-preview')
def image_preview():
    return render_template('preview.html')
    # return "<title>Arlen's BackEnd - Blog</title> <h1>Blog</h1><h3>Yes.</h3><br>"

@app.route('/home/profile')
def profile():
    user = {
        "email":"arlenjou336@gmail.com",
        "name": "Arlen",
        "username": "Arl#8192",
        "date": "17.01.2012"
    }
    return render_template('profile.html', user=user)
    # return "<title>Arlen's BackEnd - Blog</title> <h1>Blog</h1><h3>Yes.</h3><br>"

# Error 404 Route
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error-404.html'), 404

# Run App
if __name__ == "__main__":
    app.run("0.0.0.0", 80, True)