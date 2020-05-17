from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/works')
def works():
    return render_template('works.html')


@app.route('/about.me')
def about_me():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


# @app.route('/components')
# def components():
#     return render_template('components.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return render_template('thankyou.html')
            # return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong... Try again!'


# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'{email}|{subject}|{message}\n')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='', encoding='utf-8') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter='|',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
