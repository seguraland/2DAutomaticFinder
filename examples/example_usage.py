# example_usage.py
from dscamlib.functions import *
from dscamlib.utils import save_image

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

                # Additional camera operations here...
                # Get and print all features of the camera
                features = GetAllFeatures(camera_handle)
                if isinstance(features, list):
                    print("Features: ", features)

                    # Get and print all feature descriptions
                    # feature_descs = GetAllFeaturesDesc(camera_handle, features)
                    # print(feature_descs)
                    # if isinstance(feature_descs, list):
                    #     print("Feature Descriptions: ", feature_descs)
                    # else:
                    #     print(feature_descs)  # Error message
                else:
                    print(features)  # Error message

                # Capture an image
                stImage, error_msg = CAM_GetImage(camera_handle, True)  # True for the latest image

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
    frame_size_command = CAM_CMD_GetFrameSize()
    result = CAM_Command(camera_handle, "CAM_CMD_GET_FRAMESIZE", frame_size_command)
    if result != LX_OK:
        return False, "Failed to get frame size"

    frame_size = frame_size_command.uiFrameSize
    # Additional preparations based on frame size and format.
    # ...

    return True, None
