
from  config import logging_config  # type: ignore
from producer.producer import producer_job
from producer.producerwithcallback import producer_with_callback
from producer.producerwithkeys import producer_with_keys
from consumer.consumer import consumer_job

#Simple Producer Func -- Uncomment to Run
#producer_job("Hello World")


#Producer with callback -- Uncomment to Run
#producer_with_callback("Hello World")

#Producer with keys -- Uncomment to Run
#producer_with_keys("Hello World!")

#Consumer call
consumer_job()

