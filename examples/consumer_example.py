from consumer import new_consumer, consume
from config import KAFKA_BROKERS, KAFKA_TOPICS, KAFKA_GROUP_ID
import threading

def print_message(msg):
    if msg is not None and not msg.error():
        print(f"Received: {msg.value().decode('utf-8')}")

if __name__ == "__main__":
    consumer = new_consumer(KAFKA_BROKERS, KAFKA_GROUP_ID, [KAFKA_TOPICS])
    stop_event = threading.Event()
    try:
        consume(stop_event, consumer, print_message)
    except KeyboardInterrupt:
        print("Shutting down consumer...")
        stop_event.set()
    finally:
        consumer.close()
