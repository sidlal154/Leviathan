import utils
import yaml
import time
import sys
from datetime import date
from win10toast import ToastNotifier

#TODO: Add erronous inputs
#TODO: add for all ages option
#TODO: make compatible for other OS
if __name__=="__main__":
    
    start= time.time()
    today = date.today()
    d1 = today.strftime("%d-%m-%Y")
    #print(str(d1))
    distid,distname,state,age,cap = utils.main_arguments(sys.argv[1:])

    if distid == "":
        distid = utils.getDistIDfromName(distname,state)
    if distid == "Error":
        print("Server error, try after few minutes")
        sys.exit()
    print("District ID<save for future>: "+str(distid))

    available_centers = []
    while True:
        available_centers = utils.getAvailableCenters(distid,d1,int(age),int(cap))
        if available_centers == "Error":
            print("Error from server, retrying...")
            time.sleep(5)
            continue
        if len(available_centers)>0:
            break
        print("Sorry, no slots available")
        time.sleep(5)
    
    #available_centers = utils.getAvailableCenters(distid,d1,int(age))
    end = time.time()
    print(f"Runtime of the program is {end - start}")
    file = open("available-centers.yaml", "w")
    file.write("Available Centers:\n\n")
    i = 0
    for a in available_centers:
        i=i+1
        file.write("Center Slno:"+str(i)+"\n")
        yaml.dump(a,file, allow_unicode=True, default_flow_style=False)
        file.write("-------------------------------------------------------------------------------\n")
        file.write("\n\n")
    file.write("----------------------------------------END--------------------------------------")
    file.close()
    n = ToastNotifier()
    n.show_toast("Vaccine-Mitra", "Vaccination slots available in "+str(i)+" centers", duration = 2)
    
    
