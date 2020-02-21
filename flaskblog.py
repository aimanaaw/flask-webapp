from flask import Flask, render_template
app = Flask(__name__)


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