python mapper.py 1000000 > mapperOutput.txt
cat mapperOutput | sort -n > sortOutput.txt
cat sortOutput.txt | python reducer.py > reducerOutput.txt