import ctypes
from ctypes import cast, POINTER, byref
from pathlib import Path
from .structures import (
    CAM_CMD_GetFrameSize, CAM_CMD_StartFrameTransfer, CameraState,
    CAM_Device, Vector_CAM_FeatureValue, CAM_FeatureValue, CAM_FeatureDesc, CAM_Image, CAM_Event)
from .definitions.error_codes import LX_OK
from .definitions.other_definitions import *
from .definitions.constants import (
    ECamFeatureId, ECamVariantRunType, ECamTriggerMode, ECamEventType)
from .utils import get_error_message, process_feature_desc

# Determine the absolute path to the 'DSCam.dll' file
dll_path = Path(__file__).resolve().parent.parent / 'binary' / 'DSCam.dll'

# Load the DLL using its absolute path
dscam = ctypes.CDLL(str(dll_path))

# Define lx_result as __int32
lx_result = ctypes.c_int32
lx_uint32 = ctypes.c_uint32

# Opens a list of connected devices, including simulators
dscam.CAM_OpenDevices.argtypes = [ctypes.POINTER(lx_uint32), ctypes.POINTER(ctypes.POINTER(CAM_Device))]
dscam.CAM_OpenDevices.restype = lx_result

# Closes the devices opened by CAM_OpenDevices
dscam.CAM_CloseDevices.argtypes = []
dscam.CAM_CloseDevices.restype = lx_result

# Opens a camera device
dscam.CAM_Open.argtypes = [lx_uint32, ctypes.POINTER(lx_uint32), lx_uint32, ctypes.POINTER(ctypes.c_wchar)]
dscam.CAM_Open.restype = lx_result

# Closes a camera device
dscam.CAM_Close.argtypes = [lx_uint32]
dscam.CAM_Close.restype = lx_result

# Retrieves all feature values from the camera
dscam.CAM_GetAllFeatures.argtypes = [lx_uint32, ctypes.POINTER(Vector_CAM_FeatureValue)]
dscam.CAM_GetAllFeatures.restype = lx_result

# Retrieves specified feature values from the camera
# #dscam.CAM_GetFeatures.argtypes = [lx_uint32, ctypes.POINTER(Vector_CAM_FeatureValue)]
# #dscam.CAM_GetFeatures.restype = lx_result

# Sets specified feature values on the camera
dscam.CAM_SetFeatures.argtypes = [lx_uint32, ctypes.POINTER(Vector_CAM_FeatureValue)]
dscam.CAM_SetFeatures.restype = lx_result

# Retrieves a feature's description
dscam.CAM_GetFeatureDesc.argtypes = [lx_uint32, lx_uint32, ctypes.POINTER(CAM_FeatureDesc)]
dscam.CAM_GetFeatureDesc.restype = lx_result

# Retrieves an image from the camera
dscam.CAM_GetImage.argtypes = [lx_uint32, ctypes.c_bool, ctypes.POINTER(CAM_Image), ctypes.POINTER(lx_uint32)]
dscam.CAM_GetImage.restype = lx_result

# Sends a command to the camera
dscam.CAM_Command.argtypes = [lx_uint32, ctypes.POINTER(ctypes.c_wchar), ctypes.c_void_p]
dscam.CAM_Command.restype = lx_result

# Polls for an event from the camera
dscam.CAM_EventPolling.argtypes = [lx_uint32, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(CAM_Event)]
dscam.CAM_EventPolling.restype = lx_result

# Sets a callback function for camera events
FCAM_EventCallback = ctypes.CFUNCTYPE(None, lx_uint32, ctypes.POINTER(CAM_Event), ctypes.c_void_p)
dscam.CAM_SetEventCallback.argtypes = [lx_uint32, FCAM_EventCallback, ctypes.c_void_p]
dscam.CAM_SetEventCallback.restype = lx_result


# Sets a callback function for notifications
# #FCAM_NoticeCallback = ctypes.CFUNCTYPE(None, lx_uint32, ctypes.POINTER(CAM_Notice), ctypes.c_void_p)
# #dscam.CAM_SetNoticeCallback.argtypes = [lx_uint32, FCAM_NoticeCallback, ctypes.c_void_p]
# #dscam.CAM_SetNoticeCallback.restype = lx_result


# # Define CAM_OpenDevices Function
def CAM_OpenDevices():
    """
    Opens all available camera devices and retrieves their information.

    :return: A list of dictionaries containing device information if successful,
             or an error message string if unsuccessful.
    """

    # Initialize a variable to hold the count of devices
    uiDeviceCount = ctypes.c_uint32()

    # Initialize a pointer to hold the array of devices
    ppstCamDevice = ctypes.POINTER(CAM_Device)()

    # Call the CAM_OpenDevices function from the DLL
    result = dscam.CAM_OpenDevices(ctypes.byref(uiDeviceCount), ctypes.byref(ppstCamDevice))

    # Check if the call was successful
    if result == LX_OK:
        devices = []
        # Iterate over the array of devices and extract their information
        for i in range(uiDeviceCount.value):
            device = ppstCamDevice[i]
            devices.append({
                'Type': device.eCamDeviceType,  # Device type
                'Serial Number': device.uiSerialNo,  # Serial number
                'Camera Name': device.wszCameraName  # Camera name
            })
        return devices
    else:
        # Return an error message if the call was unsuccessful
        return "Failed to open devices."


def CAM_CloseDevices():
    """
    Closes all devices that were opened.

    :return: A string indicating success or an error message.
    """
    result = dscam.CAM_CloseDevices()
    if result != LX_OK:
        return "Failed to close devices, error code: {}".format(result)

    return "Devices closed successfully"


def CAM_Open(device_index):
    """
    Opens a camera device.

    :param device_index: Index of the device to open.
    :return: Tuple of (result, camera_handle, error_message).
             result is True if successful, False otherwise.
    """
    uiCameraHandle = ctypes.c_uint32()
    szError = (ctypes.c_wchar * CAM_ERRMSG_MAX)()  # Error message buffer

    # Open the camera
    lResult = dscam.CAM_Open(device_index, ctypes.byref(uiCameraHandle), CAM_ERRMSG_MAX, szError)
    if lResult != LX_OK:
        return False, None, szError.value

    # Set event callback (adjust as necessary)
    # lResult = dscam.CAM_SetEventCallback(uiCameraHandle.value, event_callback_function, event_trans_data)
    # if lResult != LX_OK:
    #     return False, uiCameraHandle.value, "Failed to set event callback."

    return True, uiCameraHandle.value, None


def CAM_Close(camera_handle):
    """
    Closes the camera device.

    :param camera_handle: The handle to the camera device.
    :return: A string indicating success or error message.
    """
    # Implement any necessary cleanup before closing the camera
    # e.g., StopGetImageThread(), ClearImage(), etc.
    # These depend on your specific application implementation

    # Call CAM_Close from your ctypes DLL
    result = dscam.CAM_Close(camera_handle)
    if result != LX_OK:
        return f"Failed to close camera, error code: {result}"

    # Perform any additional cleanup if necessary
    # e.g., Free_Vector_CAM_FeatureValue(), Free_CAM_FeatureDesc(), etc.

    return "Camera closed successfully"


def GetAllFeatures(camera_handle):
    """
    Retrieves all feature values from the camera.

    :param camera_handle: The handle to the camera device.
    :return: A list of feature values, or an error message if unsuccessful.
    """
    # Allocate an array of CAM_FeatureValue
    feature_array = (CAM_FeatureValue * CAM_FEA_CAPACITY)()

    # Prepare the Vector_CAM_FeatureValue
    vectFeatureValue = Vector_CAM_FeatureValue()
    vectFeatureValue.uiCapacity = CAM_FEA_CAPACITY
    vectFeatureValue.uiCountUsed = 0
    vectFeatureValue.pstFeatureValue = ctypes.cast(feature_array, ctypes.POINTER(CAM_FeatureValue))

    # Call CAM_GetAllFeatures
    result = dscam.CAM_GetAllFeatures(camera_handle, ctypes.byref(vectFeatureValue))
    if result != LX_OK:
        return "Failed to get all features, error code: {}".format(result)

    # Process the features
    features = []
    for i in range(vectFeatureValue.uiCountUsed):
        feature = vectFeatureValue.pstFeatureValue[i]
        feature_dict = {
            'Feature ID': feature.uiFeatureId,
            # Add other relevant fields here
        }
        features.append(feature_dict)

    return features


def CAM_SetFeatures(camera_handle, vect_feature_value):
    """
        Sets selected set of features.

        :param camera_handle: The handle to the camera device.
        :param vect_feature_value: Vector_CAM_FeatureValue object to input.
        :return: None if successful, raises RuntimeError otherwise.
        """
    result = dscam.CAM_SetFeatures(camera_handle, byref(vect_feature_value))
    if result != LX_OK:
        print("  >CAM_SetFeatures : ERROR")
        # Break the code since we are input values
        raise RuntimeError(f"Failed to set features, error code: {result}")

    print("     >CAM_SetFeatures : DONE")


def GetAllFeaturesDesc(camera_handle, features):
    """
    Retrieves descriptions for all features.

    :param camera_handle: The handle to the camera device.
    :param features: A list of features obtained from GetAllFeatures.
    :return: A list of feature descriptions or an error message.
    """
    feature_descs = []

    for feature in features:
        uiFeatureId = feature['Feature ID']

        # Assuming CAM_FeatureDesc is a ctypes structure you have defined
        feature_desc = CAM_FeatureDesc()
        result = dscam.CAM_GetFeatureDesc(camera_handle, uiFeatureId, ctypes.byref(feature_desc))
        if result != LX_OK:
            return f"Failed to get description for feature {uiFeatureId}, error code: {result}"

        # Process the feature description
        readable_desc = process_feature_desc(feature_desc)

        feature_descs.append(readable_desc)

    return feature_descs


def CAM_GetImage(camera_handle, bNewRequired, frame_size):
    """
    Captures an image from the camera.

    :param camera_handle: The handle to the camera.
    :param bNewRequired: Boolean to indicate whether to capture the latest image.
    :param frame_size: The expected size of the image frame.
    :return: A tuple (CAM_Image object, None) if successful, or (None, error message) if failed.
    """
    stImage = CAM_Image()
    stImage.uiDataBufferSize = frame_size  # Set the size of the frame

    # Allocate memory for the image data
    buffer = ctypes.create_string_buffer(frame_size)

    # Instead of casting, directly assign the memory address of the buffer to pDataBuffer
    stImage.pDataBuffer = ctypes.cast(ctypes.addressof(buffer), ctypes.c_void_p)

    uiRemained = ctypes.c_uint32()
    result = dscam.CAM_GetImage(camera_handle, bNewRequired, ctypes.byref(stImage), ctypes.byref(uiRemained))

    if result != LX_OK:
        error_msg = get_error_message(result)
        return None, f"Failed to get image, error: {error_msg}"

    return stImage, None


def CAM_Command(camera_handle, command, data):
    # 'command' is a string representing the command name
    # and 'data' is an instance of the appropriate command structure.
    # The implementation of this function will depend on how CAM_Command is defined in the SDK.

    # Check if data is None or an actual ctypes instance
    if data is not None:
        data_ref = ctypes.byref(data)
    else:
        data_ref = None

    result = dscam.CAM_Command(camera_handle, command, data_ref)

    return result


# Wrapper for CAM_EventPolling
def CAM_EventPolling(camera_handle, event_type):
    event = CAM_Event()
    result = dscam.CAM_EventPolling(camera_handle, ctypes.c_void_p(), event_type, ctypes.byref(event))
    if result != LX_OK:
        raise RuntimeError(f"Failed to poll event, error code: {result}")
    return event


# Wrapper for CAM_SetEventCallback
def CAM_SetEventCallback(camera_handle, callback_func, user_data):
    wrapped_callback = FCAM_EventCallback(callback_func)
    result = dscam.CAM_SetEventCallback(camera_handle, wrapped_callback, user_data)
    if result != LX_OK:
        raise RuntimeError(f"Failed to set event callback, error code: {result}")
    return wrapped_callback  # Keep a reference to prevent garbage collection


def set_trigger_mode(camera_handle, mode):
    print(" Trigger mode set...")
    # Prepare the feature value for setting the trigger mode
    feature_array = (CAM_FeatureValue * 1)()  # Array of one CAM_FeatureValue
    feature_array[0].uiFeatureId = ECamFeatureId.eTriggerMode.value  # Assuming this is the correct feature ID
    feature_array[0].stVariant.eVarType = ECamVariantRunType.evrt_uint32.value
    feature_array[0].stVariant.ui32Value = mode.value

    # Prepare the Vector_CAM_FeatureValue
    vect_feature_value = Vector_CAM_FeatureValue()
    vect_feature_value.uiCountUsed = 1
    vect_feature_value.uiCapacity = 1
    vect_feature_value.uiPauseTransfer = 0
    vect_feature_value.pstFeatureValue = cast(feature_array, POINTER(CAM_FeatureValue))

    # Set the features
    CAM_SetFeatures(camera_handle, vect_feature_value)
    print(" Trigger mode set successfully.")


def get_image_frame_size(camera_handle):
    print("Preparing to receive frame size...")

    # Create an instance of the structure to hold the frame size command result
    frame_size_command = CAM_CMD_GetFrameSize()

    # Send the command to get the frame size
    result = CAM_Command(camera_handle, CAM_CMD_GET_FRAMESIZE, frame_size_command)

    # Check the result of the command
    if result != LX_OK:
        raise RuntimeError(f"Failed to get frame size, error code: {result}")

    # Print the obtained frame size
    uiFrameSize = frame_size_command.uiFrameSize
    uiFrameInterval = frame_size_command.uiFrameInterval
    uiRShutterDelay = frame_size_command.uiRShutterDelay

    print(f"     >Obtained uiFrameSize: {uiFrameSize}")
    print(f"     >Obtained uiFrameInterval: {uiFrameInterval}")
    print(f"     >Obtained uiRShutterDelay: {uiRShutterDelay}")

    return uiFrameSize


def run_capture_sequence(camera_handle):
    print("Run image capture sequence...")
    set_trigger_mode(camera_handle, ECamTriggerMode.ectmSoft)
    start_image_transfer(camera_handle)
    capture_image(camera_handle)
    # Only in Mode : ectmOff
    # one_push_soft_trigger(camera_handle)
    # The image reception will be handled in the event_callback

    end_image_transfer(camera_handle)
    print("Run image capture sequence DONE")


def start_image_transfer(camera_handle):
    # Start image transfer using CAM_Command with CAM_CMD_START_FRAMETRANSFER
    print(" Starting image transfer...")

    # Create an instance of CAM_CMD_StartFrameTransfer
    start_frame_transfer_cmd = CAM_CMD_StartFrameTransfer()
    start_frame_transfer_cmd.uiImageBufferNum = DEF_DRIVER_BUFFER_NUM

    # Start image transfer using CAM_Command
    result = CAM_Command(camera_handle, CAM_CMD_START_FRAMETRANSFER, start_frame_transfer_cmd)
    if result != LX_OK:
        raise RuntimeError(f"Failed to start image transfer, error code: {result}")

    print(" Image transfer started successfully.")


def end_image_transfer(camera_handle):
    # End image transfer using CAM_Command with CAM_CMD_STOP_FRAMETRANSFER
    print(" Stopping image transfer...")

    # Stop image transfer using CAM_Command
    result = CAM_Command(camera_handle, CAM_CMD_STOP_FRAMETRANSFER, None)
    if result != LX_OK:
        raise RuntimeError(f"Failed to stop image transfer, error code: {result}")

    print(" Image transfer stopped successfully.")


def one_push_soft_trigger(camera_handle):
    # Start image transfer using CAM_Command with CAM_CMD_ONEPUSH_SOFTTRIGGER
    print(" One push soft trigger...")

    # Start image transfer using CAM_Command
    result = CAM_Command(camera_handle, CAM_CMD_ONEPUSH_SOFTTRIGGER, None)
    if result != LX_OK:
        raise RuntimeError(f"Failed to one_push_soft_trigger, error code: {result}")

    print(" One push soft triggered successfully.")


def one_push_soft_trigger_cancel(camera_handle):
    # Start image transfer using CAM_Command with CAM_CMD_ONEPUSH_TRIGGERCANCEL
    print(" One push soft trigger...")

    # Start image transfer using CAM_Command
    result = CAM_Command(camera_handle, CAM_CMD_ONEPUSH_TRIGGERCANCEL, None)
    if result != LX_OK:
        raise RuntimeError(f"Failed to one_push_soft_trigger_cancel, error code: {result}")

    print(" One push soft trigger canceled successfully.")


def capture_image(camera_handle):
    print("Capturing image...")

    frame_size = get_image_frame_size(camera_handle)

    # Attempt to capture the image
    stImage, error_msg = CAM_GetImage(camera_handle, True, frame_size)
    if error_msg:
        print(f"Failed to capture image: {error_msg}")
    else:
        # Process or save the captured image
        print("sdf image: {dfdf}")
        # save_image(stImage, 'path/to/save/image')

    # Optionally, stop image transfer if it's a one-time capture
    # one_push_soft_trigger_cancel(camera_handle)
    # end_image_transfer(camera_handle)


def event_callback(camera_handle, event_ptr, user_data):
    # Access the event structure
    event = event_ptr.contents
    state = ctypes.cast(user_data, ctypes.POINTER(CameraState)).contents

    if state.capture_enabled:
        # Check the event type and respond accordingly
        if event.eEventType == ECamEventType.ecetImageReceived.value:
            print("Image received event detected")
            state.capture_enabled = False
            capture_image(camera_handle)

        elif event.eEventType == ECamEventType.ecetFeatureChanged.value:
            print("Feature changed event detected")

        elif event.eEventType == ECamEventType.ecetExposureEnd.value:
            print("Exposure end event detected")
            # capture_image(camera_handle)

        # Add additional elif blocks for other event types as needed

        else:
            print(f"Unknown event type: {event.eEventType}")
