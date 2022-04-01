from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'counter' #used to encrypt data




@app.route('/')
def index():
    
    if 'views' not in session:
      session['views'] = 0
    else:
        session['views'] += 1
    return render_template('index.html', count=session['views'])





if (__name__) == ('__main__'):
    app.run(debug=True)