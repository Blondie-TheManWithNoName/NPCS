from flask import Flask, redirect, url_for, request, render_template, flash
from config import *
import psycopg2

app = Flask(__name__)

def do_query(c, q, n=''):
    c.execute(q, n)


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/hairs", methods=["POST", "GET"])
def hairs():
    if request.method == "POST":

        # DELETE
        if request.form["submit"] == "delete":
            try:
                c.execute("DELETE FROM hairs WHERE hairFile='%s' AND color='%s';" % (request.args.get('hairFile'), request.args.get('color')))
                conn.commit()
                flash("Successfully deleted.")
            except psycopg2.IntegrityError as e:
                flash("An exception occurred: " + str(e)[0: str(e).index("»") + 1])
                # print("An exception occurred:", e)

        # UPDATE
        elif request.form["submit"] == "update":
            try:
                c.execute("UPDATE hairs SET hairFile='%s', color='%s' WHERE hairFile='%s' AND color='%s';" % (request.form["hairFile"], request.form["color"], request.args.get('hairFile'), request.args.get('color')))    
                conn.commit()
                flash("Successfully updated.")
            except Exception as e:
                conn.rollback()
                flash("An exception occurred: " + str(e)[0: str(e).index("»") + 1])
                # print("An exception occurred:", e)
       
        # INSERT
        else:
            try:
                c.execute("INSERT INTO faces VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (request.form["id"], request.form["mouthFile"], request.form["eyesFile"], request.form["noseFile"], request.form["earsFile"], request.form["hairFile"], request.form["color"]))   
                conn.commit()
                flash("Successfully inserted.")
            except psycopg2.IntegrityError as e:
                conn.rollback()
                flash("An exception occurred: " + str(e)[0: str(e).index("»") + 1])
                # print("An exception occurred:", e)

        return redirect(request.path,code=302)

    c.execute("SELECT * FROM hairs ORDER BY color")
    data = c.fetchall()
    return render_template("table_hairs.html", data=data)


@app.route("/faces", methods=["POST", "GET"])
def faces():
    if request.method == "POST":

        # DELETE
        if request.form["submit"] == "delete":
            try:
                c.execute("DELETE FROM faces WHERE id='%s';" % (request.args.get('id')))
                conn.commit()
                flash("Successfully deleted.")
            except psycopg2.IntegrityError as e:
                flash("An exception occurred: " + str(e)[0: str(e).index("»") + 1])
                # print("An exception occurred:", e)
        
        # UPDATE
        elif request.form["submit"] == "update":
            print("id", request.form["id"])
            try:
                c.execute("UPDATE faces SET id='%s', mouthFile='%s', eyesFile='%s', noseFile='%s', earsFile='%s', hairFile='%s', color='%s' WHERE id='%s';" % (request.form["id"], request.form["mouthFile"], request.form["eyesFile"], request.form["noseFile"], request.form["earsFile"], request.form["hairFile"], request.form["color"], request.args.get('id')))    
                conn.commit()
                flash("Successfully updated.")
            except Exception as e:
                conn.rollback()
                flash("An exception occurred: " + str(e)[0: str(e).index("»") + 1])
                # print("An exception occurred:", e)
       
        # INSERT
        else:
            try:
                print("mouth", request.form["mouthFile"])
                c.execute("INSERT INTO faces VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (request.form["id"], request.form["mouthFile"], request.form["eyesFile"], request.form["noseFile"], request.form["earsFile"], request.form["hairFile"], request.form["color"]))   
                conn.commit()
                flash("Successfully inserted.")
            except psycopg2.IntegrityError as e:
                conn.rollback()
                flash("An exception occurred: " + str(e)[0: str(e).index("»") + 1])
                # print("An exception occurred:", e)
        
        return redirect(request.path, code=302)

    c.execute("SELECT * FROM faces ORDER BY id")
    data = c.fetchall()
    return render_template("table_faces.html", data=data)



@app.route("/npcs", methods=["POST", "GET"])
def npcs():
    if request.method == "POST":

        # DELETE        
        if request.form["submit"] == "delete":
            try:
                c.execute("DELETE FROM npcs WHERE id='%s' AND namereg='%s';" % (request.args.get('id'), request.args.get('namereg')))
                conn.commit()
                flash("Successfully deleted.")
            except psycopg2.IntegrityError as e:
                flash("An exception occurred: " + str(e)[0: str(e).index("»") + 1])
                # print("An exception occurred:", e)

        # UPDATE
        elif request.form["submit"] == "update":
            try:
                print("UPDATE")
                print("REQUEST:", request.args.get('id'))
                print("REQUEST:", request.args.get('namereg'))
                c.execute("UPDATE npcs SET name='%s', sex='%s', color='%s', height='%s', health='%s', id='%s', namereg='%s' WHERE id='%s' AND namereg='%s';" % (request.form["name"], request.form["sex"], request.form["color"], request.form["height"], request.form["health"], request.form["id"], request.form["namereg"], request.args.get('id'), request.args.get('namereg')))    
                conn.commit()
                flash("Successfully updated.")
            except Exception as e:
                conn.rollback()
                flash("An exception occurred: " + str(e)[0: str(e).index("»") + 1])
                # print("An exception occurred:", e)
        
        # INSERT        
        else:
            try:
                c.execute("INSERT INTO npcs VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (request.form["name"], request.form["sex"], request.form["color"], request.form["height"], request.form["health"], request.form["id"], request.form["namereg"]))
                conn.commit()
                flash("Successfully inserted.")
            except psycopg2.IntegrityError as e:
                conn.rollback()
                flash("An exception occurred: " + str(e)[0: str(e).index("»") + 1])
                # print("An exception occurred:", e)
        
        return redirect(request.path,code=302)

    c.execute("SELECT * FROM npcs ORDER BY id")
    data = c.fetchall()
    return render_template("table_npcs.html", data=data)



@app.route("/regions", methods=["POST", "GET"])
def regions():
    if request.method == "POST":
       
       # DELETE
        if request.form["submit"] == "delete":
            try:
                c.execute("DELETE FROM regions WHERE nameReg='%s'" % (request.args.get('nameReg')))    
                conn.commit()
                flash("Successfully deleted.")
            except Exception as e:
                conn.rollback()
                flash("An exception occurred: " + str(e)[0: str(e).index("»") + 1])
                # print("An exception occurred:", e)
        
       # UPDATE
        elif request.form["submit"] == "update":
            try:
                c.execute("UPDATE regions SET nameReg='%s', weather='%s' WHERE nameReg='%s'" % (request.form["nameReg"], request.form["weather"], request.args.get('nameReg')))    
                conn.commit()
                flash("Successfully updated.")
            except Exception as e:
                conn.rollback()
                flash("An exception occurred: " + str(e)[0: str(e).index("»") + 1])
                # print("An exception occurred:", e)
       
       # CREATE
        else:
            try:
                c.execute("INSERT INTO regions VALUES ('%s', '%s');" % (request.form["nameReg"], request.form["weather"]))   
                conn.commit()
                flash("Successfully inserted.")
            except psycopg2.IntegrityError as e:
                conn.rollback()
                flash("An exception occurred: " + str(e)[0: str(e).index("»") + 1])
                # print("An exception occurred:", e)
        
        return redirect(request.path,code=302)

    c.execute("SELECT * FROM regions ORDER BY nameReg")
    data = c.fetchall()
    return render_template("table_regions.html", data=data)


if __name__ == "__main__":
    app.secret_key = 'key'
    app.run()