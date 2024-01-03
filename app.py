from flask import Flask, render_template,request,redirect

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '<h1>Hello world</h1>'

@app.route('/dologin', methods=['POST'])
def dologin():
    username = request.form['uname']
    password = request.form['psw']
    print(username)
    print(password)
    if username == "suman" and password=="suman123":
        return redirect("/home")
    else:
        return redirect("/dologin")
    

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/login')
def login():
    return render_template("pages/login.html")

@app.route('/register')
def register():
    return render_template("pages/register.html")

@app.route('/forget_password')
def forget_password():
    return render_template("pages/forget_password.html")
# @app.route('/doSignup',methods=['GET','POST'])
# def doSignup():
#     return render_template("signup.html")

# @app.route('/home',methods=['GET','POST'])
# def goHome():
#     return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
