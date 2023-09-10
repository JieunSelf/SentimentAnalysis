# Extract only the tokens for Sentiment Analysis
# output : ../corpus/4_tokens/tokens6_18_selected_tokens.tsv

from konlpy.tag import Mecab
import pandas as pd

tokenizer = Mecab()
in_f = '../corpus/4_tokens/tokens6_18.tsv'

# function for extracting only the tokens for Sentiment Analysis
def mecab_select_tokens(tokens):
    selected = []
    for j in tokenizer.pos(tokens):
        if j[1][0] in ['N', 'V', 'M', 'X']:
            selected.append(j[0])
    return (' '.join(selected)).strip()

df = pd.read_csv(in_f, sep='\t')
selected_tokens = []
for i in df['tokens']:
    selected_tokens.append(mecab_select_tokens(i))
df['selected_tokens'] = selected_tokens
df.to_csv('../corpus/4_tokens/tokens6_18_selected_tokens.tsv', sep='\t')