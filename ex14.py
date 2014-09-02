from sys import argv

script, user_name = argv
prompt = '> '

print "Hello %s I'm %s." % (user_name, script)
print "I'd like to ask you a couple questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, when I asked if you like me you said %r.
You live in %r and you have a %r computer.
""" % (likes, lives, computer)