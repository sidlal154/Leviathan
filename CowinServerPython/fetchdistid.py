import utils
import time
import sys

#safe when APIs dont work
if __name__=="__main__":
    start = time.time()
    print("district ID: "+str(utils.getDistIDfromName(str(sys.argv[1]),sys.argv[2])))
    end = time.time()
    print(f"Runtime of the program is {end - start}")