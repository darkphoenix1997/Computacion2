
# coding: utf-8

# In[ ]:

import re

x = raw_input().strip(); x=s[0].upper()+x[1:]

print len(re.findall('[A-Z][^A-Z]*', x))

