d1 = { 'a': 1}
d2 = { 'b': 2}

merged = d1 | d2
print(merged)


'''ou can use multiple context managers in a single with statement more cleanly using the parenthesised context manager

with (
    open(file1.txt as f1)
    open(file2.txt as f2)
    
):
'''