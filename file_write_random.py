import random

f = open("My File.txt", "w")

for i in range(100):
    f.write(f"{random.randint(1, 100)}\n")

f.close()

'''
Below random data was written to My File.txt
21
47
53
60
58
48
48
46
93
86
9
44
27
44
38
86
89
93
68
48
81
54
96
89
40
37
22
24
90
23
61
61
28
82
8
96
38
42
17
50
35
16
61
10
26
45
44
61
11
96
93
28
91
87
22
88
10
75
90
76
88
92
15
15
74
16
79
71
96
75
3
32
40
16
60
76
10
44
59
43
21
86
69
65
60
3
71
53
29
5
74
42
31
3
23
43
32
17
32
79
'''
