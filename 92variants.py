# 92 variants by Ashley Betchart
# Co-authors: Ashley, Aman

import argparse
import gzip


parser = argparse.ArgumentParser(description='variant reporter')
parser.add_argument('gff', type=str, help='GFF file')
parser.add_argument('vcf', type=str, help='VCF file')
arg = parser.parse_args()

with gzip.open(arg.vcf, 'rt') as diff:
	change = []
	for i in diff:
		info = i.split()
		change.append({'chr':info[0], 'place':int(info[1]), 'type':[]})

with gzip.open(arg.gff, 'rt') as locate:
	for i in locate:
		data = i.split()
		data[3] = int(data[3])
		data[4] = int(data[4])
		for point in change:
			if point['chr'] == data[0] and point['place'] > data[3] and point['place'] < data[4]:
				if data[2] not in point['type']: point['type'].append(data[2])
for i in change:
	if len(i['type']) > 0: print(f'{i["chr"]}\t{i["place"]}\t{", ".join(i["type"])}')