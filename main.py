import csv

from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data["name"]
        email = data['email']
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n {name}, {email}, {subject}, {message}")


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        name = data['name']
        email = data["email"]
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',')
        csv_writer.writerow([name, email, subject, message])


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == "POST":
        data = request.form.to_dict()
        user_name = data.get('name')
        write_to_csv(data)
        return render_template('thankyou.html', name=user_name)
    else:
        return "Something went wrong. Try again!"


if __name__ == "__main__":
    app.run(debug=True)
