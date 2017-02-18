import zipfile

nothing = '90052'
ending = '.txt'
comments = ''

with zipfile.ZipFile('../data/channel.zip', 'r') as myzip:
    while nothing != '':
        text = myzip.open('{}{}'.format(nothing, ending)).read().decode('utf-8')
        info = myzip.getinfo('{}{}'.format(nothing, ending))
        print(text)
        text = text[text.find('Next nothing is'):]

        nothing = ''
        for i, c in enumerate(text):
            if c.isdigit():
                nothing = text[i:]
                break

        comments += info.comment.decode('utf-8')

print(comments)