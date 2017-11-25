from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
    dict = {'physics':93,'chemistry':87,'mathematics':98}
    return render_template('dict.html',result = dict)

if __name__ == '__main__':
    app.run(debug = True)