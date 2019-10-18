import sys
import os


def main(my_list, image_list):

    if not os.path.isfile(my_list):
        print("File path {} does not exist. Exiting...".format(my_list))
        sys.exit()

    if not os.path.isfile(image_list):
        print("File path {} does not exist. Exiting...".format(my_list))
        sys.exit()

    try:
        with open(my_list) as fa:
            for line_a in fa:
                with open(image_list) as fb:
                    for line_b in fb:
                        x = line_a.replace(".json", "").strip()
                        y = line_b.replace(".svs", "").strip()
                        row = line_b.split(",")
                        if y in x:
                            print(row[1] + "," + row[2] + "," + row[3] + "," + line_a.strip())
                            continue

    except Exception as ex:
        print(ex)
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('\nUSAGE:\n    python ' + os.path.basename(__file__) + ' /path/to/yourImageList.list /path/to/httplinks.csv')
    else:
        main(sys.argv[1], sys.argv[2])
