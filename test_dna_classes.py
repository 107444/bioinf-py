from dna_classes import Gene

# Example DNA sequence and exon regions
dna = "ATGCGTACGTAGCTAGCTAG"
exon_regions = [(0, 3), (5, 8), (10,13)]  # Start and end positions of exons

# Create a Gene object
gene = Gene(dna, exon_regions)

# 1. Use Gene.get_dna to get the full DNA sequence
print("Full DNA sequence:")
print(gene.get_dna())  # Expected: "ATGCGTACGTAGCTAGCTAG"

# 2. Use Gene.get_exons to get all exons 
print("Exon Regions:")
exons = gene.get_exons() #exon = Region(dna, 0,3)
for i, exon in enumerate(exons, start=1):
    print(f"Exon {i}: {exon.get_region()}")

# 3. Use Region.get_region on the first exon
print("First exon sequence using Region.get_region:")
print(exons[0].get_region())
print(exons[1].get_region())
print(exons[2].get_region())