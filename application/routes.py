from application import app
from flask import render_template, request
from application.models import Contact


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/create", methods=['GET','POST'] )
def create_contact():
    print(request.form)
    if request.method == 'GET':
        return render_template("create_contact.html")
    else:
        name = request.form.get('name')
        address = request.form.get('address')
        ph_num = request.form.get('ph_num')
        email = request.form.get('email')
        
        contact = Contact(name=name, address=address, ph_num=ph_num, email=email)
        contact.save()
        return render_template("index.html")

