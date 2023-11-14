from .definitions.error_codes import *


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


def save_image(stImage, path):
    print(stImage)
