import logging
from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer
from typing import Any
logger = logging.getLogger(__name__) 

#Create Kafka Properties 
conf : dict [str,Any] = {
        'bootstrap.servers': 'localhost:9092',  # Replace with broker addresses
        'key.serializer': StringSerializer,
        'value.serializer': StringSerializer,
        'acks': 'all'                           # Ensures maximum data durability
    }



#Create the Producer
producer = Producer(conf)

#send data

#flush and close the producer