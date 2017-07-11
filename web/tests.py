from django.test import TestCase

# Create your tests here.

a= '12345'
a = list(a)
for i in range(len(a)//2):
    if i != len(a)-i-1:
        a[i],a[len(a)-i-1] = a[len(a)-i-1],a[i]
print(''.join(a))