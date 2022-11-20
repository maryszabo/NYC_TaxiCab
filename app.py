# referenced: https://pythonbasics.org/flask-template-data/ 
# https://code.visualstudio.com/docs/python/tutorial-flask 
from flask import Flask,render_template,request
 
app = Flask(__name__)
 
@app.route('/query1filters')
def query1filters():
    return render_template('query1filters.html')

@app.route('/query2filters')
def query2filters():
    return render_template('query2filters.html')
 
@app.route('/results', methods = ['POST', 'GET'])
def results():
    if request.method == 'POST' :
      results = request.form 
      return render_template("results.html", results = results)
 
 
if __name__ == '__main__':
   app.run(debug = True)

"""
# referenced: https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/ 

# importing Flask and other modules
from flask import Flask, request, render_template 
import json
 
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/gfg', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       if "fname" in request.form: 
         first_name = request.form['fname']
       # getting input with name = lname in HTML form
       if "lname" in request.form:
         last_name = request.form['lname']
       #return "Your name is "+first_name + " " + last_name

       if first_name and last_name: 
         print("Your name is "+ first_name + " " + last_name)
    return render_template("query1filters.html")
 
if __name__=='__main__':
   app.run()
"""
