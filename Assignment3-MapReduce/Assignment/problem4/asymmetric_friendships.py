import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

# Map function
# mr - MapReduce object
# data - json object formatted as a string
def mapper(record):
   friendA = record[0]
   friendB = record[1] 
   tupleFriendAB = (friendA, friendB)
   tupleFriendBA = (friendB, friendA)
   mr.emit_intermediate(tupleFriendAB, 1)
   mr.emit_intermediate(tupleFriendBA, 1)

# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
def reducer(key, list_of_friendTuples):
    friends = dict()
    for f in list_of_friendTuples:
        if key not in friends.keys():
            friends[key] = f;
        else:
            friends[key] += f;
    for k,v in friends.iteritems():
        if(v == 1):
            mr.emit(k)

def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    #one per line.
    mr.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    main()
