import time
import argparse
import random
import datetime
import json as js
from google.cloud import pubsub_v1


def create_topic(project, topic_name):
    pubsub_client = pubsub_v1.PublisherClient()
    topic_path = pubsub_client.topic_path(project, topic_name)
    topic = pubsub_client.create_topic(topic_path)
    print 'Topic {} created'.format(topic_name)

def create_subscriber(project, topic_name, subscription_name):
    subscriber = pubsub_v1.SubscriberClient()
    topic_path = subscriber.topic_path(project, topic_name)
    subscription_path = subscriber.subscription_path(project, subscription_name)

    subscription = subscriber.create_subscription(subscription_path, topic_path)

    print('Subscription created: {}'.format(subscription))

def publish_message(data,project, topic_name):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project, topic_name)

    data = data.encode('utf-8')
    print data
    message_id = publisher.publish(topic_path, data=data)

    #print('Message ID:{} published to topic {}'.format(message_id,topic_name))

def receive_message(counter,project, subscription_name):
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project, subscription_name)

    def callback(message):
        print('Received message: {}'.format(message))
        message.ack()

    subscriber.subscribe(subscription_path, callback=callback)
    print('Listening for messages on {}'.format(subscription_path))
    while True:
        time.sleep(60)

#    for i in xrange(counter):
#        results = subscriber.pull(return_immediately=False)
#        if results:
#            for ack_id, message in results:
#                print '* {}: {}, {}'.format(message.message_id, message.data, message.attributes)
#                subscriber.acknowledge([ack_id for ack_id, message in results])



# ----------------------------------------------
# Generating only 10 stock prices for testing
# ----------------------------------------------

def deliver_stock_price(cnt):
    topic_name = 'salesstream'
    subscription_name = 'salesReceiver'
    project = 'complete-rush-206308'
    counter = 1
    hms_time = datetime.datetime.strptime('9:30:00', '%H:%M:%S')
    stock = cnt
    product = {'milk':22, 'soft_drink_300ml':37, 'soft_drink_500ml':43, 'soft_drink_1l':69, 'beer':84, 'snacks':51, 'sweets':112, 'candy':34,'rice':67, 'dhal':73,'shampoo':96, 'soap':29,'face_wash':121,'chicken':212,'mutton':576, 'shirt':399, 'pant':599, 'shorts':259, 'salvar':699, 'shoe':399,'flipflop':199}
    for num, ix in enumerate(product):
        hms_time = hms_time + datetime.timedelta(0,1)
        #stock = stock_price(stock)
        data = '{},{},{},{}'.format(time.time(),ix,product[ix],num+1)
        #data = ('%s\n' % js.dumps({'ProductID': 1 + num, 'ProductName': ix, 'Price': product[ix], 'Timestamp': time.time()}))
        #print data
        publish_message(data,project, topic_name)
        counter = counter + 1

    return counter

if __name__ == "__main__":
    topic_name = 'salesstream'
    subscription_name = 'salesReceiver'
    project = 'complete-rush-206308'

    parser = argparse.ArgumentParser()
    parser.add_argument('--cnt', help='Give a count for product sale iteration', required=True, type=int)
    args = parser.parse_args()

    #create_topic(project, topic_name)
    #create_subscriber(project, topic_name, subscription_name)
    counter = deliver_stock_price(args.cnt)
    print(counter)
    receive_message(counter,project, subscription_name)
