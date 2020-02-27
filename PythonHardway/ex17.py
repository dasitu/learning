# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists

script, input_file, output_file = argv
print "Copying file content from %s to %s" % (input_file, output_file)

input_file_handler = open(input_file)
input_file_content = input_file_handler.read()
print "The input file size is %d bytes." % len(input_file_content)
print "Does the output file exists? %s" % exists(output_file)

print "Ready, hit ENTER to continue or CTRL+C to terminate."
raw_input()

output_file_handler = open(output_file, 'w')
output_file_handler.write(input_file_content)

print "All Done."
input_file_handler.close()
output_file_handler.close()
