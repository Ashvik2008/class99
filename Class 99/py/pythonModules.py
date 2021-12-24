import platform
#x=platform.system()
#print(x)

#list all the defined names belonging to the platform module
import platform
x=dir(platform)
print(x)

import mymodule
mymodule.greeting(" Ashvik")


a = mymodule.person1["age"]
print(a)

#prints name stored in mymodle.py
from mymodule import person1
print(person1["name"])

#datetime module in python
import datetime
x=datetime.datetime.now()
print(x)

#the date contains year,month,day,hour,minute,second and microsecond

#returns the year and name of weekday
print(x.year)

#Weekday
print(x.strftime("%A"))

#month 
print(x.strftime("%B"))

#day of the month
print(x.strftime("%A"))

#year 
print(x.strftime("%Y"))