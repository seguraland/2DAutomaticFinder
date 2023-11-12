import ctypes
from .definitions.other_definitions import *


# CAM_Device Structure: Camera information
class CAM_Device(ctypes.Structure):
    _fields_ = [
        ("eCamDeviceType", ctypes.c_uint),
        ("uiSerialNo", ctypes.c_uint32),
        ("wszFwVersion", ctypes.c_wchar * CAM_VERSION_MAX),
        ("wszFpgaVersion", ctypes.c_wchar * CAM_VERSION_MAX),
        ("wszUsbDcVersion", ctypes.c_wchar * CAM_VERSION_MAX),
        ("wszUsbVersion", ctypes.c_wchar * CAM_VERSION_MAX),
        ("wszDriverVersion", ctypes.c_wchar * CAM_VERSION_MAX),
        ("wszCameraName", ctypes.c_wchar * CAM_NAME_MAX),
    ]

# CAM_FeatureNameRef Structure
# CAM_Area Structure
# CAM_Position Structure
# CAM_Size Structure
# CAM_TriggerOption Structure
# CAM_MultiExposureTime Structure
# CAM_Format Structure
# CAM_Variant Structure
# CAM_FeatureValue Structure
# Vector_CAM_FeatureValue Structure
# CAM_FeatureDescElement Structure
# CAM_FeatureDescRange Structure
# CAM_FeatureDescArea Structure
# CAM_FeatureDescPosition Structure
# CAM_FeatureDescSize Structure
# CAM_FeatureDescTriggerOption Structure
# CAM_FeatureDescFormat Structure
# CAM_FeatureDesc Structure
# CAM_Image Structure
# CAM_ImageInfo Structure
# CAM_ImageInfoEx Structure
# CAM_CMD_GetFrameSize Structure
# CAM_CMD_StartFrameTransfer Structure
# CAM_CMD_IsTransferStarted Structure
# CAM_CMD_FrameDropless Structure
# CAM_CMD_Grouping Structure
# CAM_CMD_GetSdkVersion Structure
# CAM_CMD_ControlCis Structure
# CAM_CMD_CheckFwVersion Structure
# CAM_CMD_FovSize Structure
# CAM_CMD_FovRoi Structure
# CAM_EventImageReceived Structure
# CAM_EventFeatureChanged Structure
# CAM_EventSignal Structure
# CAM_EventTransError Structure
# CAM_EventBusReset Structure
# CAM_Event Structure
# CAM_NoticeTransError Structure
# CAM_NoticeGroup Structure
# CAM_NoticeInfo Structure
# CAM_Notice Structure
