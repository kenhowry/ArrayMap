class Item:
    def __init__(self, k, v):
        self.key = k
        self.value = v

    def set_value(self, new_value):
        old_value = self.set_value
        self.value = new_value
        return old_value
        
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"<{self.key}, {self.value}>"
    
class ArrayMap:
    def __init__(self):
        self.the_map = []

    def __str__(self):
        return str(self.the_map)
    
    def __iter__(self):
        return iter(self.keys())

    def put(self, k, v):
        #search for an item w/ key 'k'
        for item in self.the_map:
            if item.key == k:
                return item.set_value(v)
        
        #if Item is not found in the map
        new_item = Item(k, v)
        self.the_map.append(new_item)
        return None
    
    def get(self, k):
        #check if key exists
        for item in self.the_map:
            if item.key == k:
                return item.value
        #if key does not exist
        return None
    
    def remove(self, k):
        for item in self.the_map:
            if item.key == k:
                removed_value = item.value
                self.the_map.remove(item)
                return removed_value
            
        return None

    def items(self):
        """
        Description:
            returns an iterable over a snapshot of the items
        Parameters:
            None
        Return:
            list
        """
        return [item for item in self.the_map]
    
    def keys(self):
        return [item.key for item in self.the_map]
    
    def values(self):
        return [item.value for item in self.the_map]


map = ArrayMap()

map.put("A", "Apple")
map.put("B", "Bee")
map.put("C", "Car")
map.put("D", "Day")
map.put("D", "Dog")
print(map.remove("C"))
print(map)