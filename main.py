from flask import Flask, render_template, request, make_response, session, redirect, url_for
import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="database"
# )
mydb = mysql.connector.connect(
  host="db4free.net",
  user="pr_gram123",
  password="Y_etDisDude$12",
  database="pr_gram123"
)

print(mydb)

mycursor = mydb.cursor()
app = Flask(__name__)

@app.route("/")
def registerpage():
    return render_template("register.html")

@app.route("/registeraccount", methods=["POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        address = request.form["address"]
        city = request.form["address"]
        postalcode = request.form["postalcode"]
        country = request.form["country"]

        sql = "INSERT INTO persons (LastName, FirstName, Address, City, Postal_code, Country, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (lastname, firstname, address, city, postalcode, country, username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("register.html", status="Success")
    
@app.route("/usertable")
def usertable():
    mycursor.execute("SELECT * FROM persons")

    myresult = mycursor.fetchall()
    print(myresult)
    return render_template("table.html", myresults = myresult)

@app.route("/updateinformationpage")
def updateinfopage():
    global userid
    userid = request.args.get('id')
    sql = "SELECT * FROM persons WHERE PersonID = %s"
    where = (userid, )
    mycursor.execute(sql, where)
    myresult = mycursor.fetchone()
    return render_template("updateinfo.html", userid=userid, myresult = myresult)

@app.route("/updateinfo", methods=["POST"])
def updateinfo():
    if request.method == "POST":
        lastname = request.form["lastname"]
        firstname = request.form["firstname"]
        address = request.form["address"]
        city = request.form["address"]
        postalcode = request.form["postalcode"]
        country = request.form["country"]
        username = request.form["username"]
        password = request.form["password"]
        sql = "UPDATE persons SET LastName = %s, FirstName = %s, Address = %s, City = %s, Postal_code = %s, Country = %s, Username = %s, Password = %s WHERE PersonID = %s"
        val = (lastname, firstname, address, city, postalcode, country, username, password, userid)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("updateinfo.html", status="Success", myresult = 0)

@app.route("/election")
def showpage():
    return render_template("election.html")

@app.route("/electiontable")
def electiontable():
    mycursor.execute("SELECT * FROM election")

    myresult = mycursor.fetchall()
    return render_template("electiontable.html", myresult=False)

@app.route("/checkelection")
def checkelection():
    id = request.args.get("id")
    sql = f'SELECT * FROM election WHERE idNumber = "{id}";'
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    print(myresult)
    return render_template("electiontable.html", myresult=myresult)

@app.route("/checkinfo")
def checkinfo():
    idNumber = request.args.get("idNumber")
    idNumber2 = request.args.get("idNumber2")
    firstName = request.args.get("firstName")
    lastName = request.args.get("lastName")
    birthday = request.args.get("birthday")
    birthmonth = request.args.get("birthmonth")
    birthyear = request.args.get("birthyear")
    houseNumber = request.args.get("houseNumber")
    sql = "INSERT INTO election (idNumber, idNumber2, firstName, lastName, birthday, birthmonth, birthyear, houseNumber) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (idNumber, idNumber2, firstName, lastName, birthday, birthmonth, birthyear, houseNumber)
    mycursor.execute(sql, val)
    mydb.commit()
    print(idNumber, idNumber2, firstName, lastName, birthday, birthmonth, birthyear, houseNumber)
    return render_template("election.html")


@app.route("/deleteuser")
def deleteuserpage():
    userid = request.args.get("id")
    sql = "DELETE FROM persons WHERE PersonID = %s"
    mycursor.execute(sql, (userid,))
    mydb.commit()
    return redirect(url_for("usertable"))

if __name__ == "__main__":
    app.run()