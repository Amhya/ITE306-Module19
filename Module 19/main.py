from flask import Flask,redirect,request,url_for,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("LogIn.html")
@app.route("/success/<name>")
def success(name):
    return "Welcome %s" %name
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form['user']
        return redirect(url_for('success',name=user))
    else:
        user=request.args.get('user')
        return redirect(url_for('success',name=user))


if __name__=="__main__":
    app.run()