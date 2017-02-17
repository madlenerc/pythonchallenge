# level 4
import urllib.request

base = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = '8022'
ending = '.php'

while nothing != '':
    response = urllib.request.urlopen('{}{}{}'.format(base, nothing, ending))
    body = response.read().decode('utf-8')
    body = body[body.find('and the next nothing is'):]
    print(body)

    nothing = ''
    for i, c in enumerate(body):
        if(c.isdigit()):
            nothing = body[body.find(c):]
            print(nothing)
            break