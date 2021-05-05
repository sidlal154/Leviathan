import requests
import json
import getopt
import sys

#returns prettyjson
def apicall(url,querystring):
    #print(querystring)
    #querystring = {}
    #print(url)
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        'cache-control': "no-cache",
        'postman-token': "61ed487f-17a9-5010-288b-598fc5386ea1"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.status_code)
    #print(response.text)
    if response.text in ("Unauthenticated access!","Internal server error!"):
        print(response.text)
        return "Error"
    return json.loads(response.text)

#dump important info
def appendDeets(availableList,center_dict,sessions):
    deet = {}
    deet["center_id"] = center_dict["center_id"]
    deet["name"] = center_dict["name"]
    deet["address"] = center_dict["address"]
    deet["available_sessions"] = sessions
    availableList.append(deet)
    return availableList

#get district id from district name
def getDistIDfromName(distname,state):
    state_url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
    resp = apicall(state_url,{})
    if resp == "Error":
        return "Error"
    stateid = list(filter(lambda d: d["state_name"] == state, resp["states"]))[0]["state_id"]
    dist_url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/" + str(stateid)
    nresp = apicall(dist_url,{})
    if nresp == "Error":
        return "Error"
    distid = list(filter(lambda d: d["district_name"] == distname, nresp["districts"]))[0]["district_id"]
    return distid


#get available centers for a district for 7 days, for age group and above certain capacity
def getAvailableCenters(distid,d1,age,cap):
    available_centers = []
    querystring = {}
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
    querystring["district_id"] = str(distid)
    querystring["date"] = str(d1)
    #print(url)
    resp = apicall(url,querystring)
    if resp == "Error":
        return "Error"
    for c in resp["centers"]:
        available_sessions = []
        for s in c["sessions"]:
            if s["available_capacity"] >= cap and s["min_age_limit"]==age:
                available_sessions.append(s)
        if len(available_sessions)>0:
            available_centers = appendDeets(available_centers,c,available_sessions)

    return available_centers

#helper function to get arguments as flags
def main_arguments(argv):
   distid = ""
   distname = "BBMP"
   state = "Karnataka"
   age = "18"
   cap = "1"
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["distid=","distname=","state=","age=","cap="])
   except getopt.GetoptError:
      print("Incorrect Usage, please try following 2 templates:")
      print(">> python main.py --distid <district-id from getchdistid.py> --age <minimum age> --cap <minimum capacity of available slots>")
      print(">> python main.py --distname <Name of your district> --state <Name of your state> --age <minimum age> --cap <minimum capacity of available slots>")
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-h","--help"):
         print("[Help] Following 2 templates:")
         print(">> python main.py --distid <district-id from getchdistid.py> --age <minimum age> --cap <minimum capacity of available slots>")
         print(">> python main.py --distname <Name of your district> --state <Name of your state> --age <minimum age> --cap <minimum capacity of available slots>")
         sys.exit()
      elif opt == "--distid":
         distid = arg
      elif opt == "--distname":
         distname = arg
      elif opt == "--state":
         state = arg
      elif opt == "--age":
         age = arg
      elif opt == "--cap":
         cap = arg
   return distid,distname,state,age,cap