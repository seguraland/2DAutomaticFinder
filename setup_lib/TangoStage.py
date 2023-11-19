# -*- coding: utf-8 -*-


import serial


#Command communication with response

def send_command_to_com_port(command, com_port, baud_rate=9600, timeout=1):
    try:
        # Initialize the serial connection
        ser = serial.Serial(com_port, baud_rate, timeout=timeout)

        # Ensure the port is open
        if ser.is_open:
            # Write the command to the COM port
            ser.write(command.encode())

            # Read the response from the COM port (optional)
            response = ser.readline().decode().strip()
            return response

        else:
            print(f"Error: COM Port {com_port} is not open.")

    except serial.SerialException as e:
        print(f"Error: {e}")

    finally:
        # Close the serial connection
        if ser and ser.is_open:
            ser.close()
            
#Command communication without response
            
def send_command_to_com_port2(command, com_port, baud_rate=9600, timeout=1):
    try:
        # Initialize the serial connection
        ser = serial.Serial(com_port, baud_rate, timeout=timeout)

        # Ensure the port is open
        if ser.is_open:
            # Write the command to the COM port
            ser.write(command.encode())
        else:
            print(f"Error: COM Port {com_port} is not open.")

    except serial.SerialException as e:
        print(f"Error: {e}")

    finally:
        # Close the serial connection
        if ser and ser.is_open:
            ser.close()
            
#Functions            
            

def MoveXYRelative (x,y):
    send_command_to_com_port2("mor {} {}\r\n".format(x,y),"COM7")
    
def GoTo(x,y):
    send_command_to_com_port2("go {} {}\r\n".format(x,y),"COM7")
    
#Units in mm    
def ReadPosition():
    return send_command_to_com_port("?pos\r\n","COM7")
#Change original position to 0,0
def SetZero():
    send_command_to_com_port("!pos 0 0\r\n","COM7")
    
#Reset to original position
def ClearPos():
    send_command_to_com_port("!posclr\r\n","COM7")
    
def XYPosition():
    response = ReadPosition()
    x = float(response.split(" ")[0])
    y = float(response.split(" ")[1])
    return x,y

def SavePosition():
    response = ReadPosition()
    x = response.split(" ")[0]
    y = response.split(" ")[1]
    return x,y





