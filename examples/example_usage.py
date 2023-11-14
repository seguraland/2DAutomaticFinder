# example_usage.py
from dscamlib.functions import CAM_OpenDevices, CAM_Open, GetAllFeatures, GetAllFeaturesDesc


def run_example():
    print("Running example...")
    # Open devices and print their details
    devices = CAM_OpenDevices()
    if isinstance(devices, list):
        print(f"Successfully opened {len(devices)} devices.")
        for i, device in enumerate(devices):
            print(f"Device {i}: {device}")

        # For simplicity, let's open the first device if available
        if devices:
            device_index = 0
            success, camera_handle, error_msg = CAM_Open(device_index)
            if success:
                print(f"Opened camera with handle: {camera_handle}")

                # Additional camera operations here...
                # Get and print all features of the camera
                features = GetAllFeatures(camera_handle)
                if isinstance(features, list):
                    print("Features: ", features)

                    # Get and print all feature descriptions
                    feature_descs = GetAllFeaturesDesc(camera_handle, features)
                    print("sdfsdfsfsfsfsfsfsfd")
                    print(feature_descs)
                    if isinstance(feature_descs, list):
                        print("Feature Descriptions: ", feature_descs)
                    else:
                        print(feature_descs)  # Error message
                else:
                    print(features)  # Error message
            else:
                print(f"Failed to open camera: {error_msg}")

            # Get and print all features of the camera
    #         # GetAllFeatures(camera_handle)

    # Close the camera
    #         # CAM_Close(camera_handle)

    else:
        print(devices)  # Print error message
    #
    # # Close all devices
    # # CAM_CloseDevices()


if __name__ == "__main__":
    run_example()
