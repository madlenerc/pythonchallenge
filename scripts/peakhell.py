# level 5
import pickle
import urllib.request


body = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
pickled = pickle.loads(body)

for line in pickled:
    print(''.join(elem[0] * elem[1] for elem in line))