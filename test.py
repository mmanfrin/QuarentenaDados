from Bio import SeqIO

for record in SeqIO.parse("/mnt/c/Users/Marcos/Git/QuarentenaDados/Aula1/movies.csv", "csv"):
    print("%s %i" % (record.id, len(record)))