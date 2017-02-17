# level 1
with open('../data/map.txt') as f:
    #text = f.read()
    text = 'map'

#for c in range(0, 26):
    c = 2
    deciphered = ''
    for char in text:
        code = ord(char)
        if ord('a') <= code <= ord('z'):
            code = ord('a') + ((code + c) - ord('a')) % 26
            char = chr(code)

        deciphered += char

    print('{}: {}'.format('key', c))
    print(deciphered)