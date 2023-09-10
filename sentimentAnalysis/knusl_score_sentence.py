# Dictionary-based Sentiment Analysis
# output : ../corpus/4_tokens/tokens6_18_score.tsv
import pandas as pd
import knusl_mecab # KnuSentiLex : https://github.com/park1200656/KnuSentiLex

in_f = '../corpus/4_tokens/tokens6_18_score.tsv'
ksl = knusl_mecab.KnuSL

df = pd.read_csv(in_f, sep='\t')
new_tokens = []
for i in df['selected_tokens']:
    new_i = str(i).split()
    new_tokens.append(new_i)

senti_words = []
senti_score = []

for i in new_tokens:
    result, score = ksl.data_list(i)
    senti_words.append(result)
    senti_score.append(score)

df['senti_words'] = pd.Series(senti_words)
df['senti_score'] = pd.Series(senti_score)
df.to_csv('../corpus/4_tokens/tokens6_18_score.tsv', sep='\t')