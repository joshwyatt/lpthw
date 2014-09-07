class Person(object):

  def __init__(self, name):
    self.name = name

  def say_my_name(self):
    print "My name is %s" % self.name

josh_wyatt = Person('Josh')

josh_wyatt.say_my_name()

bonnie_chan = Person('bonnie')
bonnie_chan.say_my_name()