import requests
from datetime import datetime, timedelta
def bookRoom():
    email = ["ektakati","hparthas","syedaqhi","arunsure","aaa'"]
    time1 = ["10","12","14","16","18"]
    time2 = ["12","14","16","18","20"]

    todayDate = datetime.now()
    dayAftrTmrw = todayDate + timedelta(days=3)
    dayAftrTmrw = dayAftrTmrw.strftime("%Y-%m-%d")
    print(dayAftrTmrw)

    for idx, val in enumerate(email):
        url = "https://booking.lib.buffalo.edu/ajax/space/book?formData%5Bfname%5D=firstname&formData%5Blname%5D=lastname&formData%5Bemail%5D="+email[idx]+"%40buffalo.edu&forcedEmail=&bookings%5B0%5D%5Bid%5D=4&bookings%5B0%5D%5Beid%5D=19762&bookings%5B0%5D%5Bgid%5D=5235&bookings%5B0%5D%5Blid%5D=3154&bookings%5B0%5D%5Bstart%5D="+dayAftrTmrw+"+"+time1[idx]+"%3A00&bookings%5B0%5D%5Bend%5D="+dayAftrTmrw+"+"+time2[idx]+"%3A00&returnUrl=%2Freserve%2Fsilverman"

        payload = { }
        headers = {
        'Referer': "https://booking.lib.buffalo.edu/reserve/silverman"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)
