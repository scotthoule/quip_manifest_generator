# quip manifest file generator
PURPOSE: FIND IN PathDB httplinks.csv, CREATE manifest.csv

1) Download httplinks.csv from PathDB
2) `ls -l | awk '{print $9}' > ~/myList.list  # Make sure no blank lines or 'extra' files that don't belong.`
3) Run `python manifest_file_generator.py "/path/to/myList.list" "/path/to/httplinks.csv" [manifest_type <map|segmentation>]`
4) Copy pgm output to file or redirect output to file
