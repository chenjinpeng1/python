from django.test import TestCase

# Create your tests here.
def test(**kwargs):
    print(kwargs)
a={"1":1,"2":2}
test(**a)