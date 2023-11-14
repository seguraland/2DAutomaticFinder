import ctypes
from .definitions.constants import *
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


# <For Feature> ########################################
# CAM_FeatureNameRef Structure
class CAM_FeatureNameRef(ctypes.Structure):
    _fields_ = [
        ("eId", ctypes.c_uint32),
        ("wszName", ctypes.c_wchar * CAM_FEA_COMMENT_MAX),
    ]


# CAM_Area Structure
class CAM_Area(ctypes.Structure):
    _fields_ = [
        ("uiLeft", ctypes.c_uint32),
        ("uiTop", ctypes.c_uint32),
        ("uiWidth", ctypes.c_uint32),  # 4x step
        ("uiHeight", ctypes.c_uint32),
    ]

    def __eq__(self, other):
        if not isinstance(other, CAM_Area):
            return False
        return (self.uiLeft == other.uiLeft and
                self.uiTop == other.uiTop and
                self.uiWidth == other.uiWidth and
                self.uiHeight == other.uiHeight)

    def __ne__(self, other):
        return not self.__eq__(other)


# CAM_Position Structure
class CAM_Position(ctypes.Structure):
    _fields_ = [
        ("uiX", ctypes.c_uint32),
        ("uiY", ctypes.c_uint32),
    ]

    def __eq__(self, other):
        return isinstance(other, CAM_Position) and self.uiX == other.uiX and self.uiY == other.uiY

    def __ne__(self, other):
        return not self.__eq__(other)


# CAM_Size Structure
class CAM_Size(ctypes.Structure):
    _fields_ = [
        ("uiWidth", ctypes.c_uint32),
        ("uiHeight", ctypes.c_uint32),
    ]

    def __eq__(self, other):
        return isinstance(other, CAM_Size) and self.uiWidth == other.uiWidth and self.uiHeight == other.uiHeight

    def __ne__(self, other):
        return not self.__eq__(other)


# CAM_TriggerOption Structure
class CAM_TriggerOption(ctypes.Structure):
    _fields_ = [
        ("uiFrameCount", ctypes.c_uint32),
        ("iDelayTime", ctypes.c_int32),  # usec
    ]

    def __eq__(self, other):
        if not isinstance(other, CAM_TriggerOption):
            return False
        return (self.uiFrameCount == other.uiFrameCount and
                self.iDelayTime == other.iDelayTime)

    def __ne__(self, other):
        return not self.__eq__(other)


# CAM_MultiExposureTime Structure
class CAM_MultiExposureTime(ctypes.Structure):
    _fields_ = [
        ("uiNum", ctypes.c_uint32),
        ("uiExposureTime", ctypes.c_uint32 * CAM_FEA_MULTIEXPOSURETIME_MAX),
    ]

    def __eq__(self, other):
        if not isinstance(other, CAM_MultiExposureTime) or self.uiNum != other.uiNum:
            return False
        return all(self.uiExposureTime[i] == other.uiExposureTime[i] for i in range(self.uiNum))

    def __ne__(self, other):
        return not self.__eq__(other)


# CAM_Format Structure
class CAM_Format(ctypes.Structure):
    _fields_ = [
        ("eColor", ctypes.c_uint),
        ("eMode", ctypes.c_uint),
    ]

    def __eq__(self, other):
        return isinstance(other, CAM_Format) and self.eColor == other.eColor and self.eMode == other.eMode

    def __ne__(self, other):
        return not self.__eq__(other)


# CAM_Variant Structure
class CAM_Variant_Union(ctypes.Union):
    _fields_ = [
        ("i32Value", ctypes.c_int32),
        ("ui32Value", ctypes.c_uint32),
        ("i64Value", ctypes.c_int64),
        ("ui64Value", ctypes.c_uint64),
        ("dValue", ctypes.c_double),
        ("bValue", ctypes.c_bool),
        ("pValue", ctypes.c_void_p),
        ("wszValue", ctypes.c_wchar * CAM_FEA_VARIANT_MAX),
        ("stArea", CAM_Area),
        ("stPosition", CAM_Position),
        ("stSize", CAM_Size),
        ("stTriggerOption", CAM_TriggerOption),
        ("stMultiExposureTime", CAM_MultiExposureTime),
        ("stFormat", CAM_Format),
    ]


class CAM_Variant(ctypes.Structure):
    _fields_ = [
        ("eVarType", ctypes.c_int),        # Using ctypes.c_int for the enum field
        ("Data", CAM_Variant_Union),
    ]


# CAM_FeatureValue Structure
class CAM_FeatureValue(ctypes.Structure):
    _fields_ = [
        ("uiFeatureId", ctypes.c_uint32),
        ("stVariant", CAM_Variant),
        ("ucTransSize", ctypes.c_ubyte),  # Application doesn't use
    ]

    def __init__(self):
        super(CAM_FeatureValue, self).__init__()
        self.uiFeatureId = 0


# Vector_CAM_FeatureValue Structure
class Vector_CAM_FeatureValue(ctypes.Structure):
    _fields_ = [
        ("uiCountUsed", ctypes.c_uint32),
        ("uiCapacity", ctypes.c_uint32),
        ("uiPauseTransfer", ctypes.c_uint32),
        ("pstFeatureValue", ctypes.POINTER(CAM_FeatureValue))
    ]

    def __init__(self):
        super(Vector_CAM_FeatureValue, self).__init__()
        self.uiCountUsed = 0
        self.uiCapacity = CAM_FEA_CAPACITY
        self.uiPauseTransfer = 0
        # Allocate memory for pstFeatureValue
        self.pstFeatureValue = (CAM_FeatureValue * CAM_FEA_CAPACITY)()


# <For Feature Attribute> ##############################
class FeatureDescElement(ctypes.Structure):
    _fields_ = [
        ("stMin", ctypes.c_int),
        ("stMax", ctypes.c_int),
        ("stRes", ctypes.c_int),
        ("stDef", ctypes.c_int)
    ]

    def __eq__(self, other):
        return (
                self.stMin == other.stMin and
                self.stMax == other.stMax and
                self.stRes == other.stRes and
                self.stDef == other.stDef
        )

    def __ne__(self, other):
        return (
                self.stMin != other.stMin or
                self.stMax != other.stMax or
                self.stRes != other.stRes or
                self.stDef != other.stDef
        )


# CAM_FeatureDescElement Structure
class CAM_FeatureDescElement(ctypes.Structure):
    _fields_ = [
        ("varValue", CAM_Variant),
        ("wszComment", ctypes.c_wchar * CAM_FEA_COMMENT_MAX)
    ]

    def __eq__(self, other):
        return self.varValue == other.varValue and self.wszComment == other.wszComment

    def __ne__(self, other):
        return self.varValue != other.varValue or self.wszComment != other.wszComment


# CAM_FeatureDescRange Structure
class CAM_FeatureDescRange(FeatureDescElement):
    _fields_ = [
        ("stMin", CAM_Variant),
        ("stMax", CAM_Variant),
        ("stRes", CAM_Variant),
        ("stDef", CAM_Variant)
    ]


# CAM_FeatureDescArea Structure
class CAM_FeatureDescArea(FeatureDescElement):
    _fields_ = [
        ("stMin", CAM_Area),
        ("stMax", CAM_Area),
        ("stRes", CAM_Area),
        ("stDef", CAM_Area)
    ]


# CAM_FeatureDescPosition Structure
class CAM_FeatureDescPosition(FeatureDescElement):
    _fields_ = [
        ("stMin", CAM_Position),
        ("stMax", CAM_Position),
        ("stRes", CAM_Position),
        ("stDef", CAM_Position)
    ]


# CAM_FeatureDescSize Structure
class CAM_FeatureDescSize(ctypes.Structure):  # Change if FeatureDescElement
    _fields_ = [
        ("stMin", CAM_Size),
        ("stMax", CAM_Size),
        ("stRes", CAM_Size),
        ("stDef", CAM_Size)
    ]


# CAM_FeatureDescTriggerOption Structure
class CAM_FeatureDescTriggerOption(ctypes.Structure):
    _fields_ = [
        ("stRangeFrameCount", CAM_FeatureDescRange),
        ("stRangeDelayTime", CAM_FeatureDescRange)
    ]

    def __eq__(self, other):
        return self.stRangeFrameCount == other.stRangeFrameCount and self.stRangeDelayTime == other.stRangeDelayTime

    def __ne__(self, other):
        return self.stRangeFrameCount != other.stRangeFrameCount or self.stRangeDelayTime != other.stRangeDelayTime


# CAM_FeatureDescFormat Structure
class CAM_FeatureDescFormat(ctypes.Structure):
    _fields_ = [
        ("stFormat", CAM_Format),
        ("uiImageWidth", ctypes.c_uint32),
        ("uiImageHeight", ctypes.c_uint32),
        ("uiImageWidthMin", ctypes.c_uint32),
        ("uiImageHeightMin", ctypes.c_uint32),
        ("uiImageWidthRes", ctypes.c_uint32),
        ("uiImageHeightRes", ctypes.c_uint32),
        ("uiBitPerPixel", ctypes.c_uint32),
        ("wszComment", ctypes.c_wchar * CAM_FEA_COMMENT_MAX),
        ("uiTriggerListCount", ctypes.c_uint32),
        ("stTriggerList", CAM_FeatureDescElement * 3),  # ectmTriggerMax = 3
        ("stDescArea", CAM_FeatureDescArea),
        ("stDescPosition", CAM_FeatureDescPosition),
        ("stDescSize", CAM_FeatureDescSize)
    ]


# CAM_FeatureDesc Structure
class CAM_FeatureDesc(ctypes.Structure):
    _fields_ = [
        ("uiFeatureId", ctypes.c_uint32),
        ("uiListCount", ctypes.c_uint32),
        ("eFeatureDescType", ctypes.c_int),         # Using ctypes.c_int for the enum field
        ("union_data", ctypes.c_void_p)             # Define the appropriate union type
    ]


# <For Image> ##########################################
# CAM_Image Structure
class CAM_Image(ctypes.Structure):
    _fields_ = [
        ("pDataBuffer", ctypes.c_void_p),       # pDataBuffer is set in the driver (includes image info)
        ("uiDataBufferSize", ctypes.c_uint32),  # uiDataBufferSize is set by the application.
        ("uiImageSize", ctypes.c_uint32),       # set in the SDK (from driver) or used by the application.
        ("uiEndTime", ctypes.c_uint32),         # set in the SDK (from driver) or used by the application.
        ("uiEndTime64", ctypes.c_uint64),       # set in the SDK (from driver) or used by the application.
        ("uiFrameCount", ctypes.c_uint64),      # set in the SDK (from driver) or used by the application.
        ("uiRefCount", ctypes.c_uint32)         # set in the SDK (from driver) or used by the application.
    ]

    def __init__(self):
        super().__init__()
        self.pDataBuffer = None
        self.uiDataBufferSize = 0
        self.uiImageSize = 0
        self.uiEndTime = 0
        self.uiEndTime64 = 0
        self.uiFrameCount = 0
        self.uiRefCount = 0


# CAM_ImageInfo Structure
class CAM_ImageInfo(ctypes.Structure):
    _pack_ = 1  # Ensures that the struct uses 1-byte alignment for the fields
    _fields_ = [
        ("usFrameNo", ctypes.c_ushort),
        ("usTrggerOptionNo", ctypes.c_ushort),
        ("usMultiExposureTimeNo", ctypes.c_ushort),
        ("ucReserve006", ctypes.c_ubyte * 2),
        ("uiExposureTime", ctypes.c_uint),
        ("uiFocusLevelR", ctypes.c_uint),
        ("uiFocusLevelGr", ctypes.c_uint),
        ("uiFocusLevelGb", ctypes.c_uint),
        ("uiFocusLevelB", ctypes.c_uint),
        ("ucReserve028", ctypes.c_ubyte * 36),
        ("ucCameraType", ctypes.c_ubyte),
        ("ucImageMode", ctypes.c_ubyte),
        ("ucImageColor", ctypes.c_ubyte),
        ("ucTriggerMode", ctypes.c_ubyte),
        ("uiSerialNo", ctypes.c_uint),
        ("uiFwVersion", ctypes.c_uint),
        ("uiFpgaVersion", ctypes.c_uint),
        ("usUsbDcVersion", ctypes.c_ushort),
        ("ucReserve082", ctypes.c_ubyte * 2),
        ("usImageWidth", ctypes.c_ushort),
        ("usImageHeight", ctypes.c_ushort),
        ("usRoiLeft", ctypes.c_ushort),
        ("usRoiTop", ctypes.c_ushort),
        ("uiFrameSize", ctypes.c_uint),
        ("ucExposureMode", ctypes.c_ubyte),
        ("cExposureBias", ctypes.c_byte),
        ("ucTone", ctypes.c_ubyte),
        ("ucScene", ctypes.c_ubyte),
        ("ucReserve100", ctypes.c_ubyte * 4),
        ("usGain", ctypes.c_ushort),
        ("sBrightness", ctypes.c_short),
        ("cSharpness", ctypes.c_byte),
        ("ucCaptureMode", ctypes.c_ubyte),
        ("ucAeStay", ctypes.c_ubyte),
        ("ucMeteringMode", ctypes.c_ubyte),
        ("usMeteringAreaLeft", ctypes.c_ushort),
        ("usMeteringAreaTop", ctypes.c_ushort),
        ("usMeteringAreaWidth", ctypes.c_ushort),
        ("usMeteringAreaHeight", ctypes.c_ushort),
        ("sHue", ctypes.c_short),
        ("sSaturation", ctypes.c_short),
        ("usWhiteBalanceRed", ctypes.c_ushort),
        ("usWhiteBalanceBlue", ctypes.c_ushort),
        ("usDefect", ctypes.c_ushort),
        ("usWhiteBalanceGreen", ctypes.c_ushort),
        ("ucReserve132", ctypes.c_ubyte * 4),
        ("ucReserve136", ctypes.c_ubyte * 4),
        ("cWhiteBalance", ctypes.c_byte),
        ("ucReserve140", ctypes.c_ubyte),
        ("usAutoWhiteBalanceRed", ctypes.c_ushort),
        ("usAutoWhiteBalanceGreen", ctypes.c_ushort),
        ("usAutoWhiteBalanceBlue", ctypes.c_ushort),
        ("usAutoWhiteBalanceX", ctypes.c_ushort),
        ("usAutoWhiteBalanceY", ctypes.c_ushort),
        ("ucReserve152", ctypes.c_ubyte),
        ("cIrcfAdaptor", ctypes.c_byte),
        ("usDefect2", ctypes.c_ushort),
        ("ucReserve156", ctypes.c_ubyte * 4),
        ("ucReserve160", ctypes.c_ubyte * 96),
    ]


CAM_IMG_INFO_SIZE = ctypes.sizeof(CAM_ImageInfo)


# CAM_ImageInfoEx Structure
class CAM_ImageInfoEx(ctypes.Structure):
    _fields_ = [
        ("ucInfo", ctypes.c_ubyte * CAM_IMG_INFO_SIZE),
    ]

    def __init__(self):
        super().__init__()
        self.stInfo = CAM_ImageInfo()

    def copy_into(self, pInfo):
        for i, byte in enumerate(pInfo):
            self.ucInfo[i] = byte

    def get_info(self, stImage):
        self.copy_into(((ctypes.c_ubyte * stImage.uiImageSize).from_address(ctypes.addressof(stImage.pDataBuffer))))
        return self.stInfo


# <For Command> ########################################
# CAM_CMD_GetFrameSize Structure
class CAM_CMD_GetFrameSize(ctypes.Structure):
    _fields_ = [
        ("uiFrameSize", ctypes.c_uint32),      # [out] frame buffer size (include ImageInfo)
        ("uiFrameInterval", ctypes.c_uint32),  # [out] frame interval
        ("uiRShutterDelay", ctypes.c_uint32)   # [out] RSutter delay (usec)
    ]


# CAM_CMD_StartFrameTransfer Structure
class CAM_CMD_StartFrameTransfer(ctypes.Structure):
    _fields_ = [
        ("uiImageBufferNum", ctypes.c_uint32)  # [in] Driver allocates memory by this parameter. (1 - 128)
    ]


# CAM_CMD_IsTransferStarted Structure
class CAM_CMD_IsTransferStarted(ctypes.Structure):
    _fields_ = [
        ("bStarted", ctypes.c_bool)  # [out] true:Started, false:Stopped
    ]


# CAM_CMD_FrameDropless Structure
class CAM_CMD_FrameDropless(ctypes.Structure):
    _fields_ = [
        ("bSet", ctypes.c_bool),  # [in] true:Set, false:Get
        ("bOnOff", ctypes.c_bool)  # [in/out] true:ON, false:OFF
    ]


# CAM_CMD_Grouping Structure
class CAM_CMD_Grouping(ctypes.Structure):
    _fields_ = [
        ("bSet", ctypes.c_bool),    # [in] true:Set, false:Get
        ("ucGroup", ctypes.c_ubyte * CAM_DEVICE_MAX)  # [in/out]
    ]


# CAM_CMD_GetSdkVersion Structure
class CAM_CMD_GetSdkVersion(ctypes.Structure):
    _fields_ = [
        ("wszSdkVersion", ctypes.c_wchar * CAM_VERSION_MAX)  # [out]
    ]


# CAM_CMD_ControlCis Structure
class CAM_CMD_ControlCis(ctypes.Structure):
    _fields_ = [
        ("bSet", ctypes.c_bool),  # [in] true:Set, false:Get
        ("ucState", ctypes.c_ubyte)  # [in/out] 0:Down, 1:Run
    ]


# CAM_CMD_CheckFwVersion Structure
class CAM_CMD_CheckFwVersion(ctypes.Structure):
    _fields_ = [
        ("bValid", ctypes.c_bool),  # [out] true:Valid, false:Invalid
        ("wszInvalidReason", ctypes.c_wchar * CAM_CMD_STRING_MAX)  # [out]
    ]


# CAM_CMD_FovSize Structure
class CAM_CMD_FovSize(ctypes.Structure):
    # [in] Fov-Type
    # 0: OFF, 1: Full, 2: HD, 3: 25Phi, 4: 22Phi, 5: 16Phi
    _fields_ = [
        ("uiFovType", ctypes.c_uint32),
        ("bFreeRoi", ctypes.c_bool),  # [in] Is free setting
        ("stFovSize", CAM_Size),     # [out] FovSize-Value
        ("stDeskSize", CAM_FeatureDescSize),  # [out] RoiSize-Desk
        ("stDeskPosition", CAM_FeatureDescPosition),  # [out] RoiPosition-Desk
        ("stDeskArea", CAM_FeatureDescArea)  # [out] MeteringArea-Desk
    ]


# CAM_CMD_FovRoi Structure
class CAM_CMD_FovRoi(ctypes.Structure):
    _fields_ = [
        ("stSize", CAM_Size),       # [in] RoiSize-Value
        ("stPosition", CAM_Position),  # [in] RoiPosition-Value
        ("stArea", CAM_Area)         # [in] MeteringArea-Value
    ]


# <For Event> ##########################################
# CAM_EventImageReceived Structure
class CAM_EventImageReceived(ctypes.Structure):
    _fields_ = [
        ("uiTick", ctypes.c_uint32),
        ("uiTick64", ctypes.c_uint64),
        ("uiFrameNo", ctypes.c_uint32),
        ("uiRemained", ctypes.c_uint32)
    ]


# CAM_EventFeatureChanged Structure
class CAM_EventFeatureChanged(ctypes.Structure):
    _fields_ = [
        ("uiTick", ctypes.c_uint32),
        ("uiTick64", ctypes.c_uint64),
        ("uiFeatureId", ctypes.c_uint32),
        ("stVariant", CAM_Variant)
    ]


# CAM_EventSignal Structure
class CAM_EventSignal(ctypes.Structure):
    _fields_ = [
        ("uiTick", ctypes.c_uint32),
        ("uiTick64", ctypes.c_uint64),
        ("eEventType", ctypes.c_int)
    ]


# CAM_EventTransError Structure
class CAM_EventTransError(ctypes.Structure):
    _fields_ = [
        ("uiTick", ctypes.c_uint32),
        ("uiTick64", ctypes.c_uint64),
        ("uiUsbErrorCode", ctypes.c_uint32),
        ("uiDriverErrorCode", ctypes.c_uint32),
        ("uiReceivedSize", ctypes.c_uint32),
        ("uiSettingSize", ctypes.c_uint32)
    ]


# CAM_EventBusReset Structure
class CAM_EventBusReset(ctypes.Structure):
    _fields_ = [
        ("uiTick", ctypes.c_uint32),
        ("uiTick64", ctypes.c_uint64),
        ("eBusResetCode", ctypes.c_int),
        ("bImageCleared", ctypes.c_bool)
    ]


# CAM_Event Structure
class CAM_Event(ctypes.Structure):
    class _CAM_Event__union(ctypes.Union):
        _fields_ = [
            ("stImageReceived", CAM_EventImageReceived),
            ("stFeatureChanged", CAM_EventFeatureChanged),
            ("stSignal", CAM_EventSignal),
            ("stTransError", CAM_EventTransError),
            ("stBusReset", CAM_EventBusReset)
        ]

    _fields_ = [
        ("eEventType", ctypes.c_int),
        ("_union", _CAM_Event__union)
    ]


# CAM_NoticeTransError Structure
class CAM_NoticeTransError(ctypes.Structure):
    _fields_ = [
        ("uiTick", ctypes.c_uint32),
        ("uiTick64", ctypes.c_uint64),
        ("uiRequestCode", ctypes.c_uint32),
        ("uiCameraErrorCode", ctypes.c_uint32),
        ("uiUsbErrorCode", ctypes.c_uint32),
        ("uiDriverErrorCode", ctypes.c_uint32)
    ]


# CAM_NoticeGroup Structure
class CAM_NoticeGroup(ctypes.Structure):
    _fields_ = [
        ("uiTick", ctypes.c_uint32),
        ("uiTick64", ctypes.c_uint64),
        ("eCode", ctypes.c_int),
        ("iDetail", ctypes.c_int32),
        ("wszComment", ctypes.c_wchar * CAM_TEXT_MAX)
    ]


# CAM_NoticeInfo Structure

class CAM_NoticeInfo(ctypes.Structure):
    _fields_ = [
        ("uiTick", ctypes.c_uint32),
        ("uiTick64", ctypes.c_uint64),
        ("eCode", ctypes.c_int),
        ("iValue", ctypes.c_int32),
        ("dValue", ctypes.c_double),
        ("bValue", ctypes.c_bool),
        ("wszText", ctypes.c_wchar * CAM_TEXT_MAX)
    ]


# CAM_Notice Structure
class CAM_Notice(ctypes.Structure):
    class _CAM_Notice__union(ctypes.Union):
        _fields_ = [
            ("stTransError", CAM_NoticeTransError),
            ("stGroup", CAM_NoticeGroup),
            ("stInfo", CAM_NoticeInfo)
        ]

    _fields_ = [
        ("eNoticeType", ctypes.c_int),
        ("_union", _CAM_Notice__union)
    ]


# <Other> ############################################
# Structure for CAM_CMD_GET_PHI_RESOLUTION
class CAM_CMD_PhiResolution(ctypes.Structure):
    _fields_ = [
        ("dPhi", ctypes.c_double),  # [in] (Ex.) 16.8=16.8Phi
        ("uiWidth", ctypes.c_uint32),  # [out]
        ("uiHeight", ctypes.c_uint32)  # [out]
    ]


# Structure for TEST_CMD_GET_METERING_AIM
class TEST_CMD_GetMeteringAim(ctypes.Structure):
    _fields_ = [
        ("usArrivalRate", ctypes.c_uint16)  # [out]
    ]


# Structure for TEST_CAM_CMD_SHADING_DATA
class TEST_CAM_CMD_ShadingData(ctypes.Structure):
    _fields_ = [
        ("uiMode", ctypes.c_uint32),  # [in] 1: Get size, 2: Make, 3: Send, 4: Clear
        ("uiDataSize", ctypes.c_uint32),  # [in/out] Shading data size
        ("pucData", ctypes.POINTER(ctypes.c_ubyte))  # [in/out] Shading data (Allocate memory by application)
    ]


# Structure for TEST_CAM_CMD_SCENE_AUTO_MODE
class TEST_CAM_CMD_SceneAutoMode(ctypes.Structure):
    _fields_ = [
        ("bSet", ctypes.c_bool),  # [in] true:Set, false:Get
        ("bMode", ctypes.c_bool)  # [in/out] true:ON, false:OFF
    ]
