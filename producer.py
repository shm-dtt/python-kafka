import uuid
import json
import random
import names
from faker import Faker
from faker_food import FoodProvider
fake = Faker()
fake.add_provider(FoodProvider)


from confluent_kafka import Producer
producer_config = {"bootstrap.servers": "localhost:9092"}

producer = Producer(producer_config)

def delivery_report(err, msg):
    if err:
        print("Message delivery failed: {}".format(err))
    else:
        print("Message delivery succeeded: {}".format(msg.value().decode('utf-8')))
        # print(dir(msg))


n=0

while n<100:
    order = {
        "order_id": str(uuid.uuid4()),
        "user": names.get_first_name(),
        "item": fake.dish(),
        "quantity": random.randint(1, 15),
    }

    value = json.dumps(order).encode("utf-8")

    producer.produce(
        topic="orders",
        value=value,
        callback=delivery_report
    )

    if n % 7 == 0:
        producer.flush()
    n += 1

producer.flush()


