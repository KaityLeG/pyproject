from flask import Flask, render_template, url_for, redirect

app= Flask(__name__)

@app.route("/")
def head():
    name= "Clarusway"
    return render_template('greet.html', name=name)

@app.route('/evens')
def evens():
    return render_template('evens.html')

@app.route('/list10')
def list10():
    return render_template('list10.html')

@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)

@app.route('/google')
def redirection():
    return redirect("https://www.google.com")

@app.route('/error')
def error():
    return f"<h1> Wrong Endpoint </h1>"

@app.route("/fuzz")
def fuzz():
    return redirect(url_for("error"))

@app.route("/pong/name")
def pong(name):
    return f"<h1> Pong {name}</h1>"

@app.route("/ping")
def ping():
    return redirect(url_for("pong", name="Kaity"))


if __name__=='__main__':
        app.run(host='0.0.0.0', port=3003, debug=False)
