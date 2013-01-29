import boto
import time
import random

def printqueues(conn):
    """docstring for printqueues"""
    qs = conn.get_all_queues()
    print "Number of queues " + str(len(qs))
    for q in qs:
        print q.id


def main():
    c = boto.connect_sqs()
    printqueues(c)
    q_name ='testqueue' + str(random.randint(1000, 9999))
    q = c.create_queue(q_name)
    while len(c.get_all_queues()) == 0:
        print "Sleeping for queue create"
        time.sleep(10)
    printqueues(c)

    m = boto.sqs.message.Message()
    m.set_body("Hey Everybuddy!")
    status = q.write(m)  # returns True, False or Exception
    time.sleep(3)
    
    r = q.get_messages()
    print r[0].get_body()
    q.delete_message(r[0])

    c.delete_queue(q)
    while len(c.get_all_queues()) != 0:
        print "Sleeping for queue delete"
        time.sleep(10)
    printqueues(c)


if __name__ == '__main__':
    main()
