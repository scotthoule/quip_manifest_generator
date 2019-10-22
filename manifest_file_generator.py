import os
import sys


def main(my_list, image_list, manifest_type):
    if not os.path.isfile(my_list):
        print("File path {} does not exist. Exiting...".format(my_list))
        sys.exit()

    if not os.path.isfile(image_list):
        print("File path {} does not exist. Exiting...".format(my_list))
        sys.exit()

    try:
        if manifest_type == 'segmentation':
            print('segmentdir,studyid,clinicaltrialsubjectid,imageid')

        if manifest_type == 'map':
            print('studyid,clinicaltrialsubjectid,imageid,filename')

        with open(my_list) as fa:
            for line_a in fa:
                with open(image_list) as fb:
                    for line_b in fb:
                        x = line_a[:line_a.find(".")].strip()
                        y = line_b[:line_b.find(".")].strip()
                        row = line_b.strip().split(',')
                        if x in y:
                            if manifest_type == 'map':
                                print(row[1] + "," + row[2] + "," + row[3] + "," + line_a.strip())
                            if manifest_type == 'segmentation':
                                print(line_a.strip() + "," + row[1] + "," + row[2] + "," + row[3])
                            continue

    except Exception as ex:
        print(ex)
        sys.exit(1)


if __name__ == '__main__':
    # 1) Download httplinks.csv from PathDB
    # 2) REMOVE CSV HEADER!
    # 3) ls -l | awk '{print $9}' > ~/myList.list  # Make sure no blank lines or 'extra' files that don't belong.
    if len(sys.argv) < 4:
        print('\nUSAGE:\n    python ' + os.path.basename(
            __file__) + ' /path/to/yourImageList.list /path/to/httplinks.csv manifest_type [map | segmentation]')
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
