class Song(object):

  def __init__(self, lyrics):
    self.lyrics = lyrics

  def sing_me_a_song(self):
    for line in self.lyrics:
      print line

rock_around = Song(['one', 'two', 'three oclock', 'four oclock rock'])

rock_around.sing_me_a_song()