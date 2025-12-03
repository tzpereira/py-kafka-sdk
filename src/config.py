import os
from dotenv import load_dotenv

load_dotenv()

KAFKA_BROKERS = os.getenv('KAFKA_BROKERS', 'localhost:9092')
KAFKA_TOPICS = os.getenv('KAFKA_TOPICS', 'test-topic')
KAFKA_GROUP_ID = os.getenv('KAFKA_GROUP_ID', 'test-group')
