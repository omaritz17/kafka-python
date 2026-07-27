import logging
from confluent_kafka import Producer
from typing import Any

logger = logging.getLogger(__name__) 

#Create Kafka Properties 
def producer_job(record):
    conf = {
            'bootstrap.servers': 'localhost:9092',  # Replace with broker addresses
            'acks': 'all'                           # Ensures maximum data durability
        }

    #Create the Producer
    producer = Producer(conf) 

    #send data -- Asynchronous 
    producer.produce(
        topic = 'python_demo', value = record.encode("utf-8")
    )


    #flush and close the producer -- Synchronous
    print("Flushing outstanding messages...")
    producer.flush()