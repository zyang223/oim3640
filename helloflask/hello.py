from flask import Flask

app = Flask(__name__)

@app.route("/") # if website domain is www.abc.come, https:// www.abc.com/ will trigger this function
@app.route("/hello/<name>")
def hello_world(name=None):
    if name:
        return f"hello,{name}!</h1><p> I am excited to learn Flask.</p>"
    return "HELLO WORLD"

@app.route("/square/")
@app.route("/square/<number>")
def square(number):
    if number:
        return str(int(number) ** 2)
    return("you need to provide a number")


if __name__=="__main__":
    app.run(debug=True)