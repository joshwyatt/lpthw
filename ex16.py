from sys import argv

script, filename = argv

formatter = "%r %r %r %r %r %r "
newline = "\n"

print "We're going to erase %r." % filename
print "If you don't wanna' do that hit ^C."
print "If that's cool, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Bye!!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

stuff_to_write = formatter % (line1, newline, line2, newline, line3, newline)

target.write(stuff_to_write)

print "And now close it"
target.close()