# level 12
f = open('../data/evil2.gfx', 'rb').read()

endings = ['.jpg', '.png', '.gif', '.png', '.jpg']
for i in range(0, 5):
    open('../data/image' + str(i) + endings[i], 'wb').write(f[i::5])