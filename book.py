import json
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
import json
import ccloud_lib


class Book:
  def __init__(self, price, title):
    self.price = price
    self.title = title

  def __str__(self):
    return str(self.__class__) + ' ' + f'price: {self.price} title: {self.title}'


if __name__ == "__main__":
    book = Book(50, "HK")
    print(book)
    print(json.dumps(book.__dict__))

    topic = 'book'

    # for full list of configurations, see:
    #  https://docs.confluent.io/platform/current/clients/confluent-kafka-python/#schemaregistryclient
    schema_registry_conf = {
        'url': 'http://localhost:8081'}

    schema_registry_client = SchemaRegistryClient(schema_registry_conf)


    def book_to_dict(book, ctx):
        return book.__dict__


    # name_avro_serializer = AvroSerializer(schema_registry_client=schema_registry_client,
    #                                       schema_str=ccloud_lib.name_schema,
    #                                       to_dict=ccloud_lib.Name.name_to_dict)
    count_avro_serializer = AvroSerializer(schema_registry_client=schema_registry_client,
                                           schema_str=ccloud_lib.book_schema,
                                           to_dict=book_to_dict)

    # for full list of configurations, see:
    #  https://docs.confluent.io/platform/current/clients/confluent-kafka-python/#serializingproducer
    producer_conf = {
        # 'key.serializer': StringSerializer,
        'bootstrap.servers': 'localhost:9092',
        'value.serializer': count_avro_serializer}
    producer = SerializingProducer(producer_conf)

    delivered_records = 0


    # Optional per-message on_delivery handler (triggered by poll() or flush())
    # when a message has been successfully delivered or
    # permanently failed delivery (after retries).
    def acked(err, msg):
        global delivered_records
        """Delivery report handler called on
        successful or failed delivery of message
        """
        if err is not None:
            print("Failed to deliver message: {}".format(err))
        else:
            delivered_records += 1
            print("Produced record to topic {} partition [{}] @ offset {}"
                  .format(msg.topic(), msg.partition(), msg.offset()))


    for n in range(10):
        book_object = Book(97, 'HK')
        print("Producing Avro record: {}")
        producer.produce(topic=topic, key=str(n), value=book, on_delivery=acked)
        producer.poll(0)

    producer.flush()

    print("{} messages were produced to topic {}!".format(delivered_records, topic))
