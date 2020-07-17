from itertools import count
import os

class User():
  _ids = count(0)

  def __init__(self, name):
    self.id = next(self._ids)
    self.name = name

    self.createUserFolder()

  def __str__(self):
    return self.name + " id:" + str(self.id)
  # de creeat folder la inregistrare

  def createUserFolder(self):
    # daca nu exista folder pentru upload, il creem
    if not os.path.exists('uploaded-files/'):
      os.makedirs('uploaded-files/')

    path = 'uploaded-files/' + str(self.id)
    
    if not os.path.exists(path):
      os.makedirs(path)

def getId(nume, users):
    for user in users:
      if nume == user.name:
        return user.id
      
    return -1

def saveUsers(users):
  fi = open('static/python/users.txt', 'w+')

  for user in users:
    fi.write(str(user.name) + '\n')

  fi.close()

def loadUsers():
  users = []
  fi = open('static/python/users.txt', 'r')

  for line in fi:
    users.append(User(line[:-1]))# username fara ultimele 2 caractere ('\n')

  fi.close()
  return users

