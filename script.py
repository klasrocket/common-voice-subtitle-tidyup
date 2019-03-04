#script to tidy up swe subutitles for using with mozilla common voice project
#
#

import re
result = ""
with open("file.txt","r") as f:
    for i in f.readlines():
        if re.match('^[0-9]+',i) or re.match(r'^\s*$', i):
            i=i
        else:
            result = result + i
            #print(i)

    result = result.replace('-','')
    result = result.replace('<i>', '')
    result = result.replace('</i>', '')
    result = result.replace('\n', ' ')
    result = result.replace('.', '.\n')

    result = result.replace('?', '?\n')

    result = result.replace('!', '!\n')
    result = result.replace('\n.', '')
    result = result.replace('\n ', '\n')
    result = result.replace('nåt', 'något')
    result = result.replace('nån', 'någon')

    result=result.splitlines()
    y=len(result)
    new_result = ''
    for x in range(y):

        if len(result[x].split()) >2 and len(result[x].split()) <14:
            new_result = new_result + result[x] + '\n'
        #print(result[x])
    print(new_result)

