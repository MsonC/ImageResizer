import os, sys
import PIL
from PIL import Image
import argparse
import glob


# TODO Change the image resize method to be more dynamic. As in add a loop to do the given sizes instead of the presets

default_sizes = ['18', '36', '72']


def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    # width, height = original_image.size
    # print('The original image size is {wide} wide x {height} '
    #       'high'.format(wide=width, height=height))

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    # print('The resized image size is {wide} wide x {height} '
    #       'high'.format(wide=width, height=height))
    resized_image.save(output_image_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        description='Make Twitch Sub Badges. Takes in an image and outputs the correct sizes. Names them too.')
    parser.add_argument('-f', '--folder', action='store', dest='foldername',
                        help='The folder name where the original files and the output files are contained', nargs="*")
    parser.add_argument('-r', '--recursive', action='store_true', default=False, dest='recursive',
                        help='Should it look for files in the folders withing the folder that the program is running?')
    parser.add_argument('-s', '--sizes', action='store', dest='sizes',
                        help='Use your own sizes for the resizing proccess. If this is not provided it will use the defualt sizes. Example: -s 18 36 72', nargs='*')

    results = parser.parse_args()
    if results.recursive == True and results.foldername == None:
        print("Running the recursive code")
        allfiles = []
        subdirs = next(os.walk('.'))[1]
        for s in subdirs:
            f = glob.glob(s + "\\*.png")
            if len(f) == 1:
                allfiles.append([s, f[0]])
            else:
                print("Too many files in directory: {}".format(str(s)))
        
        for x in range(len(allfiles)):
            if results.sizes != None:
                for size in results.sizes:
                    resize_image(input_image_path=str(allfiles[x][1]),
                        output_image_path="{}\\{}px - {}.png".format(
                                str(allfiles[x][0]), str(size), str(allfiles[x][0])),
                                size=(int(size), int(size)))
            else:
                for size in default_sizes:
                    resize_image(input_image_path=str(allfiles[x][1]),
                                 output_image_path="{}\\{}px - {}.png".format(
                        str(allfiles[x][0]), str(size), str(allfiles[x][0])),
                        size=(int(size), int(size)))
    elif results.recursive == False and results.foldername != None:
        # print("Running NON-Recursive code")
        dr = os.path.abspath(str(results.foldername[0]))
        files = os.listdir(dr + "\\")
        for x in range(len(files)):
            if results.sizes != None:
                for size in results.sizes:
                    resize_image(input_image_path="{}\\{}".format(str(dr), str(files[x])),
                                 output_image_path="{}\\{}px - {}".format(
                        str(dr), str(size), str(files[x])),
                        size=(int(size), int(size)))
            else:
                for size in default_sizes:
                    resize_image(input_image_path="{}\\{}".format(str(dr), str(files[x])),
                                 output_image_path="{}\\{}px - {}".format(
                        str(dr), str(size), str(files[x])),
                        size=(int(size), int(size)))
    else:
        print("Something went wrong!")
