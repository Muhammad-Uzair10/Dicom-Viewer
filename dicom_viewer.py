import pydicom
import matplotlib.pyplot as plt

# Load the DICOM file
dicom_path = r'path to your file.dcm'
dataset = pydicom.dcmread(dicom_path)

# Check if the file contains multiple frames
if hasattr(dataset, 'NumberOfFrames'):
    num_frames = dataset.NumberOfFrames
    print(f"Number of frames: {num_frames}")

    # Iterate through the frames and display each one
    for i in range(num_frames):
        frame = dataset.pixel_array[i]
        plt.imshow(frame, cmap='gray')
        plt.title(f"Frame {i + 1}")
        plt.show()
else:
    # Display the single frame
    frame = dataset.pixel_array
    plt.imshow(frame, cmap='gray')
    plt.show()
