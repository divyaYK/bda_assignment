# python mapper.py <n: fibonacci length> <m: max value> <experiment tries> | sort -n | python reducer.py
python mapper.py 25 200 500 | sort -n | python reducer.py