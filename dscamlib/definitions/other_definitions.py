# other_definitions.py

# Max Number of Device Management
CAM_DEVICE_MAX = 32

# Error Message Max Length
CAM_ERRMSG_MAX = 256

# Version Max Length
CAM_VERSION_MAX = 16

# Text Max Length
CAM_TEXT_MAX = 256

# Name Max Length
CAM_NAME_MAX = 32

# Max Number of Feature ID
CAM_FEA_CAPACITY = 64

# Max Length of Variant Character String
CAM_FEA_VARIANT_MAX = 256

# Comment Max Length
CAM_FEA_COMMENT_MAX = 64

# Max Number of Feature Attribute List
CAM_FEA_DESC_LIST_MAX = 256

# Max Number of Multi Exposure Time
CAM_FEA_MULTIEXPOSURETIME_MAX = 15

# Max Length of Frame Size
CAM_FEA_FRAME_SIZE_MAX = 143460000  # ((6000 * 6) * (3984 + 1))

# Command Strings
# OnePush functions
CAM_CMD_ONEPUSH_AE = "CAM_CMD_ONEPUSH_AE"
CAM_CMD_ONEPUSH_WHITEBALANCE = "CAM_CMD_ONEPUSH_WHITEBALANCE"
CAM_CMD_ONEPUSH_SOFTTRIGGER = "CAM_CMD_ONEPUSH_SOFTTRIGGER"
CAM_CMD_ONEPUSH_TRIGGERCANCEL = "CAM_CMD_ONEPUSH_TRIGGERCANCEL"

# Receive image commands
CAM_CMD_GET_FRAMESIZE = "CAM_CMD_GET_FRAMESIZE"  # Get frame size (include ImageInfo)
CAM_CMD_START_FRAMETRANSFER = "CAM_CMD_START_FRAMETRANSFER"  # Start frame transfer
CAM_CMD_STOP_FRAMETRANSFER = "CAM_CMD_STOP_FRAMETRANSFER"  # Stop frame transfer
CAM_CMD_IS_TRANSFER_STARTED = "CAM_CMD_IS_TRANSFER_STARTED"  # Check transfer started

# FOV commands
CAM_CMD_FOV_SIZE = "CAM_CMD_FOV_SIZE"  # Set FOV, Get size information
CAM_CMD_FOV_ROI = "CAM_CMD_FOV_ROI"  # Set ROI in FOV

# Frame dropless mode command
CAM_CMD_FRAME_DROPLESS = "CAM_CMD_FRAME_DROPLESS"  # Frame dropless mode

# Group camera command
CAM_CMD_GROUPING = "CAM_CMD_GROUPING"  # Grouping settings

# Other commands
CAM_CMD_GET_SDKVERSION = "CAM_CMD_GET_SDKVERSION"  # Get SDK's version
CAM_CMD_CONTROL_CIS = "CAM_CMD_CONTROL_CIS"  # Control CIS power
CAM_CMD_CHECK_FW_VERSION = "CAM_CMD_CHECK_FW_VERSION"  # Check valid FW version
CAM_CMD_GET_PHI_RESOLUTION = "CAM_CMD_GET_PHI_RESOLUTION"  # Get resolution each of phi (for Digital Sight 10)

# Test commands
TEST_CMD_GET_METERING_AIM = "TEST_CMD_GET_METERING_AIM"
TEST_CAM_CMD_SHADING_DATA = "TEST_CAM_CMD_SHADING_DATA"
TEST_CAM_CMD_SCENE_AUTO_MODE = "TEST_CAM_CMD_SCENE_AUTO_MODE"

# Max Number of Command string
CAM_CMD_STRING_MAX = 128
