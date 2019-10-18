/**
 * PURPOSE: FIND IN PathDB httplinks.csv, CREATE manifest.csv
 */
package edu.stonybrook.bmi;

import java.io.BufferedReader;
import java.io.FileReader;

public class FileGen {

    public static void main(String[] args) {
        try {
            String myList = args[0];
            String imageList = args[1];

            // 1) Download httplinks.csv from PathDB
            // 2) REMOVE CSV HEADER!
            // 3) ls -l | awk '{print $9}' > ~/myList.list  # Make sure no blank lines or 'extra' files that don't belong.
            manifest_from_imagelist(myList, imageList);

        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("ArrayIndexOutOfBoundsException caught");
        }

    }

    public static void manifest_from_imagelist(String myList, String imageList) {

        String line;
        String line1;

        try {
            FileReader fileReader = new FileReader(myList);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            boolean found;

            System.out.println("studyid,clinicaltrialsubjectid,imageid,filename");
            while ((line = bufferedReader.readLine()) != null) {
                found = false;
                FileReader fileReader1 = new FileReader(imageList);
                BufferedReader bufferedReader1 = new BufferedReader(fileReader1);
                while ((line1 = bufferedReader1.readLine()) != null) {
                    String x = line.replace(".json", "");
                    String y = line1.replace(".svs", "");
                    String[] row = line1.split(",");
                    if (y.contains(x)) {
                        System.out.println(row[1] + "," + row[2] + "," + row[3] + "," + line.trim());
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    System.err.println(">>>>" + line);
                }
                bufferedReader1.close();

            }
            bufferedReader.close();

        } catch (Exception ex) {
            ex.printStackTrace();
            System.exit(1);
        }
    }
}
