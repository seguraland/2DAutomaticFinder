# -*- coding: utf-8 -*-
#Import Nikon Library
from NikonLV import NikonLv
import TangoStage as TS


#Create NIkon object
Nikon = NikonLv()

#Move relative position in micrometers
def MoveZRelative(z):
    #Check first if device is available
    if Nikon.ZDrive.IsMounted() == 1 :
    #20 factor transforms unit into micrometers
        Nikon.ZDrive.MoveRelative(z*20)
        
#Move Absolute position in micrometers     
def MoveZAbsolute(z):
    #Check first if device is available
    if Nikon.ZDrive.IsMounted() == 1 :
    #20 factor transforms unit into micrometers
        Nikon.ZDrive.MoveAbsolute(z*20)
        
#Read position in micrometers        
def ZPosition():
    if Nikon.ZDrive.IsMounted() == 1 :
        return Nikon.ZDrive.Position()
    
#Abort movement    
def ZAbort():
    if Nikon.ZDrive.IsMounted() == 1 :
        Nikon.ZDrive.Abort()
        
#Read Speed 1-7 Speeds        
def ZReadSpeed():
    if Nikon.ZDrive.IsMounted() == 1 :
        return Nikon.ZDrive.Speed()
    
# There are 8 Speeds from 0 to 7

# -Speed0  2.50 mm/sec

# -Speed1  1.25 mm/sec

# -Speed2  0.625 mm/sec

# -Speed3  0.3125 mm/sec

# -Speed4  0.125 mm/sec

# -Speed5  0.0625 mm/sec

# -Speed6  0.0375 mm/sec

# -Speed7  0.01 mm/sec

def ZSpeed(speed):
    if Nikon.ZDrive.IsMounted() == 1 :
        Nikon.Zdrive.Speed = speed
        
def XYZPosition():
    x = TS.XYPosition()[0]
    y = TS.XYPosition()[1]
    z = ZPosition()
    return x,y,z
        



