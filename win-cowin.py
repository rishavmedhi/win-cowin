import requests
import json
import os
import sched, time, datetime, pytz

s = sched.scheduler(time.time, time.sleep)
districtIds = [265, 294]

IST = pytz.timezone('Asia/Kolkata')

def requestUtil(url):
  # print(url)
  headers = {"User-Agent":"PostmanRuntime/7.26.10"}
  response =  requests.get(url, headers=headers);
  if response.status_code == 200:
    jsonResponse = response.json()
    centerSlotFinder(jsonResponse)
  else:
    print("API FAILED :: status"+str(response.status_code));

def centerSlotFinder(apiResponse):
  centersList = apiResponse['centers']
  if len(centersList)>0:
    for center in centersList:
      centerSessions = center['sessions']
      if len(center['sessions'])>0:
        for session in centerSessions:
          if session['available_capacity']>0 and session['min_age_limit']==18:
            ## alert here that slots are available
            os.system('say "Slots found"')
            print("SLOTS FOUND::GO AND BOOK NOW "+datetime.datetime.now(IST).strftime("%d-%m-%Y %H:%M:%S"))
    else:
      print("No slots for this district "+datetime.datetime.now(IST).strftime("%d-%m-%Y %H:%M:%S"))
  else:
      print("No centers present for this location "+datetime.datetime.now(IST).strftime("%d-%m-%Y %H:%M:%S"))

def generateURL(districtId, dateString):
  return "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id="+str(districtId)+"&date="+dateString

def main(sc):
  formatTime = datetime.datetime.now(IST).strftime("%d-%m-%Y")
  for dId in districtIds:
    requestUtil(generateURL(dId, formatTime))
  s.enter(60,1, main, (sc,))

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

s.enter(60,1, main, (s,))
s.run()