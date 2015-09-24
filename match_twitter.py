import sys
import gzip
import datetime
import json

F_IN = gzip.open(sys.argv[1])

def GetSegments(words, annotations, tag, lower=True, getIndices=False):
    results = []

    annotations = [x.split(":")[0] for x in annotations]

    start = None
    for i in range(len(words)):
        if annotations[i].split(':')[0] == 'B-%s' % tag:
            if start != None:
                if getIndices:
                    results.append((' '.join(words[start:i]), (start,i)))
                else:
                    results.append(' '.join(words[start:i]))
            start = i
        elif annotations[i] == 'O' and start != None:
            if getIndices:
                results.append((' '.join(words[start:i]), (start,i)))
            else:
                results.append(' '.join(words[start:i]))
            start = None
    if start != None:
        if getIndices:
            results.append((' '.join(words[start:]), (start,i)))
        else:
            results.append(' '.join(words[start:]))

    if lower:
        if getIndices:
            results = [(x[0].lower(),x[1]) for x in results]
        else:
            results = [x.lower() for x in results]            
    return results

entities2event = {}
for line in open('freebase_data'):
    (event, a1, a2, date) = eval(line.strip())
    try:
        entities2event[(a1, a2)] = entities2event.get((a1, a2), []) + [{'type':event, 'date':datetime.datetime.strptime(date, '%Y-%m-%d')}]
    except:
        pass

for line in F_IN:
    fields = line.strip().split('\t')
    if len(fields) != 11:
        continue
    (sid, uid, loc, created_at, date, entity, eType, words, pos, neTags, eventTags) = fields

    entities = GetSegments(words.split(' '), neTags.split(' '), 'ENTITY')

    tweetDate = None
    try:
        tweetDate = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
    except Exception as e:
        tweetDate = datetime.datetime.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y')

    words_list = words.lower().split(' ')

    for e1 in entities:
        for e2 in entities:
            if entities2event.has_key((e1.lower(), e2.lower())):
                for event in entities2event[(e1.lower(), e2.lower())]:
                    if abs((tweetDate - event['date']).days) < 10:
                        print json.dumps({'sid':sid, 'entity':entity, 'created_at':created_at, 'words':words, 'pos':pos, 'neTags':neTags})
                        print event
                        print tweetDate - event['date']
