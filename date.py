import datetime

now = datetime.datetime.now()

print "Current date and time using str method of datetime object:"
print str(now)

print "Current date and time using instance attributes:"
print "Current year: %d" % now.year
print "Current month: %d" % now.month
print "Current day: %d" % now.day
print "Current hour: %d" % now.hour
print "Current minute: %d" % now.minute
print "Current second: %d" % now.second
print "Current microsecond: %d" % now.microsecond

if now.hour < 10:
	ora = "0" + str(now.hour)
elif now.hour > 10:
	ora = str(now.hour)

if now.minute < 10:
	perc = "0" + str(now.minute)
elif now.minute > 10:
	perc = str(now.minute)

print "Current date and time using strftime:"
print now.strftime("%Y-%m-%d %HH:%MM")

print "Current date and time using isoformat:"
print now.isoformat()

print("kurva program resze lesz egyszer")
print("%s:%s" % (now.hour, now.minute))
#print("%s" % (test2))
#print("%s" % (str(ora)[1]))
#print("%s" % (str(now.minute)[0]))
#print("%s" % (str(now.minute)[1]))
#print("%s" % datetime.datetime)
print("%s" % (ora[0]))
print("%s" % (ora[1]))
print("%s" % (perc[0]))
print("%s" % (perc[1]))
