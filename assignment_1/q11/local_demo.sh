python generate_input.py 2000000 2000000 input.txt
cat input.txt | python mapper.py | sort -n | python reducer.py