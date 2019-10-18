# quip manifest file generator
PURPOSE: FIND IN PathDB httplinks.csv, CREATE manifest.csv

1) Download httplinks.csv from PathDB
2) REMOVE CSV HEADER!
3) `ls -l | awk '{print $9}' > ~/myList.list`  # Make sure no blank lines or 'extra' files that don't belong.
4) Run FileGen.java with parameters /path/to/myList.list and /path/to/httplinks.csv
5) Copy the output
