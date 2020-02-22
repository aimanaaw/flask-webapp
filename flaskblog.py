from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config[('SECRET_KEY')] = '9efff572d7b906f3d63a3880f73f7619'
# go into the python repl and import secrets then generate a secret key


posts = [
  {
    'author': 'Jane Doe',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'April 21, 2018'
  }
]

@app.route('/')
@app.route('/home')
def home():
  # by adding additional arguments in the return render_template, we can pass additional data to the render file
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
    app.run(debug=True)