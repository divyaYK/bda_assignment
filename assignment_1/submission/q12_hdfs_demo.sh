mkdir input
cd input
for n in 1 2 3 4 5 6 7 8 9 10
do
    python "../generate_input.py" 200000 2000000 "input_$n.txt"
done
cd ..
hdfs dfs -mkdir assign1/q12
hdfs dfs -mkdir assign1/q12/input
hdfs dfs -copyFromLocal input/* assign1/q12/input
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D mapreduce.jobs.maps=4 -file ./mapper.py -mapper "python ./mapper.py" -file ./reducer.py -reducer ./reducer.py -input /user/maria_dev/assign1/q12/input/ -output assign1/q12/final_output
hdfs dfs -cat assign1/q12/final_output/part-00000