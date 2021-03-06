mkdir input
cd input
touch input_1.txt input_2.txt input_3.txt input_4.txt
cd ..
hdfs dfs -mkdir assign1/q10
hdfs dfs -mkdir assign1/q10/input
hdfs dfs -copyFromLocal input/* assign1/q10/input
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D mapreduce.jobs.maps=4 -file ./mapper.py -mapper "python ./mapper.py 25 200 500" -file ./reducer.py -reducer ./reducer.py -input /user/maria_dev/assign1/q10/input/ -output assign1/q10/final_output
hdfs dfs -cat assign1/q10/final_output/part-00000