from flask import Flask, render_template, request, redirect
# from flask_table import Table, Col
import pandas as pd
import username
import graph_helper as gh
import change_colour  as cc

########################
rowdy_csv = "rowdy_data.csv"

ill_activities_csv = "ill_activities.csv"

feedback_csv = "feedback.csv"

auth_csv = "auth.csv"

mem_details_csv = "mem_details.csv"

crime_areas_csv = "crime_areas.csv"

####################

def add_helper(sample):
    temp = []
    for i in sample.columns:
        temp.append(input(i))
    sample = sample.append(pd.Series(temp, index = sample.columns, name = len(sample)+1), ignore_index = False)
    return sample


def del_helper(data, idn):
    data = data.drop(index = idn, reset_index = True)
    return data

#########################

app = Flask(__name__)
csv_path = "I:/frontend/temp.csv"


@app.route('/')
def home():
    return render_template('index.html')
# def static():
#     return render_template("../static/img/sky.png")


@app.route("/signin/si/crimemap")
def crimemap():
    x = {1:0.75, 2:0.8, 3:0.9, 4:0.9}
    cc.lap(x)
    return render_template("crimemap.html")

#------------SIGIN----------
@app.route("/signin/")
def signin():
    return render_template("signin.html")

@app.route("/signin/", methods=["POST"])
def signin_post():
    uname = request.form['Username']
    pwde = request.form["Password"]
    auth = pd.read_csv(auth_csv)
    ind = (auth.index[auth["userid"] == uname].tolist())
    if (auth["pwd"].values[ind][0] == pwde):
        if uname.split("_")[1] == "ASI":
            text = "si"
            return render_template("si.html", value = text)
        elif uname.split("_")[1] == "CON":
            text = "beatconstable"
            return render_template("beatconstable.html", value = text)
    else:
        return render_template("signin.html")



#---------------SIGNIN/BS---------
@app.route("/signin/beatconstable")
def beatconstable():
    return render_template("beatconstable.html")


#-----------------SIGNIN/SI-------
@app.route("/signin/si")
def si():
    return render_template("si.html")




#----------------signin/si/beat1-------

# @app.route("/signin/si/beat1/")
# def beat1():
#     img_path = "/static/img/chart.png"   ##--->push
#     return render_template("beat1.html", user_image=img_path)

@app.route("/signin/si/beat1/",methods = ["GET"])
def beat1_post():
    beat = 3
    mem_details = pd.read_csv(mem_details_csv)
    tab = mem_details[mem_details["beat_number"].values == beat]
    img_path = gh.plotter(mem_details_csv, "beat_number", "beat1")
    print("this",  img_path)
    return render_template("beat1.html",tab=tab, user_image = "/"+img_path)


#----------------signin/si/beat2-------
# @app.route("/signin/si/beat2")
# def beat2():
#     img_path = "/static/img/chart.png"   ##--->push
#     return render_template("beat2.html", user_image=img_path)


@app.route("/signin/si/beat2/",methods = ["GET"])
def beat2_post():
    beat = 3
    mem_details = pd.read_csv(mem_details_csv)
    tab = mem_details[mem_details["beat_number"].values == beat]
    img_path = gh.plotter(mem_details_csv, "beat_number", "beat2")
    return render_template("beat2.html",tab=tab, user_image = "/" + img_path)


#----------------signin/si/beat3-------
# @app.route("/signin/si/beat3")
# def beat3():
#     img_path = "/static/img/chart.png"   ##--->push
#     return render_template("beat3.html", user_image=img_path)


@app.route("/signin/si/beat3/",methods = ["GET"])
def beat3_post():
    beat = 3
    mem_details = pd.read_csv(mem_details_csv)
    tab = mem_details[mem_details["beat_number"].values == beat]
    img_path = gh.plotter(mem_details_csv, "beat_number", "beat3")
    return render_template("beat3.html",tab=tab, user_image = "/"+img_path)

#----------------signin/si/beat4-------
# @app.route("/signin/si/beat4")
# def beat4():
#     img_path = "/static/img/chart.png"   ##--->push
#     return render_template("beat4.html", user_image=img_path)


@app.route("/signin/si/beat4/",methods = ["GET"])
def beat4_post():
    beat = 3
    mem_details = pd.read_csv(mem_details_csv)
    print(mem_details)
    tab = mem_details[mem_details["beat_number"].values == beat]
    # print("#######",tab[0])
    print(tab.values[0])
    img_path = gh.plotter(mem_details_csv, "beat_number", "beat4")
    print("iiimmmmgggg", img_path)
    return render_template("beat4.html",tab=tab, user_image = "/"+img_path)

#----------------SIGNIN/SI/ADDORDEL----------
# @app.route("/signin/si/addordel/")
# def addordel():
#     return render_template("addordel.html")


@app.route("/signin/si/addordel/",methods = ["GET", "POST"])
def addordel_post():
    auth = pd.read_csv(auth_csv)
    if request.method == "GET":
        print("----------entered-------------")
        tab=auth.values
        print(tab)
        return render_template("addordel.html", tab=tab)
    else:
        print("--------POST----------")
        id = request.form["id"]
        ind = (auth.index[auth["userid"] == id][0])
        auth = auth.drop(ind)
        return render_template("si.html")




#-----------------database----------
@app.route("/signin/si/view_db")
def view_db():
    with open("templates/auth.html", "w") as f:
        auth = pd.read_csv(auth_csv)
        f.write(auth.to_html())
    with open("templates/crime_areas.html", "w") as f:
        crime_areas = pd.read_csv(crime_areas_csv)
        f.write(crime_areas.to_html())
    with open("templates/feedback.html", "w") as f:
        feedback = pd.read_csv(feedback_csv)
        f.write(feedback.to_html())
    with open("templates/ill_activities.html", "w") as f:
        ill_activities = pd.read_csv(ill_activities_csv)
        f.write(ill_activities.to_html())
    with open("templates/rowdy_data.html", "w") as f:
        rowdy_data = pd.read_csv(rowdy_csv)
        f.write(rowdy_data.to_html())
    with open("templates/mem_details.html", "w") as f:
        mem_details = pd.read_csv(mem_details_csv)
        f.write(mem_details.to_html())
    return render_template("view_db.html")

@app.route("/signin/si/view_db/rowdy_data")
def rowdy_data_html():
    return render_template("rowdy_data.html")

@app.route("/signin/si/view_db/auth_data")
def auth_data_html():
    return render_template("auth.html")

@app.route("/signin/si/view_db/crime_data")
def crime_data_html():
    return render_template("crime_areas.html")

@app.route("/signin/si/view_db/feedback_data")
def feedback_data_html():
    return render_template("feedback.html")

@app.route("/signin/si/view_db/ill_activities_data")
def ill_activities_data_html():
    return render_template("ill_activities.html")

@app.route("/signin/si/view_db/mem_details_data")
def mem_details_data_html():
    return render_template("mem_details.html")


#---------------signin/bs/--------
@app.route("/signin/beatconstable/rowdychecking")
def rowdychecking():
    return render_template("rowdychecking.html")

@app.route("/signin/beatconstable/rowdychecking", methods = ["POST"])
def rowdychecking_post():
    name = request.form['Name']
    add = request.form["Address"]
    act = request.form['Suspicious_Activity']
    occ = request.form["Current_Occupation"]
    bmr = request.form["Beat_Memebers_remarks"]
    rowdy = pd.read_csv(rowdy_csv)
    rowdy = rowdy.append(pd.DataFrame({"name": name, "address": add, "suspicious_activity":act, "occupation":occ, "remark":bmr}, index = [len(rowdy)]))
    rowdy.to_csv(rowdy_csv, index = False)
    return render_template("beatconstable.html")


#--------------signin/bs/illegalcriminalactivities---------
@app.route("/signin/beatconstable/illegalcriminalactivities")
def illegalcriminalactivities():
    return render_template("illegalcriminalactivities.html")


@app.route("/signin/beatconstable/illegalcriminalactivities", methods = ["POST"])
def illegalcriminalactivities_post():
    name = request.form['name']
    add = request.form["address"]
    off = request.form["offence"]
    ill_activities = pd.read_csv(ill_activities_csv)
    ill_activities = ill_activities.append(pd.DataFrame({"name": name, "address": add, "offense":off}, index = [len(ill_activities)]))
    ill_activities.to_csv(ill_activities_csv, index = False)
    return render_template("beatconstable.html")


#--------------crime_prone_areas---------
@app.route("/signin/beatconstable/crimeproneareas")
def crimeproneareas():
    return render_template("crimeproneareas.html")

@app.route("/signin/beatconstable/crimeproneareas", methods = ["POST"])
def crimeproneareas_post():
    name = request.form['name']
    add = request.form["address"]
    event = request.form["events"]
    crime_areas = pd.read_csv(crime_areas_csv)
    crime_areas = crime_areas.append(pd.DataFrame({"name": name, "address": add, "events": event}, index = [len(crime_areas)]))
    crime_areas.to_csv(crime_areas_csv, index = False)
    return render_template("beatconstable.html")

#-----------------map-------------
@app.route("/signin/beatconstable/map_api")
def map_api():
    return render_template("map_api.html")


#---------------signin/bs/beatmemberfeedback---------------
@app.route("/signin/beatconstable/beatmemberfeedback")
def beatmemberfeedback():
    return render_template("beatmemberfeedback.html")

@app.route("/signin/beatconstable/beatmemberfeedback", methods = ["POST"])
def beatmemberfeedback_post():
    name = request.form['name']
    comm = request.form["comments"]
    feedback = pd.read_csv(feedback_csv)
    feedback = feedback.append(pd.DataFrame({"name": name, "comments": comm}, index = [len(feedback)]))
    feedback.to_csv(feedback_csv, index = False)
    return render_template("beatconstable.html")




if __name__ == '__main__':
    app.run(host = "127.0.0.1", port = "8028", debug = True)
