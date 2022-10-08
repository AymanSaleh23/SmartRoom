
"""
----------------------------------------------------
------ Author: Ayman Saleh        ------------------ 
------ Date  : 8/OCT/2022         ------------------ 
------ Version: V.1.0.0           ------------------ 
------ Type   : Smart Room        ------------------ 
----------------------------------------------------

"""
#   Import all needed Modules
import tkinter
from tkinter import ttk
import threading
import winsound


#   Some global variables as indecators
HoursIndex    = 0
MinutesIndex  = 1
SecondsIndex  = 2
DayLightIndex = 3

LightON = True
LightOFF = False

FanON = True
FanOFF = False

AlarmStatus = False
alarmValue = 0

#   Data container
state = {
    "time" : [0,0,0,'AM'],
    "Light": LightOFF,
    "Fan"  : FanOFF,
    "Alarm": alarmValue,
    "AlarmSeconds": 0
    }

#   Main frame 
mainFrame = tkinter.Tk()
mainFrame.title("Smart Room System")

#   Configuration and setting frame 
ConfigFrame = tkinter.Tk()
ConfigFrame.title("Configuration Room System")

#   Control frame 
ControlFrame = tkinter.Tk()
ControlFrame.title("Control Room System")

#   Updatable Lable for display Clock
ClockLable = tkinter.Label(mainFrame, font = ('calibri', 70, 'bold'),
                           background = 'purple',foreground = 'white',
                           text=state["time"])
ClockLable.grid(row = 0, column = 0)

#   Updatable Lable for display Room Status
StateLable = tkinter.Label(mainFrame, font = ('calibri', 25, 'bold'),
                           foreground = 'black', text=state["time"])
StateLable.grid(row = 1, column = 0)

#   Finction For Turn Led On
def onLight():
    global LightON
    global state
    state["Light"] = LightON
    print("Light: " + str(state["Light"]))

#   Finction For Turn Led Off
def offLight():
    global LightOFF
    global state
    state["Light"] = LightOFF
    print("Light: " + str(state["Light"]))

#   Finction For Turn Fan On
def onFan():
    global FanON
    global state
    state["Fan"] = FanON
    print("Fan: " + str(state["Fan"]))

#   Finction For Turn Fan Off
def offFan():
    global FanOFF
    global state
    state["Fan"] = FanOFF
    print("Fan: " + str(state["Fan"]))

#   Finction For Test data (debugging porpuses)
def testRoom():
    global state
    for i in state:    
        print(str(i)+ " : "+ str(state[i]))

#   Finction to update data every second
def clock():
    global state
    global ClockLable
    global AlarmStatus
    
    #   construct the data to display
    timeToDisplay = str(state["time"][HoursIndex])+':'+str(state["time"][MinutesIndex])+':'+str(state["time"][SecondsIndex])+ "  " + str(state["time"][DayLightIndex])
    print(state)
    print(timeToDisplay)
    
    # exception handling for any fault may occure
    try:
        ClockLable.config(text = str(timeToDisplay) )
    except:
        print("warning")
    stateToMonitor = ""
    
    #   Display the Data Dictionary (container)
    for i in state:
        if i == "time":
            # exception handling for any fault may occure
            try:
                ClockLable.config(text = str(timeToDisplay) )
            except:
                print("warning")
        else:
            stateToMonitor = stateToMonitor + " "+ str(i) +" " + str(state[i])+"\n"
    
    # exception handling for any fault may occure
    try:
        StateLable.config(text = str(stateToMonitor) )
    except:
        print("warning")
    
    #   Check if alarm is activated
    if AlarmStatus == True:
        #   Count up on Alarm second counter
        state["AlarmSeconds"] = state["AlarmSeconds"] +1    
        
        #   Check Alarm second counter if pass 1 minute
        if state["AlarmSeconds"] > 60:
            #   reset Alarm second counter
            state["AlarmSeconds"] = 0
            #   Count down on Alarm minute counter
            state["Alarm"] = state["Alarm"] - 1 
            
            #   Check if all Alarm minutes are consumed
            if state["Alarm"] == 0:
                #   Reset Alarm Flag
                winsound.Beep(750,750)
                
                AlarmStatus = False
    
    # Second Test < 60 
    if  state["time"][SecondsIndex] + 1 < 60:
        #   Count up Container seconds
        state["time"][SecondsIndex] = state["time"][SecondsIndex] + 1
    # Second Test == 60
    else:
        #   Reset Container seconds
        state["time"][SecondsIndex] = 0
        
        # Minute Test < 60
        if state["time"][MinutesIndex] + 1 < 60:
            #   Count up Container Minutes
            state["time"][MinutesIndex] = state["time"][MinutesIndex] + 1
        
        # Minute Test == 60
        else :
            #   Reset Container Minutes
            state["time"][MinutesIndex] = 0
            # Hour Test < 12
            if state["time"][HoursIndex] + 1 < 12:
                #   Count up Container Hours
                state["time"][HoursIndex] = state["time"][HoursIndex] + 1
            # Hour Test == 12
            else:
                #   Reset Container Hours
                state["time"][HoursIndex] = 0
                
                # Change Day Light into AM or PM
                if str(state["time"][DayLightIndex]) == "AM":
                    state["time"][DayLightIndex] = "PM"
                    
                elif str(state["time"][DayLightIndex]) == "PM":
                    state["time"][DayLightIndex] = "AM"
    
    #   Set a Software Timer for 1 second
    threading.Timer(1,clock).start()
   
#   Function to set Alarm minutes
def AlarmSet():
    global AlarmStatus 
    
    # exception handling for any fault may occure
    try:
        #    Get the Entry value in the system
        state["Alarm"] = int(str(AlarmEntry.get()))
        
        #    Reset the last Alarm counter
        state["AlarmSeconds"] = 0
        
        #    print the inserted value for debugging purposes
        print ("Got : "+ str(state["Alarm"]))
        
        #   Set the Alarm Flag
        AlarmStatus = True
    except:
        print("Error Alarm Time in minutes")
    
#   Function For Configure Clock
def UpadteTimeDay():
    global AlarmStatus 
    
    # exception handling for any fault may occure
    try:
        #   Get Seconds from user
        state["time"][SecondsIndex] = int(str(SecConfigEntry.get()))
    except:
        print("Error Second Configuration")

    # exception handling for any fault may occure
    try:
        #   Get Minutes from user
        state["time"][MinutesIndex] = int(str(MinConfigEntry.get()))
    except:
        print("Error Minutes Configuration")

    # exception handling for any fault may occure
    try:
        #   Get Hours from user
        state["time"][HoursIndex]   = int(str(HConfigEntry.get()))
    except:
        print("Error Hour Configuration")
    # exception handling for any fault may occure
    try:
        #   Get Day Light from user
        print ("Comp "+str(DConfigCombo.current()))
        if DConfigCombo.current()== 0:
            state["time"][DayLightIndex] = "AM"    
        elif DConfigCombo.current() == 1:
            state["time"][DayLightIndex] = "PM"
        
        #   Reset Alarm Seconds
        state["AlarmSeconds"] = 0
        #   Reset Alarm Flag
        state["Alarm"] = 0
        AlarmStatus = False
        
    except:
        print("Error Hour Configuration")
        
    #   Print Current Container Values
    print(state)
        
#   Function for display Control Frame
def ctrlFrame():
    print("Generate ctrl Frame")
    
    ControlFrame.mainloop()
    
#   Function for display Configuration Frame
def configFrame():
    print("Generate config Frame")
    
    ConfigFrame.mainloop()
    
#   Lable for Light
LightLable = tkinter.Label(ControlFrame,text='Light').grid(row = 2, column = 0)
#   On Button for Light
lightOn = tkinter.Button(ControlFrame, text = "Light On ", command = onLight).grid(row = 2, column = 1)
#   Off Button for Light
lightOff = tkinter.Button(ControlFrame, text = "Light Off", command = offLight).grid(row = 2, column = 2)


#   Lable for Fan
FanLable = tkinter.Label(ControlFrame,text='Fan').grid(row = 3, column = 0)
#   On Button for Fan
FanOn = tkinter.Button(ControlFrame, text = "Fan On ", command = onFan).  grid(row = 3, column = 1)
#   Off Button for Fan
FanOff = tkinter.Button(ControlFrame, text = "Fan Off", command = offFan).grid(row = 3, column = 2)

#   Lable for Alarm
AlarmLable = tkinter.Label(ControlFrame,text='Alarm in Minutes').grid(row = 4, column = 0)
#   Entry for Alarm
AlarmEntry = tkinter.Entry(ControlFrame)
AlarmEntry.grid(row = 4, column = 1)

#   Button for verify the Alarm value
AlarmStart = tkinter.Button(ControlFrame, text = "Start", command = AlarmSet).grid(row = 4, column = 2)


#   Lable for Clock Configuration
ClockConfigLbl = tkinter.Label(ConfigFrame,text='Clock Configure').grid(row = 8, column = 0)
#   Set Seconds
#   Lable for Second configuration
SecConfigLbl = tkinter.Label(ConfigFrame,text='S').grid(row = 8, column = 1)
#   Entry for Second configuration
SecConfigEntry = tkinter.Entry(ConfigFrame)
SecConfigEntry.grid(row = 8, column = 2)

#   Set Mintue
#   Lable for Minute configuration
MinConfigLbl = tkinter.Label(ConfigFrame,text='M').grid(row = 9, column = 1)
#   Entry for Minute configuration
MinConfigEntry = tkinter.Entry(ConfigFrame)
MinConfigEntry.grid(row = 9, column = 2)


#   Set Hours
#   Lable for Hours configuration
HConfigLbl = tkinter.Label(ConfigFrame,text='H').grid(row = 10, column = 1)
#   Entry for Hours configuration
HConfigEntry = tkinter.Entry(ConfigFrame)
HConfigEntry.grid(row = 10, column = 2)


#   Set DayLight
#   Lable for Daylight configuration
DConfigLbl = tkinter.Label(ConfigFrame,text='DayLight').grid(row = 11, column = 1)
#   Combobox for Daylight configuration
DConfigCombo= ttk.Combobox(ConfigFrame)
DConfigCombo.grid(row = 11, column = 2)

#   Initialize combobox values
DConfigCombo['values'] = ("AM","PM")

#   Button to verify the change in time
UpadteTime = tkinter.Button(ConfigFrame, text = "Upadte Time", command = UpadteTimeDay).grid(row = 12, column = 1)

#   First call for Software Timer Hence Software timer is interval not repeated
clock()

#   Display the Mainframe and all its dependancies
mainFrame.mainloop()


