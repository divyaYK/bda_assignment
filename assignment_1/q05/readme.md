# Assignment question allotted: Q.5

#### Problem Statement
-  Compute golden ratio. Golden ratio can be <br>
recursively computed as<br>
&nbsp;  => xn = 1 + 1/xn-1<br>
  – i/p 1: number of mapped instances<br>
  – i/p 2: number of computation steps<br>
  – i/p 3: a number N < 10. The initial estimate of x0 to<br>
  be taken as a random number between 1 and N.<br>
  – o/p: average of all combined outputs

#### Steps to run:

Locally:
```bash
python mapper.py <Number_of_computation_steps> | python sort.py | python reducer.py
```
