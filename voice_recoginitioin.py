import speech_recognition as sr
import pyfirmata2
board = pyfirmata2.Arduino('COM5')

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
while(1):
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)  
            audio = r.listen(source)
        result=r.recognize_google(audio)
        print(result)
        if(result=='switch on bulb'):
            board.digital[13].write(False)
            print("Bulb on")
        elif(result=='switch off bulb'):
            board.digital[13].write(True)
            print("Bulb off")
        elif(result=='switch on charger'):
            board.digital[12].write(False)
            print("Charger on")
        elif(result=='switch off charger'):
            board.digital[12].write(True)
            print("Cahrger off")
        elif(result=='switch on mosquito repellent'):
            board.digital[10].write(False)
            print("replent on")
        elif(result=='switch off mosquito repellent' or result=='off mosquito repellent' or result=='which of mosquito repellent'):
            board.digital[10].write(True)
            print("replent off")
        elif(result=='switch on laptop'):
            board.digital[9].write(False)
            print("Charger laptop on")
        elif(result=='switch off laptop'):
            board.digital[9].write(True)
            print("Charger off")
        elif(result=='turn off'):
            print("the program is closed")
            break
    except:
        print("ERROR")
        continue
