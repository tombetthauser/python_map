class JobSeeker:
  def hello(self, name='nobody'):
    print ("Hello, %s!" % name)

js = JobSeeker()
js.hello()
js.hello('Tom')