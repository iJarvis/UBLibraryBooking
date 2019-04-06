import requests
import json
from datetime import datetime, timedelta

def bookRooms():
    fname = "fname"
    lname = "lname"
    date = (datetime.today() + timedelta(days=3)).strftime("%Y-%m-%d")
    print(date)
    #Header
    head = {"Accept" : "application/json, text/javascript, */*; q=0.01",
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin" : "https://booking.lib.buffalo.edu",
            "Referer" : "https://booking.lib.buffalo.edu/reserve/silverman",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "X-Requested-With" : "XMLHttpRequest"
            }

    url = "https://booking.lib.buffalo.edu/ajax/space/book"
    emails = ["cpawa", "krinahit", "vsarvepa", "vineelpa", "freyagen", "apillai"]
    i = 0
    times = [10,12,14,16,18,20,22]
    for email in emails:
        # encoded payload
        if times[i] > 22:
            break
        start = date + " " + str(times[i]) + ":00"
        if times[i]+2 == 24:
            end = date + " 00:00"
        else:
            end = date + " " + str(times[i] + 2) + ":00"
        i = i + 1
        data = "formData%5Bfname%5D="+fname+"&formData%5Blname%5D="+lname+"&formData%5Bemail%5D="+email+"%40buffalo.edu&forcedEmail=&bookings%5B0%5D%5Bid%5D=1&bookings%5B0%5D%5Beid%5D=19763&bookings%5B0%5D%5Bgid%5D=5235&bookings%5B0%5D%5Blid%5D=3154&bookings%5B0%5D%5Bstart%5D="+start+"&bookings%5B0%5D%5Bend%5D="+end+"&returnUrl=%2Freserve%2Fsilverman"
        response = requests.post(url,data=data,headers = head)
        response_json = response.json()
        print(response_json)

    # Json format if something goes wrong
    # payload = {"formData" : {"fname" : "syed",
    #                         "lname" : "ahmed",
    #                         "email" : "abcd@buffalo.edu"},
    #             "forcedEmail" : "",
    #             "bookings" : [{"id" : 1,
    #                         "eid" : 19762,
    #                         "gid" : 5235,
    #                         "lid" : 3154,
    #                         "start" : "2019-04-05 02:00",
    #                         "end" : "2019-04-05 04:00"}],
    #             "returnUrl" : "/reserve/silverman"
    #         }