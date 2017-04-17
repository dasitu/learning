#!-- UTF-8 --

from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you do not want that, hit CTRL-C to terminate this program."
print "If you want to continue, hit ENTER."

raw_input("?")

print "Opening the file..."
with open(filename, 'r+') as target_file:
    print "Truncating the file... Goodbye!"
    target_file.truncate()

    print "Now, I am going to ask you for three lines."
    line1 = raw_input("line 1:")
    line2 = raw_input("line 2:")
    line3 = raw_input("line 3:")

    print "Writing these content to file: %s" % filename
    target_file.write(line1)
    target_file.write("\n")
    target_file.write(line2)
    target_file.write("\n")
    target_file.write(line3)
    target_file.write("\n")

    target_file.flush()

    print "Current position of the file handler: %d." % target_file.tell()

    print "Moving to the beginning of the file."
    target_file.seek(0)

    print "Now the file content is updated to:"
    for line in target_file.readlines():
        print line

    print "And finally, we close the file."
target_file.close()
