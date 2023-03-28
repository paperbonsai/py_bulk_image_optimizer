import os

# Check if PIL and tqdm modules are installed
try:
    from PIL import Image
    from tqdm import tqdm
except ImportError:
    print("Required modules PIL and/or tqdm not found. Please install them before running this script.")
    exit()

def compress_and_convert_image(file_path, output_path, quality=85):
    try:
        with Image.open(file_path) as img:
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                alpha = img.convert('RGBA').split()[-1]
                bg = Image.new('RGBA', img.size, (0, 0, 0, 0))
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

    # Get list of PNG and JPEG images in input folder
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f)) and
                   os.path.splitext(f)[-1].lower() in ('.png', '.jpg', '.jpeg') and f != 'optimized']

    # Set up main tqdm progress bar
    main_pbar = tqdm(total=len(image_files), unit='file')

    num_successful = 0
    num_failed = 0

    for filename in image_files:
        file_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + '.webp'
        output_path = os.path.join(output_folder, output_filename)

        success, saved_percentage = compress_and_convert_image(file_path, output_path)

        if success:
            main_pbar.update(1)
            num_successful += 1
        else:
            num_failed += 1

    main_pbar.close()
    print(f"Image compression completed! {num_successful} files compressed successfully, {num_failed} files failed compression.")

if __name__ == "__main__":
    input_folder = "images"
    output_folder = "images/optimized"
    main(input_folder, output_folder)
