mkdir input
cd input
touch input_1.txt input_2.txt input_3.txt input_4.txt input_5.txt input_6.txt
cd ..
hdfs dfs -mkdir assign1/q11
hdfs dfs -mkdir assign1/q11/input
hdfs dfs -copyFromLocal input/* assign1/q11/input
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D mapreduce.jobs.maps=4 -file ./mapper.py -mapper "python ./mapper.py ./input.txt" -file ./reducer.py -reducer ./reducer.py -input /user/maria_dev/assign1/q11/input/ -output assign1/q11/final_output
hdfs dfs -cat assign1/q11/final_output/part-00000