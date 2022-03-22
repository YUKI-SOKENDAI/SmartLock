## default library
import binascii
import RPi.GPIO as GPIO
import time
import datetime
#from retry import retry
import numpy as np

## external library
import nfc
import pandas as pd

## my library


## define system global variable 
# door status
DOOR_OPEN = 1
DOOR_CLOSE = 0
# room status
NO_PERSON = 0x00
OKADA_IN = 0x01
TAKAHASHI_IN = 0x02
ABE_IN = 0x04
FRESHMAN_ID = 0x08
 

class NFCReader(object):
	def on_connect(self, tag):
		print("touched")
		self.idm = binascii.hexlify(tag.idm)
		return True
   # @retry
	def read_id(self):
		clf = nfc.ContactlessFrontend('usb')
		try:
			clf.connect(rdwr={'on-connect': self.on_connect})
		except Exception as e:
			self.idm = None
			clf.close()
		else:
			clf.close()
		finally:
			clf.close()

def make_servo_pulse(gp_out, door_state):
	# pulse width, 0.75ms=0deg(min), 1.75ms=90deg, 2.2ms=120deg(max) 
	GPIO.output(gp_out, 0)
	t_now=datetime.datetime.now()
	stamp=str(t_now.year)+"/"+str(t_now.month)+"/"+str(t_now.day)+"-"+str(t_now.hour)+":"+str(t_now.minute)+":"+str(t_now.second)
	if door_state:
		p_ms_width=1.75
		print (stamp + " SOKENDAI DOOR OPEN!")
	else:
		p_ms_width=0.75
		print (stamp + " SOKENDAI DOOR CLOSE!")
	p_ms_width /= 1000 # unit convert to ms
	
	for i in range(50):
		GPIO.output(gp_out, 1)
		time.sleep(p_ms_width)
		GPIO.output(gp_out, 0)
		time.sleep(p_ms_width)
	time.sleep(.5)

def roommate_statement(touch_id, member_trig, idlist):
	pass # update member statement and act each indication 

def read_card_id(data_path="./CardID/CardIDList.dat"):
	card_info = pd.read_csv(data_path,encoding="utf-8")

	list_array=[]
	for list in card_info["ID"]:
		# print ("list test: ",list)
		print ("card ID(bytes): ",list.encode())
		list_array.append(list.encode())
	card_info["IDbyte"]=list_array
	print (card_info["IDbyte"])

	return card_info

if __name__ == '__main__':
	try:
		print ("Smart lock system boot!")
		print ("*** Start Smart key initial process")
		GPIO.setmode(GPIO.BCM)
		gp_out = 4
		servo_pwr = 5
		door_state = 6
			
		GPIO.setup(gp_out, GPIO.OUT)
		GPIO.setup(servo_pwr, GPIO.OUT)
		GPIO.setup(door_state, GPIO.OUT)
			#servo = GPIO.PWM(gp_out, 400)
		reader = NFCReader()
		GPIO.output(servo_pwr, 0)
		
		GPIO.output(door_state, DOOR_CLOSE)
		
		GPIO.output(servo_pwr, 1)
		time.sleep(1)
		make_servo_pulse(gp_out, DOOR_CLOSE)
		make_servo_pulse(gp_out, DOOR_CLOSE)
		
		# define statement 
		door_trig=DOOR_CLOSE
		member_trig=NO_PERSON
		
		GPIO.output(servo_pwr, 0)
		
		
		# read dat file(later)
		card_info=read_card_id(data_path="./CardID/CardIDList.dat")
		# print (card_info["ID"])
		idlist = [b'012e4cd28e178979', b'012e48b1f6117294', b'012e48b1f61171ac', b'012e48b1f6117294', b'012e4cd257c3387a',b'01010a10c2172e27',b'012e48b1f6109680']
		idlist2 = list(card_info["IDbyte"])
		print ('card_info["IDbyte"]: \n',card_info["IDbyte"],type(card_info["IDbyte"][0]))
		print ("idlist: \n",idlist,type(idlist[0]))
		# print ("idlist2: \n",idlist2,type(idlist2[0]))



		# print(card_info["ID"].encode()) ## nai

		#servo.start(0.0)

		print ("*** Start Smart key process")

		while True:
			print("touch card:")
			reader.read_id()
			cardid = reader.idm
			# print(reader.idm)
			print(cardid)

			# print (cardid in idlist2,cardid in list(idlist2),cardid in idlist, "Read Card ID: ", cardid, ", Card IDlist:",idlist2)

			# if cardid in idlist:
			if cardid in idlist2:
				door_trig = ~door_trig
				print ("door_trig : ", door_trig)
				GPIO.output(servo_pwr, 1) # servo pwr supply ON
				time.sleep(1)

				#servo.start(40)
						#servo.ChangeDutyCycle(40)
				#time.sleep(.02)
				#servo.ChangeDutyCycle(80)
						#time.sleep(.02)
						#servo.ChangeDutyCycle(60)
				#time.sleep(.02)
				
				make_servo_pulse(gp_out, door_trig) # servo pulse make myself to avoid pulse width jitter effect
				GPIO.output(door_state, door_trig)		

				print(reader.idm)
				IDindex=idlist2.index(cardid)
				print ("User Name: ", card_info["Name"][IDindex], " released")

				GPIO.output(servo_pwr, 0)
				time.sleep(.5)
				
				roommate_statement(cardid, member_trig, idlist)
				#servo.stop()
			else:
		   		print ("No one exist in the ID lists.")

	finally:
		#servo.stop()
		GPIO.output(gp_out, 0)
		GPIO.output(door_state, 0)
		
		GPIO.output(servo_pwr, 1)
		time.sleep(1)
		make_servo_pulse(gp_out, DOOR_CLOSE)
		make_servo_pulse(gp_out, DOOR_CLOSE)
		GPIO.output(servo_pwr, 0)
		print ("Smart lock system down...")
