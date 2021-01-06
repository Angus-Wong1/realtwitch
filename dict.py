
# calls twitch api gets info
import pickle
import requests

d = {}

def merge_dicts(*dicts):
    for dict in dicts:
        for key in dict:
            try:
                d[key].append(dict[key])
            except KeyError:
                d[key] = [dict[key]]



def twitchParser(f):
    '''takes file of urls from twitch
    return a list of slugs'''
    count = 0
    sluglist = []
    txt = open(f,'r')
    fullList= txt.read().split(',')

    for i in fullList:
        clipint = (i.find('/clip/'))
        sluglist.append(i[clipint+6:])
        count += 1
    print(count)
    txt.close()
    return sluglist

def twithdict(sluglist):
    #takes a list from twitchParser
    #uses twitch api to get infomation

    for i in sluglist:
        url = 'https://api.twitch.tv/kraken/clips/'+i
        headers= {'Accept': 'application/vnd.twitchtv.v5+json','Client-ID': '6bomnyc6d220m1lmdt6s1ole06t65f'}
        r = requests.get(url,headers=headers)
        merge_dicts(r.json())
twithdict(twitchParser('top100slugs.txt'))
with open('twitchdict.pickle','wb') as w:
    pickle.dump(d,w,pickle.HIGHEST_PROTOCOL)

with open('trackingId.csv','w') as t:
    track = ['https://clips-media-assets2.twitch.tv/AT-cm%7C'+i+'.mp4' for i in d['tracking_id']]
    for i in track:
        t.write(i +',')
