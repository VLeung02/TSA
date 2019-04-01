import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

in1 = 24
in2 = 23
en = 25
temp1=1
pin_to_circuit = 4
GPIO.setup(in1,GPIO.OUT) 
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(75)
print("speed is at 75%")
print ('******************************************************************')
print ('DOCTOR, FAMILYMAN, COMMISSIONER, BODYBUILDER')
print ('REMEMBER TO CALIBRATE')
print ('******************************************************************')

def rc_time (pin_to_circuit):
    count = 0
   
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(1)
 
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count


try:
	while True:
		x=rc_time(pin_to_circuit)
		print x
		if x > 200000:
			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in2,GPIO.LOW)
			p.ChangeDutyCycle(20)
			print ("forwards")
			time.sleep(01)
		else:
			print ("idle")
       
		if x < 15000:
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.HIGH)
			p.ChangeDutyCycle(20)
			print ("backwards")
			time.sleep(0.1)
		else:
			print ("idle")

		if x < 200000:
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in1,GPIO.LOW)
			p.ChangeDutyCycle(20)
			print("idle")
			time.sleep(0.1)
		else:
			print ("goodgoodgood")
			
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()