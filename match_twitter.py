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

entities2rel = {}
for line in open('freebase_data'):
    (event, a1, a2, date) = eval(line.strip())
    try:
        entities2rel[(a1, a2)] = entities2rel.get((a1, a2), []) + [{'type':event, 'date':datetime.datetime.strptime(date, '%Y-%m-%d')}]
    except:
        pass

prev_id = None
for line in F_IN:
    fields = line.strip().split('\t')
    if len(fields) != 11:
        continue
    (sid, uid, loc, created_at, date, entity, eType, words, pos, neTags, eventTags) = fields

    if sid == prev_id:
        continue
    prev_id = sid

    entities = GetSegments(words.split(' '), neTags.split(' '), 'ENTITY')

    tweetDate = None
    try:
        tweetDate = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
    except Exception as e:
        tweetDate = datetime.datetime.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y')

    words_list = words.lower().split(' ')

    for e1 in entities:
        for e2 in entities:
            if entities2rel.has_key((e1.lower(), e2.lower())):
                for rel in entities2rel[(e1.lower(), e2.lower())]:
                    print (rel['type'], e1, e2, words)
