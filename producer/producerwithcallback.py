import logging
from confluent_kafka import Producer
from typing import Any
import time

logger = logging.getLogger(__name__) 

#Create Kafka Properties 
def producer_with_callback(record):
    conf = {
            'bootstrap.servers': 'localhost:9092',  # Replace with broker addresses
            'batch.size': '400',
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
            "Topic: %s\n"
            "Partition: %d\n"
            "Offset: %d",
            msg.topic(),
            msg.partition(),
            msg.offset(),
        )
    for j in range(10):
        for num in range(30): 
            #send data -- Asynchronous 
            producer.produce(
            topic = 'python_demo', 
            value = f"{record} + {++num}".encode("utf-8"), 
            callback= on_delivery
        )
        try:
            time.sleep(0.5)
        except Exception as e:
            logger.error(f"{e}")

    

    #flush and close the producer -- Synchronous
    print("Flushing outstanding messages...")
    producer.flush()