from stanfordkarel import *

class ktools:
  def m(self):
    """move"""
    move()

  def m2(self):
    """moves twice"""
    self.m()
    self.m()
    
  def m3(self):
    """moves three times"""
    self.m2()
    self.m()

  def m4(self):
    """moves four times"""
    self.m2()
    self.m2()

  def m5(self):
    """moves five times"""
    self.m2()
    self.m2()
    self.m

  def tl(self):
    """turn left"""
    turn_left()

  def tr(self):
    """turn right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """turn around"""
    self.tl()
    self.tl()

  def pick(self):
    """pick beeper"""
    pick_beeper()

  def pick3(self):
    """pick 3 beepers in a line"""
    self.pick()
    self.m()
    self.pick()
    self.m()
    self.pick()

  def put(self):
    """put beeper"""
    put_beeper()

  def put2(self):
    """put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def put7(self):
    """put 7 beepers in a line"""
    self.put5()
    self.m()
    self.put2()

  def h(self):
    """print letter H using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m3()
    self.tr()
    self.put5()
    self.ta()
    self.m2()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m2()
    self.tl()
    self.m4()

  def e(self):
    """print letter E using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m2()
    self.tr()
    self.put2()
    self.tl()
    self.m2()
    self.tl()
    self.put2()
    self.m2()

  def l(self):
    """print letter L using beepers"""
    self.tl()
    self.put5()
    self.ta()
    self.m4()
    self.tl()
    self.m()
    self.put2()
    self.m2()

  def o(self):
    """print letter O using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.ta()
    self.m4()

  def b(self):
    """print letter B using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.m2()
    self.put()
    self.tr()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.ta()
    self.m2()
    self.put()
    self.tl()
    self.m3()

  def r(self):
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.m
    self.tr()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.tl()
    self.m()
    self.tr()
    self.m()
    self.put2()
    self.tl()
    self.m2()

  def a(self):
    self.tl()
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.tr()
    self.m2()
    self.put()
    self.ta()
    self.m()
    self.tr()
    self.m()
    self.tr()
    self.put2()
    self.m()
    self.put2()
    self.tl()
    self.m2()

  def d(self):
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.ta()
    self.m3()

  def n(self):
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tl()
    self.m()
    self.tr()
    self.put()
    self.tl()
    self.m()
    self.tr()
    self.m2()
    self.ta()
    self.put5()
    self.ta()
    self.m4()
    self.tl()
    self.m2()

  def fic(self) -> bool:
    """Front is Clear"""
    return front_is_clear()

  def fib(self) -> bool:
    """Front is Blocked"""
    return not self.fic()

  def ric(self) -> bool:
    """Right is Clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True
    self.tl()
    return False

  def rib(self) -> bool:
    """Right is Blocked"""
    return not self.ric()

  def mazemove(self):
    """Maze Move"""
    if self.fib:
      self.tl()
    else:
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr
          self.m()
    pass
    

def main():
    """ Karel code goes here! """
    kt = ktools()
  
    pass


if __name__ == "__main__":
    run_karel_program()