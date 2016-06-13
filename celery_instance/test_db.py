import os
import sqlite3

import PIL
from PIL import Image

cur_dir = os.path.dirname(os.path.realpath(__file__))
DB_FILE = os.path.join(cur_dir, 'example.db')

def resize_image(image_path):
    image_path = os.path.abspath(image_path)
    basewidth = 300
    img = Image.open(image_path)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    img.save(os.path.splitext(image_path)[0] + '_resize' + os.path.splitext(image_path)[1])


def resize(image_path):
    resize_image(image_path)
    db_op(image_path, -1)
    print (image_path)

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

#resize('test')

def read_data():
    conn = sqlite3.connect(DB_FILE)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM CONVERSION_STATUS")
    rows = cur.fetchall()
    for row in rows:
        print(row)
resize_image(r'D:\work\photos\20130601_122119.jpg')