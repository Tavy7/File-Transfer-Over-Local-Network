#Python 3.7.4
#from werkzeug import secure_filename
from flask import Flask
from flask import render_template as rt
from flask import request, redirect, send_from_directory
from static.python.user import User, getId, saveUsers, loadUsers
import socket
import os

app = Flask(__name__)
users = loadUsers()

host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)

@app.route('/')
def home():
    # fac redirect prin javascript catre /<user>
    return rt('home.html')

@app.route('/<username>')
def userHome(username):
    ok = 0
    for user in users:
        if user.name == username:
            ok = 1
    
    if ok == 0:
        users.append(User(username))
        saveUsers(users)
    
    return rt('home.html')

@app.route('/uploads/')
def uploads():
    # fac redirect prin javascript catre uploads/<user>
    return rt('uploads.html')

@app.route('/uploads/<user>', methods=['GET', 'POST'])
def upload(user):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return rt('uploads.html')

        uploadFile = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if uploadFile.filename == '':
            print(str(request.url))
        
        if uploadFile:
            # get user id
            id = getId(user, users)

            if id == -1:
                return '404 Not found!'

            #filename = secure_filename(uploadFile.filename)
            uploadFile.save("uploaded-files/" + str(id) + "/" + str(uploadFile.filename))
            return redirect('/')
    
    return rt('uploads.html')

# link de download
@app.route('/uploaded-files/<int:user_id>/redirect')
def uploaded_files(user_id):
    fisiere = os.listdir('uploaded-files/' + str(user_id) + '/')
    return rt('uploaded_files.html', result=fisiere)

# redirect catre link-ul care contine id-ul 
@app.route('/uploaded-files/<username>')
def user_files(username):
    user_id = getId(username, users)
    return redirect('/uploaded-files/'+ str(user_id) + '/redirect')

# redirect prin javacript catre /username
@app.route('/uploaded-files')
def upload_main():
    return rt('uploaded_files.html')

# downloandeaza fisierul filename
@app.route('/uploaded-files/<int:user_id>/<filename>', methods=['GET', 'POST'])
def download(user_id, filename):   
    return send_from_directory(directory='uploaded-files/' + str(user_id) + '/', filename=filename, as_attachment=True)

@app.route('/ghe')
def datarstabinee():
    return '<iframe width="560" height="315" src="https://www.youtube.com/embed/-VBnSaKLe84" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>' * 6


app.debug = True
ip = '192.168.1.107'
ip = '0.0.0.0'

app.run(host=ip, port=5000)