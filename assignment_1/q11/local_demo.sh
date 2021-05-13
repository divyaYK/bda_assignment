python generate_input.py 2000000
cat input.txt | python mapper.py | sort -n | python reducer.py