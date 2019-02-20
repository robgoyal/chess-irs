import glob
import argparse

from frame import Frame


def main(input_folder, output_folder):
    input_images = glob.glob(input_folder + "/*.jpg")
    output_folder = output_folder

    for img in input_images:
        image_name = img.split("/")[-1]
        f = Frame()



if __name__ == "__main__":
    p = argparse.ArgumentParser(description= \
                                    'Find, crop and create FEN from image.')

    p.add_argument('--input_folder', type=str, \
                   help='Input Folder Path with images')
    p.add_argument('--output_folder', type=str, \
                   help='Output Folder Path with images')

    args = p.parse_args()
    main(args.input_folder, args.output_folder)