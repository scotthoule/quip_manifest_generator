# quip manifest file generator
PURPOSE: FIND IN PathDB httplinks.csv, CREATE manifest.csv

1) Download httplinks.csv from PathDB
2) REMOVE CSV HEADER!
3) `ls -l | awk '{print $9}' > ~/myList.list  # Make sure no blank lines or 'extra' files that don't belong.`
4) Run `python manifest_file_generator.py "/path/to/myList.list" "/path/to/httplinks.csv"`
5) Copy the output
