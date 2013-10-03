import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

# Map function
# mr - MapReduce object
# data - json object formatted as a string
def mapper(record):
   table_name = record[0]
   order_id = record[1] 
   mr.emit_intermediate(order_id, record)

def mapper0(record):
   row = record.split(',')
   row = [w.replace('"', '').replace('[','').replace(']','').replace(' ', '') for w in row]
   mr.emit_intermediate(row[1], row)

# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
def reducer(key, list_of_values):
    #print list_of_values
    list_length = len(list_of_values)
    if list_length > 1:
        list_of_line_items = list_of_values[1:]
        order_list = []
        order_list = list_of_values[0]
        for l in list_of_line_items:
            emit_list = []
            for i in order_list:
                emit_list.append(i)
            for j in l:
                emit_list.append(j)
            mr.emit(emit_list)

def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    #one per line.
    mr.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    main()
