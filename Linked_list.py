#Linked List
class Node:
  def __init__(self,v=None):
    self.value = v
    self.next = None
    #return
  def isempty(self):
    if self.value == None:
      return(True)
    else:
      return(False)

  def append(self,v):
    if self.isempty():
      self.value = v
    elif self.next == None:
      self.next = Node(v)
    else:
      self.next.append(v)
    #return

  def delete(self,v):
    if self.isempty():
      return
    if self.value == v:
      self.value = None
      if self.next != None:
        self.value = self.next.value
        self.next = self.next.next
      #return
    else:
      if self.next != None:
        self.next.delete(v)
        if self.next.value == None:
          self.next = None
    #return

  def display(self):
    if self.isempty():
      print("None")
    else:
      temp = self
      while temp!=None:
        print(temp.value,end=" ")
        temp = temp.next

head = Node(10)
head.append(20)
head.append(40)
head.append(80)
head.delete(20)
head.append(30)
head.display()
    
      
  
    