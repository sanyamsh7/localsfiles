from DoubleLinkedList import DoubleLinkedList

class Dictionary(object):
    def __init__(self, max_numbers = 256):
        self.map = DoubleLinkedList()
        for i in range(max_numbers):
            self.map.push(DoubleLinkedList())

    def set(self, key, value):
        bucket, slot = self.get_slot(key)
        if slot:
            slot.data = (key,value)

        else:
            bucket.push((key,value))

    def get_slot(self, key, default = None):
        bucket = self.get_bucket(key)
        if bucket:
            node = bucket.head
            while node:
                if node.data[0] == key:
                    return bucket, node
                else:
                    node = node.next
        return bucket, None

    def get_bucket(self, key):
        bucket_id = self.hash_key(key)
        bucket = self.map.get(bucket_id)
        return bucket

    def hash_key(self, key):
        count = self.map.count()
        index = hash(key)%count
        return index

    def get(self, key, default = None):
        bucket, node = self.get_slot(key, default = default)
        return node and node.data[1] or node

    def default(self, key):
        bucket, slot = self.get_slot(key)
        bucket_node = bucket.head
        while bucket_node:
            k, v = bucket_node.data
            if k == key:
                bucket.remove(bucket_node.data)
                break
            else:
                bucket_node = bucket_node.next

    def list(self):
        bucket_node = self.map.head
        while bucket_node:
            slot_node = bucket_node.data.head
            while slot_node:
                print(slot_node.data)
                slot_node = slot_node.next
            bucket_node = bucket_node.next
