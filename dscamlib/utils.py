from .definitions.error_codes import *
from .definitions.constants import ECamFeatureDescType, ECamVariantRunType


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


def get_feature_display_string(feature_value, feature_desc):
    """
    Converts a feature value into a human-readable string based on its description.

    :param feature_value: A CAM_FeatureValue object.
    :param feature_desc: A CAM_FeatureDesc object corresponding to the feature value.
    :return: A human-readable string representing the feature value.
    """
    str_value = "(unknown)"

    # Depending on the description type, format the feature value
    if feature_desc.eFeatureDescType == ECamFeatureDescType.edesc_ElementList.value:
        for i in range(feature_desc.uiListCount):
            if feature_desc.stElementList[i].varValue == feature_value.stVariant:
                str_value = feature_desc.stElementList[i].wszComment
                break

    elif feature_desc.eFeatureDescType == ECamFeatureDescType.edesc_Range.value:
        if feature_value.stVariant.eVarType == ECamVariantRunType.evrt_int32.value:
            str_value = str(feature_value.stVariant.i32Value)
        elif feature_value.stVariant.eVarType == ECamVariantRunType.evrt_uint32.value:
            str_value = str(feature_value.stVariant.ui32Value)

    elif feature_desc.eFeatureDescType == ECamFeatureDescType.edesc_Area.value:
        str_value = "{},{},{},{}".format(
            feature_value.stVariant.stArea.uiLeft,
            feature_value.stVariant.stArea.uiTop,
            feature_value.stVariant.stArea.uiWidth,
            feature_value.stVariant.stArea.uiHeight)

    # Add other cases as needed...

    return str_value


def save_image(stImage, path):
    print(stImage)
    print(path)
