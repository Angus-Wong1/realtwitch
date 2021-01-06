import random
def shuffle():
    with open('trackingId.csv','r+') as f:
        sluglist = f.read().split(',')
        random.shuffle(sluglist)
        f.seek(0)
        slugString = ''
        for i in sluglist:
            slugString+= i+','
        f.seek(0)
        f.write(slugString)
        f.truncate()
