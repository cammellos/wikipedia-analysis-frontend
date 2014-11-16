from celery import task
from kombu import Connection,Exchange, Queue, Consumer,eventloop
from edit_history.models import Url



def handle_message(body, message):
    title,state = body.split("-")
    url = Url.objects.get(title=title)
    if url:
      if state == Url.STATE.DOWNLOADING:
        url.downloading()
      elif state == Url.STATE.DOWNLOADED:
        url.downloaded()
      elif state == Url.STATE.PROCESSING:
        url.processing()
      elif state == Url.STATE.PROCESSED:
        url.processed()
      elif state == Url.STATE.COMPLETED:
        url.completed()
      elif state == Url.STATE.FAILED:
        url.failed()
      url.save()
    message.ack()

@task()
def listen_for_changes():
  wikipedia_exchange = Exchange('wikipedia', type='direct', durable=False)
  queue = Queue('status', wikipedia_exchange, routing_key='status')
  with Connection() as conn:
    with Consumer(conn, queue, callbacks=[handle_message]):
      for _ in eventloop(conn):
        pass


