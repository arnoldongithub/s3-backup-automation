import re

s="GeeksforGeeks: A computer science portal for hunks"

match=re.search(r'portal',s)

print('Start Index:',match.start())
print('End Index:',match.end())
