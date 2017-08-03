import serial
import threading
import unity as ut

def getArduinoDatas(ser,x):
    try:
       # print("alive check!")
        s = ser.readline()
        print(s)
        allThing = str(s).split("b")
        allThing = allThing[1].split(" ")
        parameter = allThing[0]
        if(parameter == "'HT11"):
            print(allThing)

            print("Temperature:"+ str(allThing[2]))
            print("humidity:"+str(allThing[4]))
            return(
                {
                    "Temp": str(allThing[2]),
                    "Humi":str(allThing[4])
                }
            )

    except Exception as e:
        print(e)




if __name__ == '__main__':

    ser = serial.Serial('COM6', 9600, timeout=100000)
    # read one byte
    x = ser.read()
    while(1):
        getArduinoDatas(ser,x)

    ser.close()

