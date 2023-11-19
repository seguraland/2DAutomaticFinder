import cv2
import numpy as np
from mss import mss

import TangoStage as TS
import NikonFocus as NF
import keyboard

def SampleLimits():
    pos = []
    print("Place microscope on sample´s top left edge")
    print("Press any key to save position")
    keyboard.read_event()
    #optional set first edge at x=0, y=0
    #TS.SetZero()
    print("Position: ",TS.ReadPosition())
    pos.append(TS.XYPosition())
    print("Place microscope on sample´s top right edge")
    print("Press any key to save position")
    keyboard.read_event()
    print("Position: ",TS.ReadPosition())
    pos.append(TS.XYPosition())
    print("Place microscope on sample´s bottom right edge")
    print("Press any key to save position")
    keyboard.read_event()
    print("Position: ",TS.ReadPosition())
    pos.append(TS.XYPosition())
    
    deltaX = abs(float(pos[1][0])-float(pos[0][0]))
    deltaY = abs(float(pos[2][1])-float(pos[0][1]))
    TS.GoTo(pos[0][0],pos[0][1])
    
    return deltaX,deltaY,pos  

def Bulk_detection():
    bulk = False
    bounding_box = bounding_box = {'top': 110, 'left': 2030, 'width': 1230, 'height': 890}
    sct = mss()

    sct_img = sct.grab(bounding_box)
    frame= np.array(sct_img)
    img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply GaussianBlur to reduce noise and improve contour detection
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

        # Use Canny edge detection to find edges
    edges = cv2.Canny(blurred_image, 50, 150)

        # Find contours in the edged image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Check if any contours are found (indicating the presence of a bulk)
    if len(contours) > 0:
        bulk = True
        
    return bulk

def capture(path):
    global img_counter
    bounding_box = {'top': 110, 'left': 2030, 'width': 1230, 'height': 890}
    sct = mss()
    sct_img = sct.grab(bounding_box)
    cv2.imwrite(f"{path}/{img_counter}.jpg", np.array(sct_img))
    img_counter+=1
    
    
# def Bulk_finder(min_range,max_range,focus_step=10):
#     focuspoint=min_range
#     for i in range(min_range,max_range,focus_step):
#         NF.MoveZAbsolute(i)
#         time.sleep(1/500)
#         if(NF.Bulk_detection()):
#         focuspoint=i
#             break
#     else:
#         focuspoint=max_range
        
#     return focuspoint

def Focus_composition(path,zmin=1820,zmax=1840,zstep=0.2,Bulk=True):
    for i in range(zmin,zmax,zstep):
        NF.MoveZAbsolute(i)
        if (Bulk):
            if(Bulk_detection()): capture(path)
        else: capture(path)
        #time.sleep(1/100)


def ScanRange(deltax,deltay,path,objective='x100',zmin=1820,zmax=1860,zstep=0.15,Bulk=True):
    objectives = {
        'x100': [0.24, 0.18],
        'x50': [0.48, 0.36],
        'x20': [0,0]
        }       
    
    xrange = objectives[objective][0]
    yrange = objectives[objective][1]
    
    xsteps = round(deltax/xrange) + 1
    ysteps = round(deltay/yrange) + 1
    
    positions = []
    cont = 0
    positions.append(TS.SavePosition())
    Focus_composition(path,zmin,zmax,zstep,Bulk=True)
    
    for j in range(ysteps):
        #X Steps Scanning
        for i in range(xsteps):
            #Move stage to the right then cont is even and to the left when con is odd.
            TS.MoveXYRelative(pow(-1,cont)*xrange,0)
            positions.append(TS.SavePosition())
            #Starts trying different focus points and capturing
            Focus_composition(path,zmin,zmax,zstep,Bulk=True)
        #When an edge is reached in the x direction
        #Jumps of Yrange unit in the y direction
        TS.MoveXYRelative(0,-yrange)
        positions.append(TS.SavePosition())
        #Starts capturing different Focus points
        Focus_composition(path,zmin,zmax,zstep,Bulk=True)
        #time.sleep(1/100)
        #print("Position index: ",position_index)
        #Save current position
        #positions.append(SavePosition())
        cont+=1
    return positions,xsteps,ysteps





    
    
    
