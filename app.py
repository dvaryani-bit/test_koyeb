from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
@app.route("/")
def home():
    #### testing if return render_template works
    return render_template('index.html')

if __name__ == "__main__":
    print("hello")
    json_file = 'test.json'
    with open(json_file, 'r') as file:
        data = json.load(file)
        print(data)
    app.run(port = 5000)
    #### testing if opening a file works
