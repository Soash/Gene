import random

def count_nbase(seq, Nbase):
    for x in Nbase:
        print(x+' =', seq.count(x))

def gc_content(seq):
    gc_ratio = (seq.count('G')+seq.count('C'))/len(seq) * 100
    print('GC Content = [{:.3f}]%'.format(gc_ratio))

def codon_pos(seq, Nbase):
    codon = ''.join(random.choices(Nbase, k=3))
    print('random codon  : '+codon)

    i = 0
    for x in seq:
        pos = seq.find(codon, i)
        if pos == -1:
            break
        print(pos, end=' ')
        i = pos+1

def transcription(seq):
    # dna > mrna : transcription
    transcription = seq.replace('T', 'U')
    print('\nTranscription : '+transcription)

def rev_comp(seq):
    global complement
    comp = []
    for nbase in seq:
        if nbase == 'A':
            comp.append('T')
        elif nbase == 'T':
            comp.append('A')
        elif nbase == 'G':
            comp.append('C')
        elif nbase == 'C':
            comp.append('G')
        elif nbase == 'U':
            comp.append('A')

    complement = ''.join(comp)
    print('Complement    : '+complement)

    rev_compliment = complement[::-1]
    print('Rev_Compli    : '+rev_compliment)


    