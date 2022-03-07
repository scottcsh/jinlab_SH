#!/usr/bin/python
import re

real_line = []

in_dir = raw_input("Input *.star file dir : ")

out_dir = raw_input("Output *.star file dir : ")

with open(in_dir, 'r') as f:

    for line in f:

	#real_name = line.split(' ')[0].split('/')[2][22:]

	p = re.compile('[0-9]{21}[_]')

	res=re.sub('[0-9]{21}[_]', '',line)

	real_line.append(res)	

with open(out_dir,'w') as f:

    for line in real_line:

	f.write(line)

