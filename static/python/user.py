from itertools import count
import os

class User():
  _ids = count(0)

  def __init__(self, name):
    self.id = next(self._ids)
    self.name = name

  def __str__(self):
    return self.name + " id:" + str(self.id)
  # de creeat folder la inregistrare

def getId(nume, users):
    for user in users:
      if nume == user.name:
        return user.id
      
    return -1

  # de creeat o baza de date pentru useri