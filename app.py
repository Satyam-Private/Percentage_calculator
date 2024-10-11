from flask import Flask , render_template , url_for , redirect ,request 
app = Flask(__name__)
@app.route('/')
def welcome():
    return redirect('/result')

@app.route('/success/<int:score>')
def success(score):
    return f" Congratulations!!! you are passed with {score} marks"

@app.route('/failure/<int:score>')
def failure(score):
    return f"You are failed with {score} marks"




@app.route('/result' , methods = ['POST' , 'GET'])
def result():
    if request.method == 'POST':
        total_marks = 0
        maths = float(request.form['mhs'])
        science = float(request.form['sc'])
        c = float(request.form['cl'])
        python = float(request.form['py'])
        total_marks = (maths + science + c + python)/ 400
        percentage = total_marks  * 100
        if percentage > 35:
            return redirect(url_for('success' , score = percentage))
        else:
            return redirect(url_for('failure' , score = percentage))
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug = True)