# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists

script, from_file, to_file = argv
print "copying file content from %s to %s" % (from_file, to_file)

input_file_handler = open(from_file)
input_file_content = input_file_handler.read()
print "The input file size is %d bytes." % len(input_file_content)
print "Does the out put file exists? %s" % exists(to_file)

print "Ready, hit ENTER to continue or CTRL+C to terminate."
raw_input()

out_file_handler = open(to_file, 'w')
out_file_handler.write(input_file_content)

print "All Done."
input_file_handler.close()
out_file_handler.close()
