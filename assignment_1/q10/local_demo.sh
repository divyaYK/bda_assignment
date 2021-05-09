python mapper.py 25 200 500 > mapperOutput.txt
cat mapperOutput | sort -n > sortOutput.txt
cat sortOutput.txt | python reducer.py > reducerOutput.txt