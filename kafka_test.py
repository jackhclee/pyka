from confluent_kafka import Consumer, KafkaError, KafkaException
import time
import sys


def basic_consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write(
                        "%% %s [%d] reached end at offset %d\n"
                        % (msg.topic(), msg.partition(), msg.offset())
                    )
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(msg.value())
                sleep = 20
                print(f"sleep {sleep} sec")
                time.sleep(sleep)
                consumer.commit(msg)
    except KafkaException as ke:
        print("kafka exception caught")
        print(ke)
    except BaseException as err:
        print("error caught")
        print(err)
    finally:
        # Close down consumer to commit final offsets.
        print("Finally decided to continue")
        # consumer.close()


def shutdown():
    running = False


if __name__ == "__main__":
    print("Hey")
    conf = {
        "bootstrap.servers": "localhost:9092",
        "group.id": "my-group",
        "enable.auto.commit": "false",
        "auto.offset.reset": "earliest",
        "max.poll.interval.ms": "15000",
        "session.timeout.ms": "15000",
    }
    consumer = Consumer(conf)
    running = True
    basic_consume_loop(consumer, ["test"])
