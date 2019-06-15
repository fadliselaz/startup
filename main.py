from flask import Flask, render_template, url_for, request, flash, redirect
import os

app = Flask(__name__)
app.secret_key = "fadliselaz"

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":

        us = request.form["username"]
        ps = request.form["password"]
        suc = True
        if us == "fadliselaz" and ps == "fadliselaz13":
            print(us +" "+ ps)
            
            return render_template("index.html", us=us, ps=ps, suc=suc)
          
            
        else:
            print("gagal masuk")
            
            return render_template("login.html", msg=True)

    return render_template("login.html")

  
def gagal():
    return render_template("login.html")


@app.route('/shutdown', methods=["POST", "GET"])
def shutDown():

    os.system("shutdown /s")



@app.route('/exit', methods=["POST","GET"])
def exit():
    os.system("start explorer.exe")
    os.system("taskkill /F /IM chrome* /T")
    os.system("taskkill /IM start_flask.exe")
    os.system("taskkill /IM cmd.exe")







if __name__ == "__main__":
    app.run(debug=True, port=3000)

