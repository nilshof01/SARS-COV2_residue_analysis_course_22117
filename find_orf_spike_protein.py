from Bio import SeqIO

# Open the FASTA file and parse the nucleotide sequence




### find orf and
def find_orf(scaffolds, start_pos = 21562, end_pos = 25384):
    with open(scaffolds, "r") as handle:
        record = SeqIO.read(handle, "fasta")
        nucleotide_seq = record.seq
    s_gene_start = start_pos # Python uses 0-based indexing
    s_gene_end = end_pos

    # Find the closest ATG near the annotated start position
    start_codon = "ATG"
    search_start = max(0, s_gene_start - 50)
    search_end = s_gene_start + 50

    closest_atg_pos = -1
    min_distance = float('inf')

    for pos in range(search_start, search_end):
        if record.seq[pos:pos+3] == start_codon:
            distance = abs(s_gene_start - pos)
            if distance < min_distance:
                closest_atg_pos = pos
                min_distance = distance

    if closest_atg_pos != -1:
        adjusted_s_gene_start = closest_atg_pos
        adjusted_s_gene_sequence = record.seq[adjusted_s_gene_start:s_gene_end]
        adjusted_spike_protein_sequence = adjusted_s_gene_sequence.translate()
        print("Adjusted spike glycoprotein sequence:")
        print(adjusted_spike_protein_sequence)
    else:
        print("No start codon found near the annotated S gene start position.")
    return adjusted_spike_protein_sequence


def save_protein_fasta(protein_sequence, output_file, header=">protein"):
    with open(output_file, "w") as f:
        f.write(header + "\n")
        f.write(str(protein_sequence) + "\n")

# Replace with the path where you want to save the file
output_file = "spike_glycoprotein.fasta"
adjusted_spike_protein_sequence = find_orf(scaffolds)
save_protein_fasta(adjusted_spike_protein_sequence, output_file)
