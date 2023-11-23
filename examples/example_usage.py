# example_usage.py
import os
import ctypes
import threading

# Check if the script is running in PyCharm
if 'PYCHARM_HOSTED' in os.environ:
    # PyCharm specific imports
    from dscamlib.dscamlib.functions import *
    from dscamlib.dscamlib.definitions.other_definitions import CAM_CMD_GET_FRAMESIZE
    from dscamlib.dscamlib.definitions.constants import ECamTriggerMode
    from dscamlib.dscamlib.structures import CameraState
    from dscamlib.dscamlib.utils import save_image
else:
    # Imports for other environments
    from dscamlib.functions import *
    from dscamlib.definitions.other_definitions import CAM_CMD_GET_FRAMESIZE
    from dscamlib.definitions.constants import ECamTriggerMode
    from dscamlib.structures import CameraState
    from dscamlib.utils import save_image

# Default save path for an image
DEF_SAVE_PATH = "path/to/save/image.jpg"

# Default cam open
DEF_DEVICE_INDEX = 1

# Default debug prints Levels : 0:None , 1:Extreme, 2:Middle, 3:All
DEBUG_PRINT = 1


def run_example():
    print("Running example...")
    devices = CAM_OpenDevices()
    if isinstance(devices, list):
        if DEBUG_PRINT > 2:
            print(f"Successfully opened {len(devices)} devices.")
            for i, device in enumerate(devices):
                print(f"Device {i}: {device}")

        camera_handle = open_camera()
        if camera_handle:
            # Set event callback for image reception
            camera_state = CameraState()
            image_captured_event = threading.Event()
            notice_captured_event = threading.Event()

            # Pack the camera state and the event into CallbackData
            callback_data = CallbackData()
            callback_data.camera_state = camera_state
            callback_data.image_captured_event = image_captured_event
            callback_data.notice_captured_event = notice_captured_event

            # Pass the CallbackData object to the callback
            user_data = ctypes.pointer(callback_data)

            # Set up the callback
            wrapped_callback = CAM_SetEventCallback(camera_handle, event_callback, user_data)

            # Set up the notice callback
            wrapped_callback_app = CAM_SetNoticeCallback(camera_handle, notice_callback, user_data)

            print_features(camera_handle, DEBUG_PRINT)

            run_capture_sequence(camera_handle, camera_state, image_captured_event)

            # Wait for the image to be captured
            image_captured_event.wait()

            close_camera(camera_handle)

    else:
        print(devices)  # Print error message

    CAM_CloseDevices()


if __name__ == "__main__":
    run_example()


def open_camera():
    success, camera_handle, error_msg = CAM_Open(DEF_DEVICE_INDEX)
    if success:
        print(f"Opened camera with handle: {camera_handle}")
        return camera_handle
    else:
        print(f"Failed to open camera: {error_msg}")
        return None


def print_features(camera_handle, debug=0):
    features = GetAllFeatures(camera_handle)
    if isinstance(features, list):
        if debug > 2:
            print("Features: ", features)
            GetAllFeaturesDesc(camera_handle, features, debug)
        return features
    else:
        if debug > 1:
            print(features)  # Error message
        return None


def close_camera(camera_handle):
    close_msg = CAM_Close(camera_handle)
    print(close_msg)


