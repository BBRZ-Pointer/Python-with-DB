import sqlite3

def init_db():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

    with open("init_student_db.sql", "r", encoding="utf-8") as f:
        sql = f.read()

    cur.executescript(sql)
    conn.commit()
    conn.close()
    print("数据库初始化完成 ✔")

def search():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

    key = input("请输入检索关键词：")

    sql = "SELECT * FROM students WHERE name LIKE ? OR major LIKE ?"
    cur.execute(sql, ("%"+key+"%", "%"+key+"%"))

    rows = cur.fetchall()

    print("\n==== 查询结果 ====")
    for r in rows:
        print(r)

    conn.close()

if __name__ == "__main__":
    init_db()
    search()
