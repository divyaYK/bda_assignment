# Assignment question allotted: Q.5

#### Problem Statement
-  Compute golden ratio. Golden ratio can be <br>
recursively computed as<br>
&nbsp;  => xn = 1 + 1/xn-1<br>
  – i/p 1: number of mapped instances<br>
  – i/p 2: number of computation steps<br>
  – i/p 3: a number N < 10. The initial estimate of x0 to<br>
  be taken as a random number between 1 and N.<br>
  – o/p: average of all combined outputs

#### Steps to run:

Locally:
```bash
$ python mapper.py <Number_of_computation_steps> | python sort.py | python reducer.py
```
<br>
HDFS:
```bash
$ cd /path/to/directory/where/python/files/exist
$ hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
  -D mapreduce.jobs.maps=2 \
  -file ./mapper.py \
  -mapper "python ./mapper.py 500" \
  -file ./reducer.py \
  -reducer ./reducer.py \
  -input /path/to/hdfs/directory/input/ \
  -output /path/to/hdfs/directory/final_output
# To view output
$ hdfs dfs -cat /path/to/hdfs/directory/final_output/part-00000
```
