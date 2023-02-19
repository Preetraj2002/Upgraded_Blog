from flask import Flask, render_template,request
import requests
import smtplib
import os

app = Flask(__name__)
URL='https://api.npoint.io/6f71df0f5cf0948ffc86'
response=requests.get(URL)
all_post=response.json()

def send_mail(name,email,phno,mssg):
    sender = os.environ["SMTP_sender"]
    receiver = os.environ["SMTP_receiver"]
    pswd = os.environ["SMTP_pass"]
    port_no = 587
    smtp_url = "smtp.gmail.com"

    mail = smtplib.SMTP(smtp_url, port_no)
    mail.ehlo()
    mail.starttls()
    mail.login(sender, pswd)

    header = f"To:{receiver}\nSubject:Message\n\n"
    content = f"Name:{name}\n" \
              f"Email:{email}\n" \
              f"Ph.no.:{phno}\n" \
              f"Message:{mssg} "
    message = header + content
    mail.sendmail(sender, receiver, message)
    mail.close()


@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html',all_post = all_post)


@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route("/post/<int:index>")
def show_post(index):
    requested_post=None
    for post in all_post:
        if post['id'] == index:
            requested_post=post
    return render_template('post.html',post=requested_post)

@app.route('/contact.html',methods=["POST","GET"])
def contact():
    error = None
    if request.method=="GET":
        return render_template('contact.html')
    elif request.method == "POST":
        name=request.form['name']
        email=request.form['email']
        phno=request.form['phone']
        message=request.form['message']
        send_mail(name,email,phno,message)
        return render_template('contact.html',sent=True)
    return "error"

if __name__=="__main__":
    app.run(debug=True)