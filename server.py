from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key='8675309DMX'

@app.route('/')         
def index():
    session['count']+=1
    return render_template("index.html")
@app.route('/count', methods=['POST'])
def count():
    if 'increaseCount' in session:
        print('key exists!')
    else:
        print("key 'increaseCount' does NOT exist")

if __name__=="__main__":   
    app.run(debug=True)    