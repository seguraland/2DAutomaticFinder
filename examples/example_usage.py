# example_usage.py
import os

# Check if the script is running in PyCharm
if 'PYCHARM_HOSTED' in os.environ:
    # PyCharm specific imports
    from dscamlib.dscamlib.functions import *
    from dscamlib.dscamlib.definitions.other_definitions import CAM_CMD_GET_FRAMESIZE
    from dscamlib.dscamlib.structures import CAM_CMD_GetFrameSize
    from dscamlib.dscamlib.utils import save_image, event_callback
else:
    # Imports for other environments
    from dscamlib.functions import *
    from dscamlib.definitions.other_definitions import CAM_CMD_GET_FRAMESIZE
    from dscamlib.structures import CAM_CMD_GetFrameSize
    from dscamlib.utils import save_image, event_callback

# Default save path for an image
DEF_SAVE_PATH = "path/to/save/image.jpg"

# Default cam open
DEF_DEVICE_INDEX = 1


def run_example():
    print("Running example...")
    # Open devices and print their details
    devices = CAM_OpenDevices()
    if isinstance(devices, list):
        print(f"Successfully opened {len(devices)} devices.")
        for i, device in enumerate(devices):
            print(f"Device {i}: {device}")

        # For simplicity, let's open the first device if available
        if devices:
            success, camera_handle, error_msg = CAM_Open(DEF_DEVICE_INDEX)
            if success:
                print(f"Opened camera with handle: {camera_handle}")

                # Set event callback for image reception
                wrapped_callback = CAM_SetEventCallback(camera_handle, event_callback)

                # Additional camera operations here...
                # Get and print all features of the camera
                features = GetAllFeatures(camera_handle)
                if isinstance(features, list):
                    print("Features: ", features)

                    # Get and print all feature descriptions
                    feature_descs = GetAllFeaturesDesc(camera_handle, features)
                    if isinstance(feature_descs, list):
                        print("Feature Descriptions:")
                        for idx, desc in enumerate(feature_descs):
                            print(f"FDES {idx + 1}:")
                            for key, value in desc.items():
                                print(f"  {key}: {value}")
                            print()  # Add an empty line for better readability
                    else:
                        print(feature_descs)

                else:
                    print(features)  # Error message

                # Prepare for receiving an image and get the frame size
                success, frame_size_or_error = prepare_receive_image(camera_handle)
                if not success:
                    print(frame_size_or_error)  # Print error message
                    return

                frame_size = frame_size_or_error
                print(f"Using frame size: {frame_size} for image capture")

                # Capture an image with the obtained frame size
                stImage, error_msg = CAM_GetImage(camera_handle, True, frame_size)  # True for the latest image
                if error_msg:
                    print(error_msg)
                else:
                    # Save the image
                    save_image(stImage, DEF_SAVE_PATH)

                # Close the camera
                close_msg = CAM_Close(camera_handle)
                print(close_msg)
            else:
                print(f"Failed to open camera: {error_msg}")

    else:
        print(devices)  # Print error message

    # Close all devices
    close_msg = CAM_CloseDevices()
    print(close_msg)


if __name__ == "__main__":
    run_example()


def prepare_receive_image(camera_handle):
    print("Preparing to receive image...")

    # Create an instance of the structure to hold the frame size command result
    frame_size_command = CAM_CMD_GetFrameSize()

    # Send the command to get the frame size
    print(f"Sending command to get frame size for camera handle: {camera_handle}")
    result = CAM_Command(camera_handle, CAM_CMD_GET_FRAMESIZE, frame_size_command)

    # Check the result of the command
    if result != LX_OK:
        print(f"Failed to get frame size, error code: {result}")
        return False, "Failed to get frame size"

    # Print the obtained frame size
    frame_size = frame_size_command.uiFrameSize
    print(f"Obtained frame size: {frame_size}")

    return True, frame_size
