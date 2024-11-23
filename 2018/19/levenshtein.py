from stringdist import levenshtein as ls

s1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. God jul.'
s2 = 'The quick brown fox jumps over the lazy dog. Godt nytt år.'

print(ls(s1, s2))