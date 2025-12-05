# py-kafka-sdk

A simple Python SDK for Apache Kafka, providing:

- Asynchronous producer abstraction  
- Multi-threaded consumer utilities  
- Batch and single-message consumption  

---

## 🚀 Easy Setup (Recommended)

If you just want to install and use the SDK:

### Install

```sh
pip install py-kafka-sdk
```

### Usage Example (Producer)

```python
from py_kafka_sdk.producer import KafkaProducer

producer = KafkaProducer(
    brokers="localhost:9092",
)

producer.start_delivery_handler(lambda err, msg: print("Delivered:", msg))

producer.produce(
    topic="test-topic",
    value=b"hello world"
)

producer.close()
```

### Usage Example (Consumer)

```python
from py_kafka_sdk.consumer import new_consumer, consume

consumer = new_consumer(
    brokers="localhost:9092",
    group_id="test-group",
    topics=["test-topic"]
)

consume(
    stop_event=None,   # For simple usage, the user may pass a dummy or manage externally
    consumer=consumer,
    handler=lambda msg: print(msg.value())
)
```

---

## 🛠️ Developer Setup (Run Locally / Build / Contribute)

If you want to modify the library, run examples, or contribute:

### Clone the repo

```sh
git clone https://github.com/mateuspdasilva/py-kafka-sdk
cd py-kafka-sdk
```

### Install dependencies

```sh
pip install -r requirements.txt
```

### Local environment

Create a `.env` file:

```
KAFKA_BROKERS=localhost:9092
KAFKA_TOPICS=test-topic
KAFKA_GROUP_ID=test-group
```

---

## 🐳 Running Kafka Locally (Docker Compose)

Use the included `docker-compose.yml`:

```sh
docker-compose up -d
```

This starts:
- Zookeeper  
- Kafka broker  
- Kafka UI (if configured)

---

## 📌 Running Examples

### Producer example

```sh
python examples/producer_example.py
```

### Consumer example

```sh
python examples/consumer_example.py
```

---

## 🧪 Running Tests

Kafka must be running on `localhost:9092`.

Run tests:

```sh
pytest tests/test_producer.py
pytest tests/test_consumer.py
```

Note: Run `test_consumer` last — it waits for a message produced by the previous test.

---

## 📚 Notes

- No brokers or topics are hardcoded — everything is injected via parameters or env vars.  
- The SDK is intentionally minimal and easy to extend.  
- Check the source code for advanced features (batch consumption, threaded consumption, custom configs).  
