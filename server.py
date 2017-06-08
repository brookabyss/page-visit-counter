from flask import Flask, render_template, session,redirect
app=Flask(__name__)
app.secret_key="234"
@app.route('/')
def index():
    if type(session['count'])!=int:
        session['count']=1
    else:
        session['count']+=1
    return render_template('index.html')
@app.route('/add2')
def add_2():
    session['count']+=1
    return redirect('/')
@app.route('/reset')
def reset():
    session['count']=0
    return redirect('/')
app.run(debug=True)
