import logging
from confluent_kafka import Consumer

#Logging
logger = logging.getLogger(__name__)

#Create Kafka Properties 
def consumer_job():
    """
    Consumer records from Kafka
    
    Parameters:
    None
    
    Returns:
    None
    
    """
    #Consumer Configs
    conf = {
            'bootstrap.servers': 'localhost:9092',  # Replace with broker addresses
            'group.id': 'my-python-application',     # Group id must be set
            'auto.offset.reset': 'earliest',
            #'debug': 'generic,broker,cgrp,consumer' #DEBUG LOGS
        }

    #Create Consumer
    consumer = Consumer(conf, logger=logger)

    #Subscirbe to a topic
    topic = ["python_demo"]
    consumer.subscribe(topic)

    #Poll for Data
    try: 
        while True:
            #logger.info("Polling for records")

            #records = consumer.poll(timeout=1.0) # returns 1 record
            records = consumer.consume(num_messages=100, timeout=1.0) #Batches of records

            for record in records:
            
                key_decoded = record.key().decode("utf-8") if record.key() is not None else "None"
                value_decoded = record.value().decode("utf-8") if record.value() is not None else "None"
                logger.info(f"Key: {key_decoded} , Value: {value_decoded} \n Partition: {record.partition()} Offset: {record.offset()}")
                
    except KeyboardInterrupt as e:
        logger.info("Consumer is starting to shutdown")     
    except Exception as e:
        logger.error("Unexpected exception: {e}")
    finally:
        consumer.close() #Close consumer and commit offsets

