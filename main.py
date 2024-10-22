from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/excursion')
def excursion():
    return render_template('excursion.html')


@app.route('/school')
def school():
    return render_template('school.html')


@app.route('/student')
def student():
    return render_template('student.html')


if __name__ == '__main__':
    app.run()

