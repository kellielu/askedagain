import threading
import time
import kafka
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import debug as config


class Consumer(threading.Thread):
    def run(self):
        consumer = kafka.KafkaConsumer(bootstrap_servers=config.KAFKA_SERVER)
        consumer.subscribe([config.KAFKA_TOPIC])

        for message in consumer:
            print("{0}\n\n".format(message))


def main():
    thread = Consumer()
    thread.daemon = True
    while True:
        if not thread.isAlive():
            print("Starting kafka consumer!")
            thread.start()
        else:
            print("Listening for new messages for topic: {0}".format(config.KAFKA_TOPIC))
            time.sleep(5)


if __name__ == "__main__":
    main()