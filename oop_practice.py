class JobSeeker:
  def __init__(self, name):
    self.name = name

  def hello(self, name='nobody'):
    print ("Hello, %s! My name is %s." % (name, self.name))

js = JobSeeker("Garon")
js.hello()
js.hello('Tom')