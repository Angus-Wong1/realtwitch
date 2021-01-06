def remove():
    print('removing...')
    x = open('top100slugs.txt','r+')
    up = open('uploaded.txt','r')
    uplist = up.read().split(',')
    f = x.read().split(',')
    for up in uplist:
        for slug in f:
            try:
                index = slug.index('clip/')+5
                if up == slug[index:]:
                    f.remove(slug)

            except:
                continue
    p = ''
    for i in f:
        p += i+','
    x.truncate(0)
    x.write(p)
    x.close()
    print('done removing')
remove()
