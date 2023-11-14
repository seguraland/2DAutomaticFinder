import ctypes
from pathlib import Path
from .structures import CAM_Device, Vector_CAM_FeatureValue, CAM_FeatureValue, CAM_FeatureDesc
from .definitions.error_codes import LX_OK
from .definitions.other_definitions import *

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
# #dscam.CAM_SetFeatures.argtypes = [lx_uint32, ctypes.POINTER(Vector_CAM_FeatureValue)]
# #dscam.CAM_SetFeatures.restype = lx_result

# Retrieves a feature's description
dscam.CAM_GetFeatureDesc.argtypes = [lx_uint32, lx_uint32, ctypes.POINTER(CAM_FeatureDesc)]
dscam.CAM_GetFeatureDesc.restype = lx_result

# Retrieves an image from the camera
# #dscam.CAM_GetImage.argtypes = [lx_uint32, ctypes.c_bool, ctypes.POINTER(CAM_Image), ctypes.POINTER(lx_uint32)]
# #dscam.CAM_GetImage.restype = lx_result

# Sends a command to the camera
# #dscam.CAM_Command.argtypes = [lx_uint32, ctypes.POINTER(ctypes.c_wchar), ctypes.c_void_p]
# #dscam.CAM_Command.restype = lx_result

# Polls for an event from the camera
# #dscam.CAM_EventPolling.argtypes = [lx_uint32, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(CAM_Event)]
# #dscam.CAM_EventPolling.restype = lx_result

# Sets a callback function for camera events
# #FCAM_EventCallback = ctypes.CFUNCTYPE(None, lx_uint32, ctypes.POINTER(CAM_Event), ctypes.c_void_p)
# #dscam.CAM_SetEventCallback.argtypes = [lx_uint32, FCAM_EventCallback, ctypes.c_void_p]
# #dscam.CAM_SetEventCallback.restype = lx_result

# Sets a callback function for notifications
# #FCAM_NoticeCallback = ctypes.CFUNCTYPE(None, lx_uint32, ctypes.POINTER(CAM_Notice), ctypes.c_void_p)
# #dscam.CAM_SetNoticeCallback.argtypes = [lx_uint32, FCAM_NoticeCallback, ctypes.c_void_p]
# #dscam.CAM_SetNoticeCallback.restype = lx_result


# # Define CAM_OpenDevices Function
def CAM_OpenDevices():
    uiDeviceCount = ctypes.c_uint32()
    ppstCamDevice = ctypes.POINTER(CAM_Device)()

    result = dscam.CAM_OpenDevices(ctypes.byref(uiDeviceCount), ctypes.byref(ppstCamDevice))
    if result == LX_OK:
        devices = []
        for i in range(uiDeviceCount.value):
            device = ppstCamDevice[i]
            devices.append({
                'Type': device.eCamDeviceType,
                'Serial Number': device.uiSerialNo,
                'Camera Name': device.wszCameraName
            })
        return devices
    else:
        return "Failed to open devices."


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
        print(feature_desc)
        result = dscam.CAM_GetFeatureDesc(camera_handle, uiFeatureId, ctypes.byref(feature_desc))
        print(result)
        if result != LX_OK:
            return f"Failed to get description for feature {uiFeatureId}, error code: {result}"

        # Process the feature description as needed
        # For example, convert the description to a more readable format
        # ##### readable_desc = process_feature_desc(feature_desc)  # Implement this function as needed
        # ##### readable_desc = process_feature_desc(feature_desc)  # Then pass readable_desc instead of feature_desc

        feature_descs.append(feature_desc)

    return feature_descs
