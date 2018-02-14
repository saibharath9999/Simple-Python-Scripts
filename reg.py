import re

string="sai.@gmail.com ss@.com @d.com"

c=len(re.findall("[\w.]{1,10}@[\w]{1,15}.[\w]{2,3}",string))
print (c)