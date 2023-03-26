# Python Script for Compressing and Converting Images to WebP Format

This is a Python script that compresses and converts PNG and JPEG images to the WebP format using the Pillow library. The script takes two input arguments: input_folder and output_folder, which represent the directory containing the original images and the directory where the compressed images will be saved, respectively.

## The script uses the following steps to compress and convert each image
1. Check if the image is a PNG or JPEG file. If it is not, the script skips the image and moves on to the next one.
2. Open the image using the Pillow library and convert it to the RGBA mode if it has transparency or is in the LA mode. This is done to ensure that the image has an alpha channel, which is required for the WebP format.
3. Create a new RGBA image with a white background and paste the original image onto it. This is done to fill any transparent pixels in the original image with white.
4. Save the new image in the WebP format with the specified quality, compression method, and lossless settings.
5. Calculate the original size and compressed size of the image and calculate the percentage of space saved by the compression.
6. Print the success or failure message for the optimization of each image.

The script uses the tqdm library to display a progress bar while optimizing the images. It also creates the output_folder if it does not already exist. The script saves the optimized images with the same name as the original images but with the .webp extension in the output_folder.

Finally, the script prints a message indicating that the image compression process has completed.

## How to install and run this script
To run this Python script, you will need to install the required libraries mentioned in the code. You can install them using the following commands in the terminal or command prompt:
1. Pillow library: pip install Pillow
2. tqdm library: pip install tqdm

Once you have installed these libraries, you can save the code in a Python file with a .py extension and run it using the command python filename.py in the terminal or command prompt. Make sure to replace filename with the actual name of your Python file.

Before running the script, make sure that the directory containing the images you want to optimize exists and that you have the necessary read and write permissions to access that directory. You may also need to modify the input and output folder paths in the main() function to match the directory paths on your system.
