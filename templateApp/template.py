from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hey/<user>')
def hello(user):
   return render_template('hey.html', name = user)

if __name__ == '__main__':
   app.run(debug = True)