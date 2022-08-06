from flask import Flask,render_template, request
import re
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("task1.html")

@app.route('/Match')
def mat():
    test_str=request.args['test']
    regex=request.args['reg']
    match = re.finditer(regex, test_str, re.MULTILINE)
    count=0
    for matchNum in match:
        count+=1
    if count==0:
        return("No match found")
    else:
        return("{count} matche(s) found!!".format(count=count))

if __name__=='__main__':
    app.run()