
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def member():
    return render_template('Register.html')

if __name__ == "__main__":
    app.run(debug=True)