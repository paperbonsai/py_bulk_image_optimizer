import os
from PIL import Image
from tqdm import tqdm

def compress_and_convert_image(file_path, output_path, quality=85):
    try:
        with Image.open(file_path) as img:
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                alpha = img.convert('RGBA').split()[-1]
                bg = Image.new('RGBA', img.size, (255, 255, 255, 255))
                bg.paste(img, mask=alpha)
                img = bg
            img.save(output_path, 'WebP', quality=quality, method=6, lossless=False)
        original_size = os.path.getsize(file_path)
        compressed_size = os.path.getsize(output_path)
        saved_percentage = (1 - (compressed_size / original_size)) * 100
        return True, saved_percentage
    except (IOError, OSError) as e:
        print(f"Error opening/saving {file_path}: {e}")
    return False, 0

def main(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in tqdm(os.listdir(input_folder)):
        if filename == 'optimized':
            continue

        file_path = os.path.join(input_folder, filename)
        file_extension = os.path.splitext(file_path)[-1].lower()

        if file_extension not in ('.png', '.jpg', '.jpeg'):
            print(f"Skipping {filename} as it is not a PNG or JPEG image")
            continue

        output_filename = os.path.splitext(filename)[0] + '.webp'
        output_path = os.path.join(output_folder, output_filename)

        success, saved_percentage = compress_and_convert_image(file_path, output_path)

        if success:
            print(f"Optimized image saved as {output_path}. Saved {saved_percentage:.2f}% space")
        else:
            print(f"Failed to optimize {filename}")

    print("Image compression completed!")

if __name__ == "__main__":
    input_folder = "images"
    output_folder = "images/optimized"
    main(input_folder, output_folder)
