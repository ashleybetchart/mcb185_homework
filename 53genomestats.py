# 53 Genome stats by Ashley Betchart
# Co-authors: Ashley, Aman

import gzip
import sys
import math

path = sys.argv[1]
feature = sys.argv[2]

with gzip.open(path, 'rt') as data:
	length = []
	for line in data:
		words = line.split()
		if words[2] != feature: continue
		length.append(int(words[4]) - int(words[3]) + 1)

total_len = 0
for n in length:
	total_len += n

length.sort()
count = len(length)
min = length[0]
max = length[-1]
mean = total_len / count
if len(length) % 2 == 0:
	med1 = length[len(length) // 2]
	med2 = length[len(length) // 2 - 1]
	med = (med1 + med2) / 2
else: med = length[len(length) // 2]

sd = 0
for n in length:
	sd += ((mean - n)**2 / count)
sd =  math.sqrt(sd)

print(count, min, max, int(mean), int(sd), int(med))