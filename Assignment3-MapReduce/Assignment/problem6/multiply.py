import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	matrix_name = record[0]
	row = record[1]
	col = record[2]
	value = record[3]
	for i in xrange(0,5):
		if (matrix_name == "a"):
			mr.emit_intermediate((row, i), (col, value))
		else:
			mr.emit_intermediate((i, col), (row, value))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
	pairs = { }
	for v in list_of_values:
		k = v[0]
		value = v[1]
		if (k not in pairs):
			pairs[k] = []
		pairs[k] += [value]
	
	s = 0
	for p in pairs.values():
		if (len(p)>1):
			s += p[0] * p[1]
	mr.emit((key[0], key[1], s))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
