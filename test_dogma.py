import dogma

s = "ACGTGGGGGGCATATG"
print(dogma.transcribe('ACGT'))
print(dogma.revcomp('AAAACGT'))
print(dogma.revcomp(s))
print(dogma.translate('ATGTAA'))
print(dogma.translate(s))
print(dogma.gc_comp(s))
print(dogma.gc_skew(s), dogma.gc_skew(dogma.revcomp(s)))
