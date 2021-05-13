mkdir input
cd input
touch input_1.txt input_2.txt input_3.txt input_4.txt
cd ..
hdfs dfs -mkdir assign1/q02
hdfs dfs -mkdir assign1/q02/input
hdfs dfs -copyFromLocal input/* assign1/q02/input
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D mapreduce.jobs.maps=2 -file ./mapper.py -mapper "python ./mapper.py 10000" -file ./reducer.py -reducer ./reducer.py -input /user/maria_dev/assign1/q02/input/ -output assign1/q02/final_output