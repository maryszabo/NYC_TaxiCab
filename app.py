# CIS4301 Fall 2022
# By Mary Szabo
# referenced: https://pythonbasics.org/flask-template-data/ 
# https://code.visualstudio.com/docs/python/tutorial-flask 

# this site
from flask import Flask,render_template,request
 
app = Flask(__name__)
 
@app.route('/')
def query1filters():
    return render_template('query1filters.html')

@app.route('/query2filters')
def query2filters():
    return render_template('query2filters.html')
 
@app.route('results/', methods = ['POST', 'GET'])
def results():
    if request.method == 'POST' :
      results = request.form 
      #return render_template("results.html", results = results)
      start_date = request.form.get("sdate")
      end_date = request.form.get("edate")
      vendor = request.form.get("vendor")
      min_passengers = request.form.get("minPass")
      max_passengers = request.form.get("maxPass")
    return render_template("results.html", results = results)

  #if request.method == 'GET':
  #    return f"The URL /results is accessed directly. Try going to '/form' to submit form"
  #if request.method == 'POST':
   #   query1filters_results = request.form
   #   return render_template('results.html',query1filters_results = query1filters_results)


#app.run(host='localhost', port=5000) 
 
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