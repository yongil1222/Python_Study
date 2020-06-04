from collections import OrderedDict
from collections import defaultdict


text = """ A check for the biometric authentication capability.
A fallback mechanism that allows a user to authenticate using their device PIN, 
pattern, or password if they cannot authenticate using their biometric input.
A hint that tells the system not to require user confirmation after the user has 
authenticated using an implicit biometric modality. 
For example, you could tell the system that no further confirmation should be 
required after a user has authenticated using face authentication.""".lower().split()

word_count = defaultdict(object)
word_count = defaultdict(lambda:1)

for word in text:
    word_count[word] += 1

print(word_count)

for i, v in OrderedDict(sorted( word_count.items(), 
                                key=lambda t: t[1], 
                                reverse=True)).items():
    print(i,v)

