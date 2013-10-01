import os
import numpy as np
#files = os.listdir(r"C:\spam")
files = os.listdir(r"C:\easy_ham")

with open("dataSpam.out","w") as out:

    n = 0
    for fname in files:
        with open("C:\\easy_ham\\" + fname) as f:
      
            data = f.readlines()
                    
            for line in  data:
                if line.startswith("Subject:"):
                    print(line)
                    n +=1
                    print(n)
                    out.write("{0}, nospam \n".format(line[8:-1]))
            print(fname)
