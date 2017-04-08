import RPi.GPIO as GPIO
import time

class NiksRobot:
	def __init__(self):
		#setup
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(7,GPIO.OUT)
		GPIO.setup(11,GPIO.OUT)
		GPIO.setup(13,GPIO.OUT)
		GPIO.setup(15,GPIO.OUT)
		print 'setup complete'
	def forward(self):
		GPIO.output(7,True)
		GPIO.output(11,False)
		GPIO.output(15,True)
		GPIO.output(13,False)
	def backward(self):
		GPIO.output(7,False)
		GPIO.output(11,True)
		GPIO.output(15,False)
		GPIO.output(13,True)
	def cleanup(self):
		GPIO.cleanup()
	def f(self):
		return 'forward'
	def r(self):
		print 'reverse'
	def l(self):
		print 'left'
	def r(self):
		print 'right'


print 'start'
nr = NiksRobot()
t=nr.f()
print t
u=nr.l()
nr.cleanup
print 'end'
#time.sleep(1)
#GPIO.output(7,False)
#GPIO.output(11,True)
#time.sleep(1)
#GPIO.output(11,False)
#GPIO.output(15,True)
#time.sleep(2.5)
#GPIO.output(13,False)
#GPIO.output(15,True)
#time.sleep(2.5)
#GPIO.output(15,False)
#GPIO.cleanup()
