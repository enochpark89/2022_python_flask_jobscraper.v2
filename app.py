from flask import Flask, render_template, request, redirect
from get_job import get_job
import os

app = Flask(__name__)

@app.route('/')
def home(): 
    word = request.args.get('jobname')
    if (word):
        return redirect(f"/{word}")
    
    return render_template("search.html")

# @app.route('/<keyword>')
# def found(keyword):
#     jobs = get_job(keyword)
#     return render_template("result.html", jobs=jobs)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)