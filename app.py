from flask import Flask, redirect, url_for, request, render_template, flash
from config import *
import psycopg2

app = Flask(__name__)

def do_query(c, q, n=''):
    c.execute(q, n)


def search(table_name):
    if request.form["search"] != '':
        try:
            c.execute("SELECT * FROM %s WHERE %s;" % (table_name, request.form["search"]))
            data = c.fetchall()
            flash("Successfully searched.")
            return render_template("table_" + table_name + ".html", data=data)
        except Exception as e:
            conn.rollback()
            errorMessage(e)

    return redirect(request.path,code=302)

def errorMessage(e):
    if "»" in str(e):
        flash("An exception occurred: " + str(e)[0: str(e).index("»") + 1])
    elif "LINE" in str(e):
        flash("An exception occurred: " + str(e)[0: str(e).index("LINE")])
    else:
        flash("An exception occurred: " + str(e))
    
    # print("An exception occurred:", e)


def getIndexInfo(query):
    _list = []
    for x in query:
        if "UNIQUE" in x[4]:
            _tuple = (x[4][x[4].index("INDEX") + 6:x[4].index("ON")], x[4][x[4].index("UNIQUE"):x[4].index("UNIQUE") + 6], x[4][x[4].index(".") + 1:x[4].index("USING")], x[4][x[4].index("USING") + 6:x[4].index("(") - 1], x[4][x[4].index("(") + 1:x[4].index(")")])
        else:
            _tuple = (x[4][x[4].index("INDEX") + 6:x[4].index("ON")], "", x[4][x[4].index(".") + 1:x[4].index("USING")], x[4][x[4].index("USING") + 6:x[4].index("(") - 1], x[4][x[4].index("(") + 1:x[4].index(")")])

        _list.append(_tuple)
    return _list

@app.route("/", methods=["POST", "GET"])
def home():
    data = None
    if request.method == "POST":
        c.execute(request.form["query"])
        data = c.fetchall()
    return render_template("index.html", data=data)


@app.route("/indexes", methods=["POST", "GET"])
def indexes():
    if request.method == "POST":

        # DELETE
        if request.form["submit"] == "delete":
            try:
                c.execute("DROP INDEX %s;" % (request.args.get('name')))
                conn.commit()
                flash("Successfully deleted.")
            except Exception as e:
                conn.rollback()
                errorMessage(e)

        # UPDATE
        elif request.form["submit"] == "update":
            try:
                c.execute("ALTER INDEX %s RENAME TO %s;" % (request.args.get('name'), request.form["name"]))    
                conn.commit()
                flash("Successfully updated.")
            except Exception as e:
                conn.rollback()
                errorMessage(e)
       
        # INSERT
        else:
            try:
                if request.form["method"] != "":
                    if "attributes1" in request.form:
                        c.execute("CREATE %s INDEX %s ON %s USING %s (%s);" % (request.form["attributes1"], request.form["name"], request.form["table"], request.form["method"], request.form["columns"]))
                    else:
                        c.execute("CREATE INDEX %s ON %s USING %s (%s);" % (request.form["name"], request.form["table"], request.form["method"], request.form["columns"]))
                else:
                    if "attributes1" in request.form:
                        print("HEY00")
                        c.execute("CREATE %s INDEX %s ON %s (%s);" % (request.form["attributes1"], request.form["name"], request.form["table"], request.form["columns"]))   
                    else:
                        print("HEY01")
                        c.execute("CREATE INDEX %s ON %s (%s);" % (request.form["name"], request.form["table"], request.form["columns"]))   
                
                if "attributes0" in request.form:
                    print("HEY")
                    c.execute("CLUSTER %s USING %s;" % (request.form["table"], request.form["name"]))

                conn.commit()
                flash("Successfully inserted.")
            except Exception as e:
                conn.rollback()
                errorMessage(e)

        return redirect(request.path,code=302)

    c.execute("SELECT * FROM pg_indexes WHERE tablename='hairs' OR tablename='faces' OR tablename='npcs' OR tablename='regions' ORDER BY tablename")
    data = c.fetchall()
    return render_template("table_indexes.html", data=getIndexInfo(data))


@app.route("/hairs", methods=["POST", "GET"])
def hairs():
    if request.method == "POST" and request.form["submit"] != "showAll":

        # DELETE
        if request.form["submit"] == "delete":
            try:
                c.execute("DELETE FROM hairs WHERE hairFile='%s' AND color='%s';" % (request.args.get('hairFile'), request.args.get('color')))
                conn.commit()
                flash("Successfully deleted.")
            except Exception as e:
                conn.rollback()
                errorMessage(e)

        # UPDATE
        elif request.form["submit"] == "update":
            try:
                c.execute("UPDATE hairs SET hairFile='%s', color='%s' WHERE hairFile='%s' AND color='%s';" % (request.form["hairFile"], request.form["color"], request.args.get('hairFile'), request.args.get('color')))    
                conn.commit()
                flash("Successfully updated.")
            except Exception as e:
                conn.rollback()
                errorMessage(e)
       
       # SELECT
        elif request.form["submit"] == "search":
            return search("hairs")

        # INSERT
        else:
            try:
                c.execute("INSERT INTO hairs VALUES ('%s', '%s');" % (request.form["hairFile"], request.form["color"]))   
                conn.commit()
                flash("Successfully inserted.")
            except Exception as e:
                conn.rollback()
                errorMessage(e)

        return redirect(request.path, code=302)

    c.execute("SELECT * FROM hairs ORDER BY color")
    data = c.fetchall()
    return render_template("table_hairs.html", data=data)


@app.route("/faces", methods=["POST", "GET"])
def faces():
    if request.method == "POST" and request.form["submit"] != "showAll":

        # DELETE
        if request.form["submit"] == "delete":
            try:
                c.execute("DELETE FROM faces WHERE id='%s';" % (request.args.get('id')))
                conn.commit()
                flash("Successfully deleted.")
            except Exception as e:
                conn.rollback()
                errorMessage(e)
        
        # UPDATE
        elif request.form["submit"] == "update":
            print("id", request.form["id"])
            try:
                c.execute("UPDATE faces SET id='%s', mouthFile='%s', eyesFile='%s', noseFile='%s', earsFile='%s', hairFile='%s', color='%s' WHERE id='%s';" % (request.form["id"], request.form["mouthFile"], request.form["eyesFile"], request.form["noseFile"], request.form["earsFile"], request.form["hairFile"], request.form["color"], request.args.get('id')))    
                conn.commit()
                flash("Successfully updated.")
            except Exception as e:
                conn.rollback()
                errorMessage(e)
       
        # SELECT
        elif request.form["submit"] == "search":
            return search("faces")

        # INSERT
        else:
            try:
                print("mouth", request.form["mouthFile"])
                c.execute("INSERT INTO faces VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (request.form["id"], request.form["mouthFile"], request.form["eyesFile"], request.form["noseFile"], request.form["earsFile"], request.form["hairFile"], request.form["color"]))   
                conn.commit()
                flash("Successfully inserted.")
            except Exception as e:
                conn.rollback()
                errorMessage(e)
        
        return redirect(request.path, code=302)

    c.execute("SELECT * FROM faces ORDER BY id")
    data = c.fetchall()
    return render_template("table_faces.html", data=data)



@app.route("/npcs", methods=["POST", "GET"])
def npcs():
    print("START")
    if request.method == "POST" and request.form["submit"] != "showAll":

        # DELETE        
        if request.form["submit"] == "delete":
            try:
                c.execute("DELETE FROM npcs WHERE id='%s' AND namereg='%s';" % (request.args.get('id'), request.args.get('namereg')))
                conn.commit()
                flash("Successfully deleted.")
            except Exception as e:
                conn.rollback()
                errorMessage(e)

        # UPDATE
        elif request.form["submit"] == "update":
            try:
                c.execute("UPDATE npcs SET name='%s', sex='%s', color='%s', height='%s', health='%s', id='%s', namereg='%s' WHERE id='%s' AND namereg='%s';" % (request.form["name"], request.form["sex"], request.form["color"], request.form["height"], request.form["health"], request.form["id"], request.form["namereg"], request.args.get('id'), request.args.get('namereg')))    
                conn.commit()
                flash("Successfully updated.")
            except Exception as e:
                conn.rollback()
                errorMessage(e)

        # SELECT
        elif request.form["submit"] == "search":
            return search("npcs")

        # INSERT        
        else:
            try:
                c.execute("INSERT INTO npcs VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (request.form["name"], request.form["sex"], request.form["color"], request.form["height"], request.form["health"], request.form["id"], request.form["namereg"]))
                conn.commit()
                flash("Successfully inserted.")
            except Exception as e:
                conn.rollback()
                errorMessage(e)

        
        return redirect(request.path,code=302)

    c.execute("SELECT * FROM npcs ORDER BY id")
    data = c.fetchall()
    return render_template("table_npcs.html", data=data)



@app.route("/regions", methods=["POST", "GET"])
def regions():
    if request.method == "POST" and request.form["submit"] != "showAll":
       
       # DELETE
        if request.form["submit"] == "delete":
            try:
                c.execute("DELETE FROM regions WHERE nameReg='%s'" % (request.args.get('nameReg')))    
                conn.commit()
                flash("Successfully deleted.")
            except Exception as e:
                conn.rollback()
                errorMessage(e)
        
       # UPDATE
        elif request.form["submit"] == "update":
            try:
                c.execute("UPDATE regions SET nameReg='%s', weather='%s' WHERE nameReg='%s'" % (request.form["nameReg"], request.form["weather"], request.args.get('nameReg')))    
                conn.commit()
                flash("Successfully updated.")
            except Exception as e:
                conn.rollback()
                errorMessage(e)
               
        # SELECT
        elif request.form["submit"] == "search":
            return search("regions")

       # CREATE
        else:
            try:
                c.execute("INSERT INTO regions VALUES ('%s', '%s');" % (request.form["nameReg"], request.form["weather"]))   
                conn.commit()
                flash("Successfully inserted.")
            except Exception as e:
                conn.rollback()
                errorMessage(e)
        
        return redirect(request.path,code=302)

    c.execute("SELECT * FROM regions ORDER BY nameReg")
    data = c.fetchall()
    return render_template("table_regions.html", data=data)


if __name__ == "__main__":
    app.secret_key = 'key'
    app.run()