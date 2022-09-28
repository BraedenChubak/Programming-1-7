from stanfordkarel import *

class ktools:
  def m(self):
    """move"""
    move()

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
    self.putm(2)
    self.m()
    self.putm(2)
    self.m()
    self.put()

  def put7(self):
    """put 7 beepers in a line"""
    self.putm(5)
    self.m()
    self.putm(2)

  def h(self):
    """print letter H using beepers"""
    self.tl()
    self.putm(5)
    self.tr()
    self.mm(3)
    self.tr()
    self.putm(5)
    self.ta()
    self.mm(2)
    self.tl()
    self.m()
    self.putm(2)
    self.tl()
    self.mm(2)
    self.tl()
    self.mm(4)

  def e(self):
    """print letter E using beepers"""
    self.tl()
    self.putm(5)
    self.tr()
    self.m()
    self.putm(2)
    self.tr()
    self.mm(2)
    self.tr()
    self.putm(2)
    self.tl()
    self.mm(2)
    self.tl()
    self.putm(2)
    self.mm(2)

  def l(self):
    """print letter L using beepers"""
    self.tl()
    self.putm(5)
    self.ta()
    self.mm(4)
    self.tl()
    self.m()
    self.putm(2)
    self.mm(2)

  def o(self):
    """print letter O using beepers"""
    self.tl()
    self.putm(5)
    self.tr()
    self.m()
    self.putm(2)
    self.m()
    self.tr()
    self.putm(5)
    self.tr()
    self.m()
    self.putm(2)
    self.ta()
    self.mm(4)

  def b(self):
    """print letter B using beepers"""
    self.tl()
    self.putm(5)
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.mm(2)
    self.put()
    self.tr()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.ta()
    self.mm(2)
    self.put()
    self.tl()
    self.mm(3)

  def r(self):
    self.tl()
    self.putm(5)
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
    self.putm(2)
    self.tl()
    self.mm(2)

  def a(self):
    self.tl()
    self.putm(2)
    self.m()
    self.putm(2)
    self.m()
    self.tr()
    self.m()
    self.put()
    self.tr()
    self.mm(2)
    self.put()
    self.ta()
    self.m()
    self.tr()
    self.m()
    self.tr()
    self.putm(2)
    self.m()
    self.putm(2)
    self.tl()
    self.mm(2)

  def d(self):
    self.tl()
    self.putm(5)
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.putm(2)
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.ta()
    self.mm(3)

  def n(self):
    self.tl()
    self.putm(5)
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
    self.mm(2)
    self.ta()
    self.putm(5)
    self.ta()
    self.mm(4)
    self.tl()
    self.mm(2)

  def one(self):
    """draws number 1 using beepers"""
    self.tl()
    self.mm(4)
    self.ta()
    self.putm(5)
    self.tl()
    self.mm(2)

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

  def lic(self) -> bool:
    """Left is Clear"""
    if left_is_clear():
      return True
    else:
      return False

  def lib(self) -> bool:
    """Left is blocked"""
    return not self.lic()

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

  def srcarpet(self):
    """Small Room Carpet"""
    if self.fib():
      if self.rib():
        if self.lib():
          self.put()

  def mm(self, num):
    """move multiple times"""
    for number in range(0,num):
      self.m()

  def putm(self,num):
    """put multiple times"""
    for i in range(num - 1):
        self.put()
        self.m()
    self.put()

  def pickm(self, num):
    """pick multiple times"""
    for _ in range(num - 1):
        self.pick()
        self.m()
    self.pick()

  def SOB(self) -> bool:
    """Standing on Beeper"""
    return beepers_present()

  def supercarpet(self):
    """supercarpet for 59"""
    while not self.fib():
      self.put()
      self.m()
    self.tr()

  def plant(self):
        """planting for k58"""
        while self.lib():
            self.put()
            if self.fib():
              if self.lic():
                self.tl()
              else:
                self.tr()
            self.m()
        if self.lic():
          self.tl()
          self.m()
          self.tl()
          self.m()
        else:
          self.tr()
          self.m()
          self.tr()
          self.m()
              
  def infinipick(self):
    """infinipick for k54"""
    while self.SOB():
      self.pick()
    self.mm(2)

  def jump(self):
    """Jump for 510"""
    while self.fic():
      self.m()
    self.tl()
    while self.rib():
      self.m()
    self.tr()
    self.m()
    self.tr()
    while self.fic():
      self.m()
    self.tl()

  def find(self):
    """find for 515"""
    while not facing_north():
      self.tl()
    self.m()
    if not self.SOB():
      self.tl()
      self.m()
      self.tl()
      self.m()
    for _ in range(2):
      if not self.SOB():
        self.m()
        self.tl()
        self.m()
    pass
    

def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.mm(4)
    kt.tl()
    kt.mm(4)
    kt.tr()
    while not kt.SOB():
      kt.plant()
    pass


if __name__ == "__main__":
    run_karel_program()