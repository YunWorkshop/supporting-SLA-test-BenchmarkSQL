#! /usr/bin/python
import argparse
import os
import random
import time

# arg validation
def positive_int(val):
	try:
		ival = int(val)
	except ValueError:
		raise argparse.ArgumentTypeError("must be an integer")

	if ival <= 0:
		raise argparse.ArgumentTypeError("must be positive")
	return ival

examples='''examples:
	./generatedata.py -t 16 		# 16 terminals
	./generatedata.py -c 100 		# per terminal file has 100 line data
	./generatedata.py -max 1000		# max sleep time is 1000 ms
	./generatedata.py -d normal -m 500 -s 10	# normal distribution random data,mu is 500,sigma is 10	
'''
parser = argparse.ArgumentParser(
    description="generate sleep time data of terminals",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=examples)
parser.add_argument("-t","--terminal",help="terminal nums",type=positive_int,dest="terminal")
parser.add_argument("-max","--max-sleep-time",help="max sleep time(ms)",dest="max",type=positive_int,default=10000)
parser.add_argument("-c","--count",type=positive_int,help="the count of random nums(sleep time)",dest="count",default=10000)
parser.add_argument("-d","--distribution",choices=["uniform","normal"],default="uniform",dest="distribution",help="distribution type")
parser.add_argument("-m","--mu",type=positive_int,default=1000,dest="mu")
parser.add_argument("-s","--sigma",default=100,type=float,dest="sigma")
parser.add_argument("-b","--backup",action="store_true",help="back up data")

args = parser.parse_args()
terminal_num=args.terminal
if(terminal_num <10):
	for i in range(1,terminal_num+1):
		os.system("touch "+"Term-0"+str(i))
else:
	for i in range(1,10):
		os.system("touch "+"Term-0"+str(i))
	for i in range(10,terminal_num+1):
		os.system("touch "+"Term-"+str(i))
print("make "+str(terminal_num)+" terminal files.")

MAX_SLEEP_TIME=args.max
count=args.count
distribution_type=args.distribution

def generate_uniform(index):
	filename=""
	if index<10:
		filename="Term-0"+str(index)
	else:
		filename="Term-"+str(index)
	f=open(filename,"w")
	for i in range(count):
		f.write(str(random.randint(0,MAX_SLEEP_TIME))+"\n")
	f.close()

def generate_normal(index):
	mu=args.mu
	sigma=args.sigma
	filename=""
	if index<10:
		filename="Term-0"+str(index)
	else:
		filename="Term-"+str(index)
	f=open(filename,"w")
	for i in range(count):
		f.write(str(min(max(int(random.gauss(mu,sigma)+0.5),0),MAX_SLEEP_TIME))+"\n")
	f.close()

if distribution_type=="uniform":
	for i in range(1,terminal_num+1):
		generate_uniform(i)
elif distribution_type=="normal":
	for i in range(1,terminal_num+1):
		generate_normal(i)
print("generate "+str(count)+" random sleemtime per terminal.")

if args.backup:
	backup_dir=time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
	os.system("mkdir "+backup_dir)
	os.system("cp Term-* ./"+backup_dir)
	print("backup data to dir: "+backup_dir)