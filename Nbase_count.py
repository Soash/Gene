import random
import gene

nucleic_acid = int(input('1. DNA\n2. RNA\n'))
length = int(input('Length = '))

if nucleic_acid == 1:
    Nbase = 'ATGC'; fname = 'dna'
elif nucleic_acid == 2:
    Nbase = 'AUGC'; fname = 'rna'
    
seq = ''.join(random.choices(Nbase, k=length))

file_name = 'random_'+fname+'_seq.txt'

try:
    file = open(file_name, 'w')
    file.write(seq)
except:
    print('file exists')

file = open(file_name, 'r')
seq = file.read()
print('Primary Seq   : '+seq)

gene.count_nbase(seq, Nbase)
gene.gc_content(seq)
gene.codon_pos(seq, Nbase)
gene.transcription(seq)
gene.rev_comp(seq)

file.close()


