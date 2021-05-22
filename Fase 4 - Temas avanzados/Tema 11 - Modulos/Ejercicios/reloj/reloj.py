import datetime
import time
import os

while True:
	os.system('cls')
	dt = datetime.datetime.now()
	dt = dt.strftime('Son las %I con %M minutos con %S segundos')
	print(dt)
	time.sleep(1)