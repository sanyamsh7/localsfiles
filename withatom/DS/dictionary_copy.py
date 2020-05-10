from DoubleLinkedList import DoubleLinkedList

class Dictionary(object):
    def __init__(self, num_buckets = 5):
        """Initialized a Map with the given number of buckets."""
        self.map = DoubleLinkedList()
        for i in range(0, num_buckets):
            self.map.push(DoubleLinkedList())

    def hash_key(self, key):
        """Given a key this will create a number and then convert
        it to an index for the aMap's buckets."""
        return hash(key) % self.map.count()

    def get_bucket(self, key):
        """Given a key, find the bucket where it would go."""
        bucket_id = self.hash_key(key)
        print("....................bucket_id: ", bucket_id )
        return self.map.get(bucket_id)

    def get_slot(self, key, default = None):
        """Returns either the bucket and node for slot, or None,
        None"""
        bucket = self.get_bucket(key)

        if bucket:
            node = bucket.head
            i = 0
            while node:
                if key == node.data[0]:
                    return bucket, node
                else:
                    node = node.next
                    i += 1
        #fall through for both if and while above
        return bucket, None

    def get(self, key, default = None):
        """Gets the data in a bucket for a given key, or the default."""
        bucket, node  = self.get_slot(key, default = default)
        return node and node.data[1] or node

    def set(self, key, data):
        """Sets the key to the data, replacing any existing data."""
        # value = data here
        bucket, slot = self.get_slot(key)

        if slot:
            # the key exists, replace it
            slot.data = (key, data)
        else:
            # the key does not, append to create it
            bucket.push((key, data))

    def default(self, key):
        """Deletes the given key from the Map."""
        bucket = self.get_bucket(key)
        node = bucket.head
        while node:
            k, v = node.data
            if key == k:
                bucket.remove(node.data)
                break

    def list(self):
        """Prints out what's in the Map."""
        bucket_node = self.map.head
        while bucket_node:
            slot_node = bucket_node.data.head
            while slot_node:
                print(slot_node.data)
                slot_node = slot_node.next
            bucket_node = bucket_node.next
