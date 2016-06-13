from celery import Celery
import os
import sqlite3
from PIL import Image

app = Celery('proj', broker='amqp://zhongqi:working@192.168.0.126/myvhost')
cur_dir = os.path.dirname(os.path.realpath(__file__))
DB_FILE = os.path.join(cur_dir, 'example.db')


@app.task(name='add_task')
def add(x, y):
    print (x, y)
    return x + y

@app.task(name='resize')
def resize(image_path):
    print(image_path)
    resize_image(image_path)
    db_op(image_path, -1)
    print (image_path)

def resize_image(image_path):
    basewidth = 300
    img = Image.open(image_path)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(os.path.splitext(image_path)[0] + '_resize' + os.path.splitext(image_path)[1])

def db_op(image_path, status):
    conn = sqlite3.connect(DB_FILE)
    with conn:
        data = ((image_path, status),)
        cur = conn.cursor()
        print("Opened database successfully")
        #cur.execute("CREATE TABLE Cars(Name TEXT, Price INT)")
        #cur.execute("INSERT INTO Cars VALUES('Audi',52642)")
        cur.execute('''CREATE TABLE IF NOT EXISTS CONVERSION_STATUS
               (PATH CHAR(255) PRIMARY KEY     NOT NULL,
                STATUS INT NOT NULL);''')
        cur.executemany("INSERT INTO CONVERSION_STATUS VALUES(?, ?)", data)
        conn.commit()

def read_data():
    conn = sqlite3.connect(DB_FILE)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM CONVERSION_STATUS")
    rows = cur.fetchall()
    for row in rows:
        print(row)
read_data()