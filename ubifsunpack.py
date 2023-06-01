import os
import subprocess

def unpack_ubifs():
    try:
        # Prompt for UBIFS image path
        ubifs_image_path = input("Enter the path to the UBIFS image file: ")
        if not os.path.isfile(ubifs_image_path):
            raise FileNotFoundError("Invalid UBIFS image file path.")

        # Prompt for output directory
        output_directory = input("Enter the path to the output directory: ")
        if not os.path.isdir(output_directory):
            raise NotADirectoryError("Invalid output directory path.")

        # Create the output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)

        # Unpack the UBIFS image using the 'mkfs.ubifs' command
        subprocess.run(['mkfs.ubifs', '-d', output_directory, '-r', ubifs_image_path], check=True)

        print('Unpacking completed successfully!')

    except (FileNotFoundError, NotADirectoryError) as e:
        print('Error:', str(e))
    except subprocess.CalledProcessError as e:
        print('Error occurred while unpacking UBIFS image:', str(e))

# Call the function to start the unpacking process
unpack_ubifs()
