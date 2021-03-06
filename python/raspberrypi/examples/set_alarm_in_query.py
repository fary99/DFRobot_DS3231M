#-*- coding: utf-8 -*-
'''
file set_alarm_in_query.py

@brief Through the example, you can set alarm clock in query:
@n     Experiment phenomenon: read data every 1 seconds and print it on terminal.

@Copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
@licence   The MIT License (MIT)

@author [LuoYufeng](yufeng.luo@dfrobot.com)
@url https://github.com/DFRobot/DFRobot_DS3231M
@version  V1.0
@date  2020-2-12
'''
import sys
sys.path.append('../')
import time
from DFRobot_DS3231M import *

rtc = DFRobot_DS3231M(bus=1)

#begin return True if succeed, otherwise return False
while not rtc.begin():
    time.sleep(2)

'''
@brief Set the vaule of pin sqw
@param mode OFF             = 0x01 # Not output square wave, enter interrupt mode
@n          SquareWave_1Hz  = 0x00 # 1Hz square wave
@n          SquareWave_1kHz = 0x08 # 1kHz square wave
@n          SquareWave_4kHz = 0x10 # 4kHz square wave
@n          SquareWave_8kHz = 0x18 # 8kHz square wave
'''
rtc.write_sqw_pin_mode(rtc.SquareWave_1Hz)
'''
@brief Read the value of pin sqw
@return mode OFF             = 0x01 # Off
@n           SquareWave_1Hz  = 0x00 # 1Hz square wave
@n           SquareWave_1kHz = 0x08 # 1kHz square wave
@n           SquareWave_4kHz = 0x10 # 4kHz square wave
@n           SquareWave_8kHz = 0x18 # 8kHz square wave
'''
#rtc.read_sqw_pin_mode()
'''
@brief Set the last compiled time as the current time
'''
#rtc.dateTime()#If users use this function, please don't set time by other way
rtc.set_year(19)#Set year, default in the 21st century, input negative number for years in the 20th century.
rtc.set_month(10)#Set the months in 1-12
rtc.set_date(23)#Set the dates in 0-31
'''
@brief Set the hours and 12hours or 24hours
@param hour:1-12 in 12hours,0-23 in 24hours
@param mode:H24hours,AM,PM
'''
rtc.set_hour(1,rtc.H24hours)
rtc.set_minute(58)#Set the minutes in 0-59
rtc.set_second(55)#Set the seconds in 0-59

rtc.adjust()#Set status on work
'''
@brief Set alarm clock
@param alarmType:EverySecond,
@n               SecondsMatch,
@n               SecondsMinutesMatch,
@n               SecondsMinutesHoursMatch,
@n               SecondsMinutesHoursDateMatch,
@n               SecondsMinutesHoursDayMatch, #Alarm1
@n               EveryMinute,
@n               MinutesMatch,
@n               MinutesHoursMatch,
@n               MinutesHoursDateMatch,
@n               MinutesHoursDayMatch,        #Alarm2
@n               UnknownAlarm
@param days      Alarm clock Day (day)
@param hours     Alarm clock Hour (hour)
@param mode:     H24hours, AM, PM
@param minutes   Alarm clock (minute)
@param seconds   Alarm clock (second)
'''
rtc.set_alarm(alarmType=rtc.SecondsMinutesHoursDayMatch,date=23,hour=1,mode=rtc.H24hours,minute=59,second=0)
'''
@brief disable the 32k output (default is enable)
'''
#rtc.disAble32k();

'''
@brief enable the 32k output 
'''
#rtc.enAble32k();

def main():
    while True:
        if rtc.is_alarm() == True:
            print("Alarm clock is triggered.")
            rtc.clear_alarm()
        #如果您不是很熟悉python，可以这样打印
        '''
        print(rtc.get_year()),
        print("/"),
        print(rtc.get_month()),
        print("/"),
        print(rtc.get_date()),
        print(","),
        print(rtc.get_day_of_the_week()),
        print(","),
        print(rtc.get_hour()),
        print(":"),
        print(rtc.get_minute()),
        print(":"),
        print(rtc.get_second()),
        print(","),
        print(rtc.get_AM_or_PM())
        '''
        #5.如果您很熟悉python，可以这样打印数据
        print("{0}/{1}/{2},{3},{4}:{5}:{6},{7}".format(rtc.get_year(),rtc.get_month(),rtc.get_date(),\
        rtc.get_day_of_the_week(),rtc.get_hour(),rtc.get_minute(),rtc.get_second(),rtc.get_AM_or_PM()))#print now time
        
        print(" ")
        time.sleep(1)

if __name__ == "__main__":
    main()