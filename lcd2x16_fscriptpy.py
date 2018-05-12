#!/usr/bin/python
# Importar librerias
import time
import Adafruit_CharLCD as LCD
import socket
import fcntl
import commands
import struct
import os
from time import sleep, strftime
from datetime import datetime
import RPi.GPIO as GPIO

# Raspberry Pi pin configuracion:
LCD_RS        = 25  # Elegir los pines correctos segun tabla BCM
LCD_EN        = 24
LCD_D4        = 23
LCD_D5        = 17
LCD_D6        = 18
LCD_D7        = 22
lcd_backlight = 4
lcd_columns = 16
lcd_rows    = 2

# Iniciar los pines de la tabla anterior
lcd = LCD.Adafruit_CharLCD(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7,
                           lcd_columns, lcd_rows, lcd_backlight)

# Definir la temperatura
def get_cpu_temp():
    tempFile = open("/sys/class/thermal/thermal_zone0/temp")
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000

# Definir IP
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s', ifname[:15]))[20:24])

# Definir velocidad de la CPU
def get_cpu_speed():    
    tempFile = open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq")
    cpu_speed = tempFile.read()
    tempFile.close()
    return float(cpu_speed)/1000

def main():
  # Bloque principal
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)       # Usa los GPIO BCM (Broadcom SOC channel) para numerar los conectores
    GPIO.setup(LCD_EN, GPIO.OUT)  # E
    GPIO.setup(LCD_RS, GPIO.OUT) # RS
    GPIO.setup(LCD_D4, GPIO.OUT) # DB4
    GPIO.setup(LCD_D5, GPIO.OUT) # DB5
    GPIO.setup(LCD_D6, GPIO.OUT) # DB6
    GPIO.setup(LCD_D7, GPIO.OUT) # DB7

    # Print a two line message
    while True:
        lcd.message(commands.getoutput('uname -or') + '\n' + datetime.now().strftime('%b %d  %H:%M:%S\n'))
        time.sleep(2.5)
        lcd.clear()
        # Siguiente mensaje
        lcd.message(("CPU Temp: " + str(round(get_cpu_temp()))) + '\n' + ("CPU Veloc: " + str(round(get_cpu_speed()))))
        time.sleep(2)
        lcd.clear()
        # Siguiente mensaje
        lcd.message(("Servicio VSFTP:") + '\n' + (commands.getoutput('sh ~/ftpactive.sh ')))
        time.sleep(2)
        lcd.clear()
        # Siguiente mensaje
        lcd.message(("Pi-Hole:") + '\n' + (commands.getoutput('sh ~/piholeactive.sh ')))
        time.sleep(2)
        lcd.clear()
        # Siguiente mensaje
        lcd.message(("IP de red local:") + '\n' + (get_ip_address('eth0')))
        time.sleep(2)
        lcd.clear()
        # Siguiente mensaje
        #lcd.message(commands.getoutput('curl v4.ifconfig.co/country') + '\n' + (commands.getoutput('curl v4.ifconfig.co')))
        #time.sleep(2.5)
        #lcd.clear()
        # Siguiente mensaje
        lcd.message(("Intruso:") + (commands.getoutput('sh ~/lastuserssh1.sh')) +'\n' + (commands.getoutput('sh /home/pi/comscripts/lastuserssh2.sh')))
        time.sleep(3.5)
        lcd.clear()
        # Turn backlight on.
        #lcd.set_backlight(1)

if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            pass
        finally:
            lcd.clear()
            time.sleep(1)
            lcd.message('Adios!')
            GPIO.cleanup()