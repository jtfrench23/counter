from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key='8675309DMX'

@app.route('/')         
def index():
    if 'visits' not in session:
        session['visits']=1
    else:
        session['visits']+=1
    if "count" not in session:
        session["count"] = 1
    else:
        session['count'] += 1
    return render_template("index.html")
@app.route('/count', methods=['POST'])
def count():
    session['count']+=1
    return redirect('/')
@app.route('/increase_amount',methods=['POST'])
def increase_count():
    amount=int(request.form['quantity'])
    session['count']+=amount-1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count']=0
    return redirect('/')

@app.route('/destroy_all')
def destroy_all():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    