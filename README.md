# lcd16x2_f_py_script
Python script for the LCD 16x2 in Raspberry Pi 3. 
Show some examples about SSH status, FTP, public IP, CPU speed & temperature, etc.
To work you need "Adafruits_Python_CharLCD", you can found here: https://github.com/adafruit/Adafruit_Python_CharLCD

For the scripts as FTP status you should create a ".sh" file with this command:

sudo service vsftpd status | grep active | awk '{print $2,$9,$10}'

For the last remote user connect: 

sudo lastb | awk 'NR==1{print $2;exit}'

And his IP:

sudo lastb | awk 'NR==1{print $3;exit}'




Some examples of LCD:
![alt text](https://raw.githubusercontent.com/FSFRS/lcd16x2_f_py_script/master/images/IMG_20180512_161308.jpg)

![alt text](https://raw.githubusercontent.com/FSFRS/lcd16x2_f_py_script/master/images/IMG_20180512_161310.jpg)

![alt text](https://raw.githubusercontent.com/FSFRS/lcd16x2_f_py_script/master/images/IMG_20180512_161312.jpg)
