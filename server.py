from flask import Flask, render_template
import requests

app = Flask(__name__)
URL='https://api.npoint.io/6f71df0f5cf0948ffc86'
response=requests.get(URL)
all_post=response.json()

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html',all_post = all_post)

@app.route('/contact.html')
def contacts():
    return render_template('contact.html')

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




if __name__=="__main__":
    app.run(debug=True)


