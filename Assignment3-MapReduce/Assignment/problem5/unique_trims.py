import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

# Map function
# mr - MapReduce object
# data - json object formatted as a string
def mapper(record):
   sequence_id = record[0]
   nucleotide = record[1]
   mr.emit_intermediate(nucleotide[:-10], sequence_id)

# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
def reducer(key, list_of_nucleotides):
        mr.emit(key)
    #trim the last 10 characters
    #for n in list_of_nucleotides:
    #    n = n[:-10] 
    #    mr.emit((key, len(n), n))

def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    #one per line.
    mr.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    main()
