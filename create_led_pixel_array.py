import re
import sys

red = ""
green = ""
blue = ""

for line in open(sys.argv[1]):
	if not re.match("^0x", line):
		continue

	line = line.strip()
	line = line.replace(" ", "")
	lineAry = line.split(",")

	red += "{"
	green += "{"
	blue += "{"

	cnt = 1
	for pixel in lineAry:
		if pixel == "":
			continue

		b = str(int(int(pixel[4:6], 16) / 10.2))
		g = str(int(int(pixel[6:8], 16) / 10.2))
		r = str(int(int(pixel[8:10], 16) / 10.2))

		red += r
		green += g
		blue += b

		if cnt < 32:
			red += ","
	                green += ","
        	        blue += ","


		cnt += 1


	red += "},\n"
        green += "},\n"
        blue += "},\n"

print red
print "----"
print green
print "----"
print blue

