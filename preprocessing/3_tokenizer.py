# split sentences into tokens
# output : ../corpus/4_tokens/tokens6_18.tsv

from konlpy.tag import Mecab
import csv

tokenizer = Mecab()
age_range = range(6, 19)
out_f = '../corpus/4_tokens/tokens6_18.tsv'
o = open(out_f, 'w', encoding='utf-8', newline="")
wr = csv.writer(o, delimiter='\t')
wr.writerow(['age', 'tokens'])
for age in age_range:
    in_f = '../corpus/3_splitSentence/{}.txt'.format(age)
    i = open(in_f, 'r', encoding='utf-8')
    text = i.readlines()
    for t in text :
        if len(t) > 10: 
            tokenized_sent = tokenizer.pos(t)
            tmp = []
            for word in tokenized_sent:
                tmp.append(word[0])
            tmp = (' '.join(tmp)).strip()
            wr.writerow([age, tmp])