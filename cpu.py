import os
temp = os.popen('cat /sys/class/thermal/thermal_zone0/temp').read()
cel = (int(float(temp)) / 1000.0)
print "%.1f C*" % cel
