This is a turing machine created in python

Here are a couple example inputs to see its functionality

1. 
Enter 5-Tuples. A . by itself to end.
A 0RB 
B 1RA
.
Enter the initial tape and press enter.

Maximum Iterations: 10
{A} 
0{B} 
01{A} 
010{B}
0101{A}
01010{B}
010101{A}
0101010{B}
01010101{A}
010101010{B}
0101010101{A}
Max Iterations Reached
Final State: A


2. 
Enter 5-Tuples. A . by itself to end.
A YRB
.
Enter the initial tape and press enter.

Maximum Iterations: 10
{A} 
Y{B}
HALTED
Final State: B
