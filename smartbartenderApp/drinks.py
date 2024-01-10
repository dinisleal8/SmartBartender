#import RPi.GPIO as GPIO
import time
from django.contrib import admin
from django.urls import path 
from GPIOEmulator.EmulatorGUI import GPIO
from django.http import HttpResponse
from django.shortcuts import render, redirect

GPIO.setwarnings(False)

def drink1(request):

    try:
        bomba1 = 17
        bomba2 = 21
        bomba3 = 22
        bomba4 = 23
        bomba5 = 24 
        bomba6 = 25
        luz = 26

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(bomba1, GPIO.OUT)
        GPIO.setup(bomba2, GPIO.OUT)
        GPIO.setup(bomba3, GPIO.OUT)
        GPIO.setup(bomba4, GPIO.OUT)
        GPIO.setup(bomba5, GPIO.OUT)
        GPIO.setup(bomba6, GPIO.OUT)
        GPIO.setup(luz, GPIO.OUT)


        # GPIO.output(bomba1, GPIO.HIGH)
        # GPIO.output(bomba2, GPIO.HIGH)
        # GPIO.output(bomba3, GPIO.HIGH)
        # GPIO.output(bomba4, GPIO.HIGH)
        GPIO.output(bomba5, GPIO.HIGH)
        GPIO.output(bomba6, GPIO.HIGH)

        GPIO.output(bomba1, GPIO.LOW)
        GPIO.output(bomba2, GPIO.LOW)
        GPIO.output(bomba3, GPIO.LOW)
        GPIO.output(bomba4, GPIO.LOW)

        GPIO.output(luz, GPIO.LOW)
        print('bombas e luz ligadas')

        time.sleep(2)

        GPIO.output(bomba2, GPIO.HIGH)
        GPIO.output(bomba3, GPIO.HIGH)
        GPIO.output(bomba4, GPIO.HIGH)

        time.sleep(2)
        GPIO.output(bomba1, GPIO.HIGH)
        GPIO.output(luz, GPIO.HIGH)
        
        time.sleep(1)
        GPIO.cleanup()
        return render(request, "conclued.html")

    except Exception as e:
        # Lidar com a exceção, se necessário
        print(f"Ocorreu uma exceção: {e}")

    finally:
        GPIO.cleanup()
        print('bombas e luz desligadas')

    return render(request, "conclued.html")

def drink2(request):

    try:
        bomba1 = 17
        bomba2 = 21
        bomba3 = 22
        bomba4 = 23
        bomba5 = 24 
        bomba6 = 25
        luz = 26

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(bomba1, GPIO.OUT)
        GPIO.setup(bomba2, GPIO.OUT)
        GPIO.setup(bomba3, GPIO.OUT)
        GPIO.setup(bomba4, GPIO.OUT)
        GPIO.setup(bomba5, GPIO.OUT)
        GPIO.setup(bomba6, GPIO.OUT)
        GPIO.setup(luz, GPIO.OUT)


        # GPIO.output(bomba1, GPIO.LOW)
        GPIO.output(bomba2, GPIO.LOW)
        GPIO.output(bomba3, GPIO.LOW)
        GPIO.output(bomba4, GPIO.LOW)
        GPIO.output(bomba5, GPIO.LOW)
        # GPIO.output(bomba6, GPIO.LOW)

        GPIO.output(bomba1, GPIO.HIGH)
        GPIO.output(bomba6, GPIO.HIGH)

        GPIO.output(luz, GPIO.HIGH)
        print('bombas e luz ligadas')

        time.sleep(9)

        GPIO.output(bomba6, GPIO.HIGH)

        time.sleep(9)
        GPIO.output(bomba1, GPIO.HIGH)
        
        time.sleep(1)
        GPIO.cleanup()
        return render(request, "conclued.html")

    except Exception as e:
        # Lidar com a exceção, se necessário
        print(f"Ocorreu uma exceção: {e}")

    finally:
        GPIO.cleanup()
        print('bombas e luz desligadas')

    return render(request, "conclued.html")

def drink3(request):


    try:
        bomba1 = 17
        bomba2 = 21
        bomba3 = 22
        bomba4 = 23
        bomba5 = 24 
        bomba6 = 25
        luz = 26

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(bomba1, GPIO.OUT)
        GPIO.setup(bomba2, GPIO.OUT)
        GPIO.setup(bomba3, GPIO.OUT)
        GPIO.setup(bomba4, GPIO.OUT)
        GPIO.setup(bomba5, GPIO.OUT)
        GPIO.setup(bomba6, GPIO.OUT)
        GPIO.setup(luz, GPIO.OUT)


        # GPIO.output(bomba1, GPIO.LOW)
        GPIO.output(bomba2, GPIO.LOW)
        GPIO.output(bomba3, GPIO.LOW)
        GPIO.output(bomba4, GPIO.LOW)
        GPIO.output(bomba5, GPIO.LOW)
        # GPIO.output(bomba6, GPIO.LOW)

        GPIO.output(bomba1, GPIO.HIGH)
        GPIO.output(bomba6, GPIO.HIGH)

        GPIO.output(luz, GPIO.HIGH)
        print('bombas e luz ligadas')

        time.sleep(9)

        GPIO.output(bomba6, GPIO.HIGH)

        time.sleep(9)
        GPIO.output(bomba1, GPIO.HIGH)
        
        time.sleep(1)
        GPIO.cleanup()
        return render(request, "conclued.html")

    except Exception as e:
        # Lidar com a exceção, se necessário
        print(f"Ocorreu uma exceção: {e}")

    finally:
        GPIO.cleanup()
        print('bombas e luz desligadas')

    return render(request, "conclued.html")

def drink4(request):

    try:
        bomba1 = 17
        bomba2 = 21
        bomba3 = 22
        bomba4 = 23
        bomba5 = 24 
        bomba6 = 25
        luz = 26

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(bomba1, GPIO.OUT)
        GPIO.setup(bomba2, GPIO.OUT)
        GPIO.setup(bomba3, GPIO.OUT)
        GPIO.setup(bomba4, GPIO.OUT)
        GPIO.setup(bomba5, GPIO.OUT)
        GPIO.setup(bomba6, GPIO.OUT)
        GPIO.setup(luz, GPIO.OUT)


        # GPIO.output(bomba1, GPIO.LOW)
        GPIO.output(bomba2, GPIO.LOW)
        GPIO.output(bomba3, GPIO.LOW)
        GPIO.output(bomba4, GPIO.LOW)
        GPIO.output(bomba5, GPIO.LOW)
        # GPIO.output(bomba6, GPIO.LOW)

        GPIO.output(bomba1, GPIO.HIGH)
        GPIO.output(bomba6, GPIO.HIGH)

        GPIO.output(luz, GPIO.HIGH)
        print('bombas e luz ligadas')

        time.sleep(9)

        GPIO.output(bomba6, GPIO.HIGH)

        time.sleep(9)
        GPIO.output(bomba1, GPIO.HIGH)
        
        time.sleep(1)
        GPIO.cleanup()
        return render(request, "conclued.html")

    except Exception as e:
        # Lidar com a exceção, se necessário
        print(f"Ocorreu uma exceção: {e}")

    finally:
        GPIO.cleanup()
        print('bombas e luz desligadas')

    return render(request, "conclued.html")

def drink5(request):

    try:
        bomba1 = 17
        bomba2 = 21
        bomba3 = 22
        bomba4 = 23
        bomba5 = 24 
        bomba6 = 25
        luz = 26

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(bomba1, GPIO.OUT)
        GPIO.setup(bomba2, GPIO.OUT)
        GPIO.setup(bomba3, GPIO.OUT)
        GPIO.setup(bomba4, GPIO.OUT)
        GPIO.setup(bomba5, GPIO.OUT)
        GPIO.setup(bomba6, GPIO.OUT)
        GPIO.setup(luz, GPIO.OUT)


        # GPIO.output(bomba1, GPIO.LOW)
        GPIO.output(bomba2, GPIO.LOW)
        GPIO.output(bomba3, GPIO.LOW)
        GPIO.output(bomba4, GPIO.LOW)
        GPIO.output(bomba5, GPIO.LOW)
        # GPIO.output(bomba6, GPIO.LOW)

        GPIO.output(bomba1, GPIO.HIGH)
        GPIO.output(bomba6, GPIO.HIGH)

        GPIO.output(luz, GPIO.HIGH)
        print('bombas e luz ligadas')

        time.sleep(9)

        GPIO.output(bomba6, GPIO.HIGH)

        time.sleep(9)
        GPIO.output(bomba1, GPIO.HIGH)
        
        time.sleep(1)
        GPIO.cleanup()
        return render(request, "conclued.html")

    except Exception as e:
        # Lidar com a exceção, se necessário
        print(f"Ocorreu uma exceção: {e}")

    finally:
        GPIO.cleanup()
        print('bombas e luz desligadas')

    return render(request, "conclued.html")

def drink6(request):

    try:
        bomba1 = 17
        bomba2 = 21
        bomba3 = 22
        bomba4 = 23
        bomba5 = 24 
        bomba6 = 25
        luz = 26

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(bomba1, GPIO.OUT)
        GPIO.setup(bomba2, GPIO.OUT)
        GPIO.setup(bomba3, GPIO.OUT)
        GPIO.setup(bomba4, GPIO.OUT)
        GPIO.setup(bomba5, GPIO.OUT)
        GPIO.setup(bomba6, GPIO.OUT)
        GPIO.setup(luz, GPIO.OUT)


        # GPIO.output(bomba1, GPIO.LOW)
        GPIO.output(bomba2, GPIO.LOW)
        GPIO.output(bomba3, GPIO.LOW)
        GPIO.output(bomba4, GPIO.LOW)
        GPIO.output(bomba5, GPIO.LOW)
        # GPIO.output(bomba6, GPIO.LOW)

        GPIO.output(bomba1, GPIO.HIGH)
        GPIO.output(bomba6, GPIO.HIGH)

        GPIO.output(luz, GPIO.HIGH)
        print('bombas e luz ligadas')

        time.sleep(9)

        GPIO.output(bomba6, GPIO.HIGH)

        time.sleep(9)
        GPIO.output(bomba1, GPIO.HIGH)
        
        time.sleep(1)
        GPIO.cleanup()
        return render(request, "conclued.html")

    except Exception as e:
        # Lidar com a exceção, se necessário
        print(f"Ocorreu uma exceção: {e}")

    finally:
        GPIO.cleanup()
        print('bombas e luz desligadas')

    return render(request, "conclued.html")
