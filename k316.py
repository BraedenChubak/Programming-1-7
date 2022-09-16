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

def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.tl()
    kt.m2()
    kt.tr()
    kt.m3()
    kt.pick3()
    kt.tl()
    kt.m()
    kt.pick3()
    kt.tl()
    kt.m()
    kt.pick3()
    kt.tl()
    kt.m()
    kt.pick3()
    pass


if __name__ == "__main__":
    run_karel_program()