from celery import Celery

app = Celery('proj', broker='amqp://zhongqi:working@192.168.0.126/myvhost')

app.send_task("add_task", [1, 2])