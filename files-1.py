# to view the contents of zip file


#from zipfile import *

#z = ZipFile("test.zip","r")
# z.extractall()
# z.close()
from itertools import islice
def file_read_from_head(fname, nlines):

    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)

file_read_from_head('sample.txt', 2)
