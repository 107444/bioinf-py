from dna_classes2 import Gene

# Create a Gene object with no DNA and no exon regions
gene = Gene()  # generate_string() will be used now 

print("Randomly generated DNA sequence:")
print(gene.get_dna())  # Output the random DNA sequence
print("Exon Regions:")
print(gene.get_exons())  # Should be None since no exon regions are provided
