#Strong  typing 
class Duck:
  def walk(self):
    print("duck walk")
    
class Horse:
  def walk(self):
    print('horse walk')

class Cat:
  def talk(self):
    print("cat talk:")
  
def myFunction(obj):
  if hasattr(obj,"walk"): 
    obj.walk()
  if hasattr(obj,'talk'):
    obj.talk()


d = Duck()  #duck object created
myFunction(d) 

h = Horse() #horse object created
myFunction(h)

c = Cat()  #this will give error 
myFunction(c) 

