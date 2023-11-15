# example_usage.py
import os


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


def run_example():
    print("Running example...")
    devices = CAM_OpenDevices()
    if isinstance(devices, list):
        print(f"Successfully opened {len(devices)} devices.")
        for i, device in enumerate(devices):
            print(f"Device {i}: {device}")

        camera_handle = open_camera()
        if camera_handle:
            # Set event callback for image reception
            camera_state = CameraState()
            camera_state.capture_enabled = True  # Enable capturing initially

            # Set up the callback
            user_data = ctypes.pointer(camera_state)
            wrapped_callback = CAM_SetEventCallback(camera_handle, event_callback, user_data)

            features = print_features(camera_handle)
            if features:
                print_feature_descriptions(camera_handle, features)

            run_capture_sequence(camera_handle)

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


def print_features(camera_handle):
    features = GetAllFeatures(camera_handle)
    if isinstance(features, list):
        print("Features: ", features)
        return features
    else:
        print(features)  # Error message
        return None


def print_feature_descriptions(camera_handle, features):
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


def close_camera(camera_handle):
    close_msg = CAM_Close(camera_handle)
    print(close_msg)


