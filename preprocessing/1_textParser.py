# Text Parsing 
# output : ../corpus/2_textParsing

import os
import xml.etree.ElementTree as elemTree

age_range = range(6,19)

# function for xml special characters 
def clean(text):
    global new_text
    new_text = text
    if '&name' in new_text:
        new_text = new_text.replace('&name', '길동이')
    new_text = new_text.replace('&', '')
    return new_text

# text parsing
for age in age_range:
    in_f = '../corpus/1_rawDiary/{}'.format(age)
    file_lst = os.listdir(in_f)
    out_f = '../corpus/2_textParsing/{}.txt'.format(age)

    with open(out_f, 'a', encoding='UTF8') as f:
        for file in file_lst:
            filepath = in_f + '/' + file
            # read files
            corpus = open(filepath, 'r', encoding='UTF8')
            global text
            text = corpus.read()
            if '&' in text :
                text = clean(text)

            tree = elemTree.fromstring(text)
            for text in tree.iter('text'):
                for t in text.findall("p"):
                    f.write(t.text + '\n')
            corpus.close()

