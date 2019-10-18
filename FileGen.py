import sys
import os


def main(myList, imageList):

    if not os.path.isfile(myList):
        print("File path {} does not exist. Exiting...".format(myList))
        sys.exit()

    if not os.path.isfile(imageList):
        print("File path {} does not exist. Exiting...".format(myList))
        sys.exit()

    with open(myList) as fp:
        for line in fp:
            print(line)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python ' + os.path.basename(__file__) + ' /path/to/yourImageList.list /path/to/httplinks.csv')
    else:
        main(sys.argv[1], sys.argv[2])
