from flask import Flask
app = Flask(__name__)

app.debug = True

@app.route('/hello/<name>')
def hello_name(name):
  return 'Hello %s!' % name

def Bye():
    return 'Goodbye'
app.add_url_rule('/','bye',Bye)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d'% postID

@app.route('/rev/<float:revNo>/')
def revision(revNo):
    return 'Revision Number %f' % revNo

if __name__ == '__main__':
   app.run(debug = True)
