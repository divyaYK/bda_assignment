python generate_input.txt 10000
cat input.txt | python mapper.py > mapperOutput.txt
cat mapperOutput.txt | sort -n > sortOutput.txt
cat sortOutput.txt | python reducer.py > reducerOutput.txt