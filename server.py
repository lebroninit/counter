from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form



@app.route('/')
def index():
    if 'amount' in session:
        session["amount"] +=1
    else:
        session["amount"] = 1


    return render_template("index.html", amount=session["amount"])

@app.route("/destroy_session")
def show_user():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)