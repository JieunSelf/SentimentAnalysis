# split text into sentences
# output : ../corpus/3_splitSentence
# pip install kss

import kss

age_range = range(6,19)
for age in age_range:

    text_file = '../corpus/2_textParsing/{}.txt'.format(age)
    out_file = '../corpus/3_splitSentence/{}.txt'.format(age)

    with open(text_file, 'r', encoding='UTF8') as f:
        text = f.readlines()
        with open(out_file, 'a', encoding='UTF8') as new_f:
                for t in text :
                    for sent in kss.split_sentences(t):
                        new_f.write(sent + '\n')
    print('{} complete'.format(age))

'''
# additional work 
for age in age_range:
    file = '../corpus/3_splitSentence/{}.txt'.format(age)

    with open(file, 'r', encoding='UTF8') as f:
        text = f.readlines()
        for t in text : 
            if len(t) > 150:
                print(t)
                raise ValueError('Too Long')
    print('{} complete'.format(age))
'''
