import itertools

def generate_mutatex_input(residues, output_file, chain = False):
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    mutations = []

    for residue in residues:
        for aa in amino_acids:
            if residue[1] != aa:
                if chain==True:
                    mutations.append(f"{residue[1]}{residue[2]}{residue[0]}"+";")
                else:
                    mutations.append(f"{residue[1]}{residue[0]}"+";")

    with open(output_file, "w") as f:
        for mutation in mutations:
            f.write(f"{mutation}\n")

# Example usage
def generate_mutatex_input(residues, output_file, chain = False):
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    mutations = []

    for residue in residues:
        if chain==True:
            mutations.append(f"{residue[1]}{residue[2]}{residue[0]}"+";")
        else:
            mutations.append(f"{residue[1]}{residue[0]}"+";")

    with open(output_file, "w") as f:
        for mutation in mutations:
            f.write(f"{mutation}\n")


# Example usage
residues = [("417", "N", "X"), ("486", "P", "X"), ("501", "Y", "X"), ("505", "H", "X"), ("497", "F", "X"), ("445", "P", "X"), ("498", "R", "X"), ("493", "Q", "X"), ("449", "Y", "X")]
output_file = "../mutatex/individual_list.txt"

generate_mutatex_input(residues, output_file)
