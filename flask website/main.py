# import the nessecary pieces from Flask
from flask import Flask,render_template, request,jsonify,Response
import os
PEOPLE_FOLDER = os.path.join('static', 'images')

#Create the app object that will route our calls
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
app.config['NAME'] = ""
app.config['COUNT'] = 0
# Add a single endpoint that we can use for testing
@app.route('/')
def start():
    return render_template('start.html')
@app.route('/q1')
def q1():
    app.config['NAME'] = request.args.get("fname")
    return render_template('q1.html')
@app.route('/q2', methods = ['POST'])
def q2():
    option = request.form['option']
    option = int(option)
    app.config['COUNT'] = app.config['COUNT'] + option
    return render_template('q2.html')
@app.route('/q3', methods = ['POST'])
def q3():
    option = request.form['option']
    option = int(option)
    app.config['COUNT'] = app.config['COUNT'] + option
    return render_template('q3.html')
@app.route('/q4', methods = ['POST'])
def q4():
    option = request.form['option']
    option = int(option)
    app.config['COUNT'] = app.config['COUNT'] + option
    return render_template('q5.html')
@app.route('/q5', methods = ['POST'])
def q5():
    option = request.form['option']
    option = int(option)
    app.config['COUNT'] = app.config['COUNT'] + option
    return render_template('q5.html')
@app.route('/q6', methods = ['POST'])
def q6():
    option = request.form['option']
    option = int(option)
    app.config['COUNT'] = app.config['COUNT'] + option
    return render_template('q6.html')
@app.route('/q7', methods = ['POST'])
def q7():
    option = request.form['option']
    option = int(option)
    app.config['COUNT'] = app.config['COUNT'] + option
    return render_template('q7.html')
@app.route('/q8', methods = ['POST'])
def q8():
    option = request.form['option']
    option = int(option)
    app.config['COUNT'] = app.config['COUNT'] + option
    return render_template('q8.html')
@app.route('/q9', methods = ['POST'])
def q9():
    option = request.form['option']
    option = int(option)
    app.config['COUNT'] = app.config['COUNT'] + option
    return render_template('q9.html')
@app.route('/q10', methods = ['POST'])
def q10():
    option = request.form['option']
    option = int(option)
    app.config['COUNT'] = app.config['COUNT'] + option
    return render_template('q10.html')
@app.route('/result', methods = ['POST'])
def result():
    option = request.form['option']
    option = int(option)
    app.config['COUNT'] = app.config['COUNT'] + option
    val = app.config['COUNT']
    character = ""
    if val >= 1 and val <= 8:
        character = "ross"
    elif val >=9 and val <= 16:
        character = "rachel"
    elif val >= 17 and val <= 24:
        character = "monica"
    elif val >= 25 and val <= 32:
        character = "chandler"
    elif val >= 33 and val <= 40:
        character = "joey"
    else:
        character = "phoebe"
    filename = character + ".jpg"
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return render_template('result.html', user_image = full_filename, user_name = app.config['NAME'], char_name = character)
#When run from command line, start the server
if __name__ == '__main__':
    app.run(debug = True)