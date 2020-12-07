#!/usr/bin/python3

from subprocess import Popen, PIPE
import sys
import json

result = {}
result['ftpclients'] = {}
result['ftpclients']['hosts'] = []
result['ftpclients']['vars'] = {}

pipe = Popen(['getent', 'hosts'], stdout=PIPE, universal_newlines=True)

for line in pipe.stdout.readlines():
	s = line.split()
	if s[1].startswith('servera'):
		result['ftpclients']['hosts'].append(s[1])

if len(sys.argv) == 2 and sys.argv[1] == '--list':
	print(json.dump(result))
elif len(sys.argv) == 3 and sys.argv[1] == '--host':
	print(json.dump({}))
else:
	print('Requires an argument, please use --list ot --host <host>')