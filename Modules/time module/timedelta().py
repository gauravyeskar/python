#from datetime import datetime,date
# print(datetime.datetime.today().date())
# print(datetime.datetime.today().time())


#3. दो तारीख़ों के बीच का अंतर यूज़र से दो डेट्स इनपुट लें (जैसे 2024-10-04 और 2025-02-20)
#   दोनों के बीच कितने दिन हैं, यह बताएँ।
# dte1 = input("Enter date 1:- ")
# getd1 = datetime.strptime(dte1,"%Y-%m-%d")
# dte2 = input("Enter date 2:- ")
# getd2 = datetime.strptime(dte2,"%Y-%m-%d")
# diff = getd2 - getd1
# print(diff)

# #4. भविष्य या पिछली तारीख यूज़र एक डेट इनपुट करे। उस डेट से 100 दिन आगे और 100 दिन पीछे की डेट दिखाएँ।
#from datetime import timedelta,datetime
# date1 = input("Enter any one date:- ")
# getdate1 = datetime.strptime(date1,"%Y-%m-%d")
# aheadate =getdate1 + timedelta(days = 100)
# backdate = getdate1 - timedelta(days = 100)

# print("100 Days ahead: ", aheadate.strftime("%Y-%m-%d"))
# print("100 Days Before :", backdate.strftime("%Y-%m-%d"))

#5. सिर्फ समय का फ़र्क निकालना दो टाइम इनपुट (जैसे 12:30:00 और 15:45:00) लेकर
#   उनके बीच कितने घंटे और मिनट का अंतर है, यह निकालिए।
# from datetime import datetime
# tm1 = input("Enter time 1:- ")
# tm2 = input("Enter time 2:- ")
# tm_frmt = "%H:%M:%S"
# t1 = datetime.strptime(tm1,tm_frmt)
# t2 = datetime.strptime(tm2,tm_frmt)

# diff = t2-t1 if t2>t1 else t1-t2
# print(diff)

# 6. किस दिन क्या आएगा यूज़र से एक डेट इनपुट लें। प्रोग्राम बताए कि वह डेट कौनसे दिन (Monday, Tuesday…) को पड़ेगा।
# from datetime import datetime
# dat = input("Enter the date (DD-MM-YYYY):- ")
# getdate = datetime.strptime(dat,"%d-%m-%Y")
# day_nm = getdate.str
# print(day_nm)

#7. पूरे महीने का कैलेंडर यूज़र से महीना और साल इनपुट लें (जैसे 10 2025)। Python calendar मॉड्यूल से उस महीने का कैलेंडर प्रिंट करें।
# import calendar
# from datetime import datetime
# dat = input("Enter the date (MM-YYYY):- ")
# getdate = datetime.strptime(dat,"%m-%Y")
# month = getdate.month
# yr  = getdate.year
# calendr = calendar.month(yr,month)
# print(calendr)

#8. वर्किंग डेज़ काउंट यूज़र एक महीने का नाम और साल दे। प्रोग्राम बताए उस महीने में कितने वीकेंड और वर्किंग डेज़ हैं।
# from datetime import datetime
# import calendar
# dat = input("Enter the date (MM-YYYY):- ")
# getdate = datetime.strptime(dat,"%m-%Y")
# month = getdate.month
# yr = getdate.year
# month_days = calendar.monthcalendar(yr,month)
# work_days = 0
# weekend = 0
# for week in month_days:
#     for i,day in enumerate(week):
#         if day!=0:
#             if i<5:
#                 work_days +=1
#             else:
#                 weekend +=1 
# print(f"{calendar.month_name[month]} {yr}")
# print("Working days:- ",work_days)
# print("Weekends :- ",weekend)


# # Q. Har sal mein kitne weekends hote hai.
from datetime import datetime
import calendar
yr = input("Enter the year(YYYY):- ")
getyr = datetime.strptime(yr,"%Y")
year = getyr.year
weekends = 0
for month in range(1,13):
    month_days = calendar.monthcalendar(year,month)

    for weeks in month_days:
        for i,day in enumerate(weeks):
            if day != 0 and i >=5 :
                weekends += 1
if calendar.isleap(int(yr)):
    tot_days = 366
else:
    tot_days = 365
tot_work_days = tot_days - weekends
print("Total Days:- ",tot_days)
print("Total Working Days:- ",tot_work_days)
print("Total Weekends are :- ", weekends)

#9. कस्टम रिमाइंडर एक डेट और टाइम इनपुट लें। अगर वह डेट/टाइम current datetime से कम है तो “Expired” दिखाएँ,
#   वरना “Upcoming” दिखाएँ।
# from datetime import datetime,date
# dat = input("Enter the Date and time (DD-MM-YYYY--HH:MM:SS ):- ")
# getdate = datetime.strptime(dat,"%d-%m-%Y--%H:%M:%S")
# currdatetime = datetime.today()
# msg = 'Expired' if getdate < currdatetime else 'Upcoming'
# print(msg)

# 10. रैंडम डेट जेनरेट करना किसी रेंज (जैसे 1 Jan 2020 से 31 Dec 2023) के बीच एक रैंडम डेट जेनरेट करें।
# from datetime import datetime,timedelta
# import random

# dat1 = input("Enter the date1 (DD-MM-YYYY) :- ")
# getdat1 = datetime.strptime(dat1,"%d-%m-%Y")
# dat2 = input("Enter the date2 (DD-MM-YYYY):- ")
# getdat2 = datetime.strptime(dat2,"%d-%m-%Y")

# mindate = min(getdat1,getdat2)
# maxdate = max(getdat1,getdat2)
# diff = (maxdate - mindate).days
# rand_days = random.randint(0,diff)
# rand_date = getdat1 + timedelta(days=rand_days)

# print("Random Date:- ",rand_date.strftime("%d-%m-%Y"))
