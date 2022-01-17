from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key='8675309DMX'

@app.route('/')         
def index():
    session['count']+=1
    return render_template("index.html")
@app.route('/count', methods=['POST'])
def count():
    session['count']+=1
    return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
    session['count']=0
    return redirect('/')
if __name__=="__main__":   
    app.run(debug=True)    