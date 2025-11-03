def to_rna(dna_strand):
    complement = {"G" : "C", "C" : "G", "T" : "A", "A" : "U"}
    return "".join([complement.get(value) for value in dna_strand])
