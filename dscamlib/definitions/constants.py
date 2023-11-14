# constants.py
from enum import Enum
from enum import IntEnum


class ECamDeviceType(IntEnum):
    ecdtUnknown = 0
    eRi2 = 1
    eRi2_Simulator = 2
    eQi2 = 3
    eQi2_Simulator = 4
    eFi3 = 5
    eFi3_Simulator = 6
    eDS10 = 7
    eDS10_Simulator = 8


class ECamFeatureId(Enum):
    eUnknown = 0
    eExposureMode = 1
    eExposureBias = 2
    eExposureTime = 3
    eGain = 4
    eMeteringMode = 5
    eMeteringArea = 6
    eExposureTimeLimit = 7
    eGainLimit = 8
    eCaptureMode = 9
    eBrightness = 13
    eSharpness = 14
    eHue = 15
    eSaturation = 16
    eTone = 17  # Application can't use.(for Debug)
    eWhiteBalanceRed = 18
    eWhiteBalanceBlue = 19
    eWhiteBalanceGreen = 20  # Application can't use.(for Debug)
    eWhiteBalance = 25  # Used by Digital Sight 10 only.(Ri2/Qi2/Fi3 are used by Command)
    ePresets = 26
    eMeteringAim = 27  # Application can't use.(Used by Command)
    eTriggerOption = 33
    eOnePushSoftTrigger = 34  # Application can't use.(Used by Command)
    eMultiExposureTime = 35
    eSignalExposureEnd = 36
    eSignalTriggerReady = 37
    eSignalDeviceCapture = 38
    eExposureOutput = 39  # TTL
    eOnePushTriggerCancel = 40  # Application can't use.(Used by Command)
    eCisPower = 41  # Application can't use.(Used by Command)
    eIrcfAdaptor = 42
    eDefectBlackShading = 48  # Application can't use.(for Debug)
    eDefectPixel = 49  # Application can't use.(for Debug)
    eDefectClump = 50  # Application can't use.(for Debug)
    eDefectFillGamma = 51  # Application can't use.(for Debug)
    eDefectGain = 52  # Application can't use.(for Debug)
    eDefectShading = 53  # Application can't use.(for Debug)
    eDefectMaxMin = 54  # Application can't use.(for Debug)
    eDefectEdge = 55  # Application can't use.(for Debug)
    eDefectVertGainFpn = 56  # Application can't use.(for Debug)
    eDefectImitation = 57  # Application can't use.(for Debug)
    eDefectUserGamma = 58  # Application can't use.(for Debug)
    eDefectAxis = 59  # Application can't use.(for Debug)
    eDefectRgb = 60  # Application can't use.(for Debug)
    eVersion = 61  # Application can't use.(for Debug)
    eStandbyMode = 62  # Application can't use.(for Debug)
    eTemperature = 63  # Application can't use.(Used by Command)
    eDefectJaggy = 73  # Application can't use.(for Debug)
    eDefectFillGammaRev = 74  # Application can't use.(for Debug)
    eDefect3x3 = 75  # Application can't use.(for Debug)
    eDefectRgbToYCbCr = 76  # Application can't use.(for Debug)
    eDefectYCbCrToRGB = 77  # Application can't use.(for Debug)
    eDefectColorToMono = 78  # Application can't use.(for Debug)
    eFormat = 80
    eRoiPosition = 81
    eTriggerMode = 82
    eRoiSize = 83
    eFeatureIdMax = 84


class ECamExposureMode(Enum):
    ecemContinuousAE = 0
    ecemOnePushAE = 1  # Exclude from select list. Application run OnePushAE by command[CAM_CMD_ONEPUSH_AE].
    ecemManual = 2
    ecemMultiExposureTime = 3


class ECamMeteringMode(Enum):
    ecmmAverage = 0
    ecmmPeak = 1


class ECamTone(Enum):
    ectUnknown = 0
    ectWideDinamicRange = 1
    ectContrastWeak = 2
    ectContrastNomal = 3
    ectContrastStrong = 4
    ectLinear = 5
    ectMetalOrganization = 6
    ectContrastEmphasis = 7


class ECamWhiteBalance(Enum):
    ecwbManual = 0
    ecwbOnePush = 1
    ecwbAuto = 2


class ECamPresetsId(Enum):
    ecpiDefault = 0
    ecpiIndustry_WaferIc = 16
    ecpiIndustry_Metal = 17
    ecpiIndustry_CircuitBoard = 18
    ecpiIndustry_Fpd = 19
    ecpiBio_BrightField = 32
    ecpiBio_He = 33
    ecpiBio_Ela = 34
    ecpiBioLed_BrightField = 48
    ecpiBioHighLed_BrightField = 49
    ecpiBioHighLed_He = 50
    ecpiBioHighLed_Ela = 51
    ecpiOther_Asbestos = 64
    ecpiOther_Linear = 80


class ECamSignalOutput(Enum):
    ecsoOff = 0
    ecsoOutput = 1
    ecsoLast = 2


class ECamFormatColor(Enum):
    ecfcUnknown = 0
    ecfcMax = 6
    ecfcRgb24 = 1
    ecfcYuv444 = 2
    ecfcMono16 = 3
    ecfcRgb48 = 4
    ecfcY16 = 5
    ecfcRaw16 = 6


class ECamFormatMode(Enum):
    ecfmUnknown = 0
    ecfmMax = 15
    ecfm4908x3264 = 1
    ecfm2454x1632 = 2
    ecfm1636x1088 = 3
    ecfm818x544 = 4
    ecfm1608x1608 = 5
    ecfm804x804 = 6
    ecfm536x536 = 7
    ecfm22p2136x2136 = 8
    ecfm22p712x712 = 9
    ecfm25p2424x2424 = 10
    ecfm25p808x808 = 11
    ecfm17p1608x1608 = 12
    ecfm17p536x536 = 13
    ecfmH2880x2048 = 1
    ecfmH1440x1024Roi = 2
    ecfmH1440x1024 = 3
    ecfmH3096x2088 = 4
    ecfmH1548x1044 = 5
    ecfmA6000x3984 = 1
    ecfmA3000x1992 = 2
    ecfmA2000x1328 = 3
    ecfmA6104x4086 = 4
    ecfmA6104x2040 = 5
    ecfmA3052x2040 = 6
    ecfmA2040x1360 = 7


class ECamIrcfAdaptor(Enum):
    eciaManual = 0
    eciaUnstable = 1
    eciaPlane = 2
    eciaIrcf = 3


class ECamTriggerMode(Enum):
    ectmOff = 0
    ectmHard = 1
    ectmSoft = 2
    ectmBoth = 3  # Application can't use.
    ectmTriggerMax = 3


class ECamVariantRunType(IntEnum):
    evrt_unknown = 0
    evrt_int32 = 1
    evrt_uint32 = 2
    evrt_int64 = 3
    evrt_uint64 = 4
    evrt_double = 5
    evrt_bool = 6
    evrt_voidptr = 7
    evrt_wstr = 8
    evrt_Area = 9
    evrt_Position = 10
    evrt_TriggerOption = 11
    evrt_MultiExposureTime = 12
    evrt_Format = 13
    evrt_Size = 14


class ECamFeatureDescType(Enum):
    edesc_unknown = 0
    edesc_ElementList = 1
    edesc_Range = 2
    edesc_Area = 3
    edesc_Position = 4
    edesc_TriggerOption = 5
    edesc_FormatList = 6
    edesc_Size = 7


class ECamGroupCaptureMode(Enum):
    egcmNoGroup = 0x00
    egcmSoftHard = 0x10
    egcmSoftSoft = 0x20


class ECamEventType(Enum):
    ecetUnknown = -1
    ecetImageReceived = 0
    ecetFeatureChanged = 1
    ecetExposureEnd = 2
    ecetTriggerReady = 3
    ecetDeviceCapture = 4
    ecetAeStay = 5
    ecetAeRunning = 6
    ecetAeDisable = 7
    ecetTransError = 8
    ecetBusReset = 9
    ecetEventTypeMax = 10


class ECamEventBusResetCode(Enum):
    ecebrcHappened = 1
    ecebrcRestored = 2
    ecebrcFailed = 3


class ECamNoticeType(Enum):
    ecntUnknown = -1
    ecntTransError = 0
    ecntGroup = 1
    ecntInfo = 2
    ecntNoticeTypeMax = 3


class ECamNoticeGroupCode(Enum):
    ecngcEventInsufficient = 1
    ecngcSetFeatureError = 2
    ecngcSetTransError = 3
    ecngcSoftTriggerError = 4
    ecngcSetImageFormatError = 5
    ecngcGetImageDataError = 6
    ecngcBusReset = 7


class ECamNoticeInfoCode(Enum):  # ECamNoticeInfoCode is not used
    ecnicTemperature = 1
    ecnicComment = 2
