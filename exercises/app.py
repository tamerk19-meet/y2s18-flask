from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    x="I'd rather die"
    return(x)


@app.route('/fs')
def favourite_sport():
    return render_template("index.html")
#################################
if __name__ == '__main__':
   app.run(debug = True)