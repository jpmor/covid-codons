from codons import codon_table as table

dna2rna = lambda b: {'t':'a', 'a':'u', 'c': 'g', 'g': 'c'}[b]
rna2dna = lambda b: {'u':'a', 'a':'t', 'c': 'g', 'g': 'c'}[b]

transcript = lambda seq: "".join([dna2rna(b) for b in seq])
reverse_transcript = lambda seq: "".join([rna2dna(b) for b in seq])

def codons(seq):
    return [seq[i:i+3] for i in range(0, len(seq), 3)]

def info(codon):
   return ('','','','') if codon not in table else table[codon]

def infoList(codon_list, i=None):
    if i:
        return [info(c)[i] for c in codon_list]
    else:
        return [info(c) for c in codon_list]

with open('origin.txt') as f:
    lines = [line.rstrip() for line in f]

covid = "".join(lines)

i = 0
j = j_base = 1
j_limit = 5

d = {}
# create subdicts
multiples = j_limit - j_base
for sl in range(j_base, j_limit):
    sd = str(sl * 3)
    d[sd] = {}


while i < len(covid) - j_base:
    while j < j_limit and i + j < len(covid):
        seq = covid[i:i + j * 3]
        dd = d[str(j * 3)]

        if seq in dd:
            dd[seq] += 1
        else:
            dd[seq] = 1

        j += 1

    j = j_base
    i += 1

# sort each subdict
for sl in range(j_base, j_limit):
    sd = str(sl * 3)
    d[sd] = sorted(d[sd].items(), key=lambda item: item[1], reverse=True)

    print("\nmost common with len {}\n".format(sd))
    for i in range(5):
        seq, count = d[sd][i]

        mapped_codons = infoList(codons(seq))

        print(count, mapped_codons)


