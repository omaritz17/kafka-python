import logging
from confluent_kafka import Producer
from typing import Any
import time

logger = logging.getLogger(__name__) 

#Create Kafka Properties 
def producer_with_keys(record):
    conf = {
            'bootstrap.servers': 'localhost:9092',  # Replace with broker addresses
            'acks':'all',                           # Ensures maximum data durability
            }

    #Create the Producer
    producer = Producer(conf) 

    #Callback Func
    def on_delivery(err, msg):
        if err:
            logger.error("Delivery failed: %s", err)
            return

        logger.info(
            "Received new metadata\n"
            "Key: %s\n"
            "Topic: %s\n"
            "Partition: %d\n"
            "Offset: %d",
            msg.key().decode("utf-8"),
            msg.topic(),
            msg.partition(),
            msg.offset(),
        )

    for j in range(2):
        for i in range(10): 
            key = ++i
            #send data -- Asynchronous 
            producer.produce(
                    topic = 'python_demo', 
                    value = f"{record} + {++i}".encode("utf-8"), 
                    key = f"{key}".encode("utf-8"),
                    callback= on_delivery
                )


    

    #flush and close the producer -- Synchronous
    print("Flushing outstanding messages...")
    producer.flush()