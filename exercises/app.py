from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    players = ["cristisno ronaldo" , "messi" , "Iker casillas"]
    return render_template(
        "index.html", 
        players = players,
        likes_same_sports = False)


if __name__ == '__main__':
   app.run(debug = True)