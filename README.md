#Python Script for Compressing and Converting Images to WebP

This is a Python script that compresses and converts PNG and JPEG images to the WebP format using the Pillow library. The script takes two input arguments: input_folder and output_folder, which represent the directory containing the original images and the directory where the compressed images will be saved, respectively.

##The script uses the following steps to compress and convert each image
1. The script imports necessary modules and packages including os, PIL, and tqdm.
2. The compress_and_convert_image function is defined, which takes a file path, an output path, and a quality level as parameters. The function opens the image file, checks if it has transparency, creates a new transparent background, pastes the original image onto the new background, and saves the image as a WebP file with the specified quality level. The function returns a boolean value indicating whether the image was successfully compressed and converted, and the percentage of disk space saved.
3. The main function is defined, which takes an input folder and an output folder as parameters. The function checks if the output folder exists, and creates it if it doesn't. The function then iterates through each file in the input folder, checks if its file extension is .png, .jpg, or .jpeg, and skips the file if it isn't. For each image file, the function calls the compress_and_convert_image function with the input file path and the output file path. If the image is successfully compressed and converted, the output file is saved in the output folder with the same filename and a .webp extension. The function also prints a message indicating the success or failure of each image compression.
4. If the script is run directly (i.e., not imported as a module), the main function is called with two arguments specifying the input and output folders. The script uses the tqdm package to display a progress bar as the images are processed.

The script uses the tqdm library to display a progress bar while optimizing the images. It also creates the output_folder if it does not already exist. The script saves the optimized images with the same name as the original images but with the .webp extension in the output_folder.

Finally, the script prints a message indicating that the image compression process has completed.

## How to install and run this script
To run this Python script, you will need to install the required libraries mentioned in the code. You can install them using the following commands in the terminal or command prompt:
1. Pillow library: pip install Pillow
2. tqdm library: pip install tqdm

Once you have installed these libraries, you can save the code in a Python file with a .py extension and run it using the command python filename.py in the terminal or command prompt. Make sure to replace filename with the actual name of your Python file.

Before running the script, make sure that the directory containing the images you want to optimize exists and that you have the necessary read and write permissions to access that directory. You may also need to modify the input and output folder paths in the main() function to match the directory paths on your system.
