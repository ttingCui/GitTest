from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

@app.route("/add/user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        conn = pymysql.connect(host="192.168.1.108", port=3306, user="root", password="288cuiting", charset="utf8",
                               db="unicom")
        cursor = conn.cursor()
        sql2 = "select * from admin"
        cursor.execute(sql2)
        userlist = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template("add_user.html", userlist=userlist)
    username = request.form.get("user")
    password = request.form.get("password")
    mobile = request.form.get("mobile")

    conn = pymysql.connect(host="192.168.1.108", port=3306, user="root", password="288cuiting", charset="utf8",
                           db="unicom")
    cursor = conn.cursor()

    sql = "insert into admin(username, password, mobile) values(%s, %s, %s)"
    cursor.execute(sql, [username, password, mobile])
    conn.commit()

    cursor.close()
    conn.close()
    return "注册成功"




if __name__ == '__main__':
    app.run()