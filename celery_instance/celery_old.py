# Not used!!!!!!!!!!!
from Celery import Celery

app = Celery('proj',broker='amqp://zhongqi@192.168.0.126//')
             #backend='amqp://',
             #include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()