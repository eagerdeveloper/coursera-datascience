import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

# Map function
# mr - MapReduce object
# data - json object formatted as a string
def mapper0(record):
    data = json.loads(record, encoding='latin-1')
    for k, v in data.items():
       key = k
       value = v
       for w in v:
           #print w
           # output (key, value) pair (only for mapper)
           mr.emit_intermediate(w, key)

def mapper(record):
    key = record[0]
    value = record[1]
    words = value.split() 
    for w in words:
          #print w
          # output (key, value) pair (only for mapper)
        mr.emit_intermediate(w, key)

# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
def reducer(key, list_of_values):
    #wordsSet = set()
    #for w in list_of_values:
    #    wordsSet.add(w)

    mr.emit((key, list(set(list_of_values))))

def addToList(self, value):
    if value not in self.uniqueDocList:
        self.uniqueDocList.append(value)

def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    #one per line.
    mr.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    main()
