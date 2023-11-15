import ctypes

# Load the DSCam.dll
dscam = ctypes.CDLL('./DSCam.dll')

# Define the Other Definition code
CAM_VERSION_MAX = 16
CAM_NAME_MAX = 32
CAM_ERRMSG_MAX = 256
CAM_FEA_CAPACITY = 10

# Define the success code
LX_OK = 0


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


class CAM_FeatureValue(ctypes.Structure):
    _fields_ = [
        ("uiFeatureId", ctypes.c_uint32),
        # stVariant is not fully described, NOTE assume it's a single byte for now
        ("stVariant", ctypes.c_ubyte),
        ("ucTransSize", ctypes.c_ubyte)  # Application doesn't use this
    ]


class Vector_CAM_FeatureValue(ctypes.Structure):
    _fields_ = [
        ("uiCountUsed", ctypes.c_uint32),
        ("uiCapacity", ctypes.c_uint32),
        ("uiPauseTransfer", ctypes.c_uint32),
        ("pstFeatureValue", ctypes.POINTER(CAM_FeatureValue))
    ]


# Define CAM_OpenDevices Function
dscam.CAM_OpenDevices.argtypes = [ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.POINTER(CAM_Device))]
dscam.CAM_OpenDevices.restype = ctypes.c_int

# Define CAM_CloseDevices Function
dscam.CAM_CloseDevices.restype = ctypes.c_int

# Define CAM_Open Function
dscam.CAM_Open.argtypes = [ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.c_uint32,
                           ctypes.POINTER(ctypes.c_wchar)]
dscam.CAM_Open.restype = ctypes.c_int

# Define CAM_Close Function
dscam.CAM_Close.argtypes = [ctypes.c_uint32]
dscam.CAM_Close.restype = ctypes.c_int


# Define local Methods
def GetAllFeatures(camera_handle):
    # Allocate an array of CAM_FeatureValue
    feature_array = (CAM_FeatureValue * CAM_FEA_CAPACITY)()

    # Prepare the Vector_CAM_FeatureValue
    vectFeatureValue = Vector_CAM_FeatureValue()
    vectFeatureValue.uiCapacity = CAM_FEA_CAPACITY
    vectFeatureValue.uiCountUsed = 0
    vectFeatureValue.uiPauseTransfer = 0
    vectFeatureValue.pstFeatureValue = ctypes.cast(feature_array, ctypes.POINTER(CAM_FeatureValue))

    # Call CAM_GetAllFeatures
    result_features = dscam.CAM_GetAllFeatures(camera_handle, ctypes.byref(vectFeatureValue))

    if result_features == LX_OK:
        # Process the features
        print(f"Number of features retrieved: {vectFeatureValue.uiCountUsed}")
        for ivec in range(vectFeatureValue.uiCountUsed):
            feature = vectFeatureValue.pstFeatureValue[ivec]
            print(f"Feature ID: {feature.uiFeatureId}")
    #            print(f"Variant: {feature.stVariant}")
    #            print(f"Trans Size: {feature.ucTransSize}")

    else:
        print("Failed to get all features")

    # Return the results or feature list as needed


uiDeviceCount = ctypes.c_uint32()
ppstCamDevice = ctypes.POINTER(CAM_Device)()

result = dscam.CAM_OpenDevices(ctypes.byref(uiDeviceCount), ctypes.byref(ppstCamDevice))
if result == LX_OK:
    print(f"Successfully opened {uiDeviceCount.value} devices.")

    for i in range(uiDeviceCount.value):
        device = ppstCamDevice[i]
        print(f"Device {i}:")
        print(f"  Type: {device.eCamDeviceType}")
        print(f"  Serial Number: {device.uiSerialNo}")
        #        print(f"  Firmware Version: {device.wszFwVersion}")
        #        print(f"  Fpga Version: {device.wszFpgaVersion}")
        #        print(f"  Usb Version: {device.wszUsbVersion}")
        #        print(f"  Usb Dc Version: {device.wszUsbDcVersion}")
        #        print(f"  Driver Version: {device.wszDriverVersion}")
        print(f"  Camera Name: {device.wszCameraName}")

else:
    print("Failed to open devices.")
    # Handle error

# Call CAM_Open (NEED CLOSE)
uiDeviceIndex = ctypes.c_uint32(0)  # Choose the device index (0 for the first device, for example)
uiCameraHandle = ctypes.c_uint32()  # Variable to store the camera handle
szError = (ctypes.c_wchar * CAM_ERRMSG_MAX)()  # Error message buffer

lResult = dscam.CAM_Open(uiDeviceIndex, ctypes.byref(uiCameraHandle), CAM_ERRMSG_MAX, szError)
if lResult == LX_OK:
    print(f"Successfully opened camera with handle: {uiCameraHandle.value}")
    # Disp feature list
    # m_lstFeature.DeleteAllItems(); << GUI? remove
    # Call the GetAllFeatures function
    GetAllFeatures(uiCameraHandle)
    # GetAllFeaturesDesc();
    # DispAllFeaturesName();
    # DispAllFeaturesValue();
    # StartGetImageThread();
    # m_isOpened = TRUE;

else:
    print(f"Open Error. [{szError.value}]")
