## Instructions for running supporting SLA test BenchmarkSQL

​	To support SLA test,  this version has modified the jTPCC code. In this version, every terminal thread could sleep a particular time before every transaction. More specifically, every thread would read a file (whose name equals the terminal thread's name) one line per time as its sleep time, and then execute the transaction.

0. Requirements

- read the original HOW-TO-RUN.txt
- python library argparse is needed.

1. Create the BenchmarkSQL user and a database
2. Compile the BenchmarkSQL source code
3. Create the benchmark configuration file
4. Build the schema and initial database load
5. Generate sleep time data and run the benchmark shell file

```
usage: generatedata.py [-h] [-t TERMINAL] [-max MAX] [-c COUNT]
                       [-d {uniform,normal}] [-m MU] [-s SIGMA] [-b]

generate sleep time data of terminals

optional arguments:
  -h, --help            show this help message and exit
  -t TERMINAL, --terminal TERMINAL
                        terminal nums
  -max MAX, --max-sleep-time MAX
                        max sleep time(ms)
  -c COUNT, --count COUNT
                        the count of random nums(sleep time)
  -d {uniform,normal}, --distribution {uniform,normal}
                        distribution type
  -m MU, --mu MU
  -s SIGMA, --sigma SIGMA
  -b, --backup          back up data

examples:
	./generatedata.py -t 16 		# 16 terminals
	./generatedata.py -c 100 		# per terminal file has 100 line data
	./generatedata.py -max 1000		# max sleep time is 1000 ms
	./generatedata.py -d normal -m 500 -s 10	# normal distribution random data,mu is 500,sigma is 10	
```

generate sleep time data before run the jTPCC program.

```
#runBenchmark.sh
...

cd sleeptime
./generatedata.py -t 16 -c 5000 -max 999999 -d normal -m 5000 -s 10000 -b # for example
cd ..

java -cp "$myCP" $myOPTS jTPCC
```

