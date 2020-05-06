from flask import Flask, render_template, request, session
from flask_session import Session

app=Flask(__name__)

app.config["SESSION_PERMINENT"] = False
app.secret_key = 'super secret key'
app.config["SESSION_TYPE"]="filesystem"

Session(app)
#@app.route("/")
#def index():
#    names=["Keke","Alice"]
#    font="cursive"
#    return render_template("index.html", names=names, font=font)
notes=[]
font="Arial"
color="#c94c4c"
lan="index.html"
@app.route("/", methods=['POST','GET'])
def font():
    global font
    global color
    global lan
    if request.form.get("button") is not None:
        font=request.form.get("button")
    if request.form.get("color") is not None:
        color=request.form.get("color")
    if request.form.get("LAN")=="ENG":
        lan="index.html"
    elif request.form.get("LAN")=="CHI":
        lan="index_chi.html"
    return render_template(lan,font=font,color=color)
    #return redirect(url_for('font'),font=font)

    #@app.route("/", methods=['POST','GET'])
    #def color():
    #    global color
    #    color=request.form.get("color")
    #    return render_template("index.html",font=font,color=color)

@app.route("/note", methods=["POST","GET"])
def note():
    global font
    if session.get("notes") is None:
        session["notes"]=[]
    if request.method=="POST":
        note=request.form.get("note")
        # notes.append(note)
        session["notes"].append(note)
    return render_template("note.html", notes=session["notes"],font=font,color=color)


@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/hello", methods=["POST","GET"])
def hello():
    if request.method=="GET":
        return index() # "Nothing has been submitted yet, please go to the home page: "
    else:
        name=request.form.get("name")
        return render_template("hello.html", names=name)

#session.init_app(app)
app.run(debug=True, use_reloader=False)
