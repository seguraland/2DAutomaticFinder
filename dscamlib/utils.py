from .definitions.error_codes import *
from .definitions.constants import ECamEventType, ECamFeatureDescType


def get_error_message(error_code):
    error_messages = {
        LX_OK: "Operation successful | Code 0 | LX_OK",
        LX_ERR_UNEXPECTED: "Unexpected error occurred | Code -1 | LX_ERR_UNEXPECTED",
        LX_ERR_NOTIMPL: "Not implemented | Code -2 | LX_ERR_NOTIMPL",
        LX_ERR_OUTOFMEMORY: "Out of memory | Code -3 | LX_ERR_OUTOFMEMORY",
        LX_ERR_INVALIDARG: "Invalid argument | Code -4 | LX_ERR_INVALIDARG",
        LX_ERR_NOINTERFACE: "No interface | Code -5 | LX_ERR_NOINTERFACE",
        LX_ERR_POINTER: "Pointer error | Code -6 | LX_ERR_POINTER",
        LX_ERR_HANDLE: "Handle error | Code -7 | LX_ERR_HANDLE",
        LX_ERR_ABORT: "Operation aborted | Code -8 | LX_ERR_ABORT",
        LX_ERR_FAIL: "General failure | Code -9 | LX_ERR_FAIL",
        LX_ERR_ACCESSDENIED: "Access denied | Code -10 | LX_ERR_ACCESSDENIED"
    }

    return error_messages.get(error_code, f"Unknown error | Code {error_code}")


def fd_area_to_dict(area_data):
    return {
        "stMin": area_data.stMin.to_dict(),
        "stMax": area_data.stMax.to_dict(),
        "stRes": area_data.stRes.to_dict(),
        "stDef": area_data.stDef.to_dict(),
    }


def process_feature_desc(feature_desc):
    readable_desc = {
        "Feature ID": feature_desc.uiFeatureId,
        "List Count": feature_desc.uiListCount,
        "Description Type": ECamFeatureDescType(feature_desc.eFeatureDescType).name,
    }

    # Check the type of feature description and process accordingly
    if feature_desc.eFeatureDescType == ECamFeatureDescType.edesc_Area.value:
        readable_desc["stArea"] = fd_area_to_dict(feature_desc.union_data.stArea)

    # Add more if needed
    # if feature_desc.eFeatureDescType == ECamFeatureDescType.edesc_ElementList.value:
    #     readable_desc["ElementList"] = feature_desc.union_data.stElementList
    # ...

    return readable_desc


def save_image(stImage, path):
    print(stImage)


def event_callback(camera_handle, event_ptr, user_data):
    # Access the event structure
    event = event_ptr.contents

    # Check the event type and respond accordingly
    if event.eEventType == ECamEventType.ecetImageReceived.value:
        print("Image received event detected")
        # Add logic to handle the image reception
        # ...

    elif event.eEventType == ECamEventType.ecetFeatureChanged.value:
        print("Feature changed event detected")
        # Handle feature change
        # ...

    elif event.eEventType == ECamEventType.ecetExposureEnd.value:
        print("Exposure end event detected")
        print("")
        # Handle exposure end
        # ...

    # Add additional elif blocks for other event types as needed

    else:
        print(f"Unknown event type: {event.eEventType}")


