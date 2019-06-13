from __future__ import absolute_import, unicode_literals
from celery import Celery

celery_app = Celery('word_cloud',
             broker='amqp://localhost/',
             backend='rpc://',
             include=['word_cloud.tasks.tasks'])


if __name__ == '__main__':
    celery_app.start()

# def make_celery(app):
#     celery = Celery(
#         app.import_name,
#         backend=app.config['CELERY_BACKEND'],
#         broker=app.config['CELERY_BROKER_URL']
#     )
#     celery.conf.update(app.config)

#     class ContextTask(celery.Task):
#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return self.run(*args, **kwargs)

#     celery.Task = ContextTask
#     return celery