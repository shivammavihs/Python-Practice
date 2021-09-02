import datetime, time
from pygame import mixer
from threading import Thread
import os

def play_sound(file_name,func,stopper):
    print('Inside play sound')
    file_name = f'.\Sounds\{file_name}'
    mixer.init()
    mixer.music.load(file_name)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while True:
        a = input(f'Write "{stopper}" to stop the alarm.')
        if a.upper() == stopper: 
            mixer.music.stop()
            func()
        else: 
            print(f'Write {stopper} properly.')
    

def date_arith(time):
    date = datetime.date(1, 1, 1)
    return datetime.datetime.combine(date, time)

def  for_exercise():
    print('for exercise running')
    time.sleep(45*60)
    play_sound('Alarm_Exercise.wav', for_exercise, stopper='EXERCISE')

def  for_eyes():
    print('for eyes running')
    global current, final
    if date_arith(datetime.datetime.now().time()) >= final:
        print('exit message')
        print('Time Passed')
        os._exit(1)
    time.sleep(0.1*60)
    print(current, final)
    play_sound('Bird_Eyes.mp3', for_eyes, stopper='EYES')

def for_water():
    print('for water runnning')
    global final, current
    elapsed = final - current
    alarm_durtion = elapsed/8
    time.sleep(alarm_durtion.seconds)
    play_sound('Gargling_Water.mp3', for_water, stopper='DRANK')
    
eligible_time = date_arith(datetime.time(16,30,0))

final = date_arith(datetime.time(17,30,00))

current = date_arith(datetime.datetime.now().time())

if current < eligible_time:
    t1 = Thread(target=for_water)
    t2 = Thread(target=for_exercise)
    t3 = Thread(target=for_eyes)
    t1.start()
    t2.start()
    t3.start()
        