import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory,Response, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/classifyresult', methods=['POST'])
def classify():
   file = request.files['file']

   if file:
       file_content = file.read()

       #TODO: Classify Content and return Result Content as CSV FIle

       print('Request for classification received as file name=%s' % file.filename)
       return Response(file_content,mimetype='text/csv')
   else:
       print('Request for classification received without file -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
