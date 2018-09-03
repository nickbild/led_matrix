import re
import sys

red = ""
green = ""
blue = ""

denominator = 256 / 35	# 256 / totalFrames -- scale colors to fit in PWM space.

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

		b = str(int(int(pixel[4:6], 16) / denominator))
		g = str(int(int(pixel[6:8], 16) / denominator))
		r = str(int(int(pixel[8:10], 16) / denominator))

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

