from producer import KafkaProducer
from config import KAFKA_BROKERS, KAFKA_TOPICS

def delivery_report(err, msg):
    if err:
        print(f"Delivery failed: {err}")
    else:
        print(f"Delivered to {msg.topic()} [{msg.partition()}]")

if __name__ == "__main__":
    producer = KafkaProducer(KAFKA_BROKERS)
    producer.start_delivery_handler(delivery_report)
    producer.produce(KAFKA_TOPICS, b"py-kafka-sdk test message")
    producer.close()
    print("Message sent!")
