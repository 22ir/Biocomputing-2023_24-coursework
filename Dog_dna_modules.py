"""
my_modules file contains the following functions:
add_mystery_to_split_breeds, run_clustalw, draw_phylogenetic_tree 

"""
def add_mystery_to_split_breeds(mystery_file, input_file, output_prefix, num_sequences_per_file):
    """
    Split sequences from a dataset FASTA file into smaller files and add the sequence from mystery_file to each file.

    Args:
        mystery_file (str): FASTA file with the unknown sequence path.
        input_file (str): Input FASTA file path.
        output_prefix (str): Prefix for output file names.
        num_sequences_per_file (int): Number of sequences in each output file.

    Returns:
        None
    """
    from Bio import SeqIO

    # Open the mystery FASTA file
    with open(mystery_file, "r") as mystery:
        mystery_record = next(SeqIO.parse(mystery, "fasta"))

    # Open the input FASTA file
    with open(input_file, "r") as file:
        # Parse the input file and get the records
        records = list(SeqIO.parse(file, "fasta"))

    # Calculate the number of output files needed
    num_output_files = (len(records) + num_sequences_per_file - 1) // num_sequences_per_file

    # Iterate over the range of output file indices
    for i in range(num_output_files):
        # Define the start and end indices for the current output file
        start_index = i * num_sequences_per_file
        end_index = min((i + 1) * num_sequences_per_file, len(records))

        # Define the output file name
        output_file = f"{output_prefix}_{i + 1}.fa"

        # Write the sequences to the output file
        with open(output_file, "w") as outfile:
            # Write mystery sequence first
            SeqIO.write(mystery_record, outfile, "fasta")

            # Write the sequences from the input file
            SeqIO.write(records[start_index:end_index], outfile, "fasta")



def run_clustalw(input_file):
    """
    Run ClustalW with the specified input file.

    Args:
        input_file (str): Path to the input FASTA file.

    Returns:
        A tuple containing the stdout and stderr outputs.
    """
    import os
    import subprocess

    # Path to ClustalW executable
    clustalw_exe = "./clustalw2.exe"

    # Check if ClustalW executable exists
    assert os.path.isfile(clustalw_exe), "Clustal W executable missing"

    # Creating the command
    cmd = f"{clustalw_exe} -infile={input_file}"

    # Run ClustalW
    results = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if results.stderr:
        print("Error from ClustalW2:")
        print(results.stderr)
    elif results.stdout:
        print("Output from ClustalW2:")
        print(results.stdout)
    else:
        print("No output from ClustalW2")
    
    return results.stdout, results.stderr


def draw_phylogenetic_tree(file_path):
    """
    Read a phylogenetic tree from a Newick file and draw it using ASCII art.

    Args:
        file_path (str): Path to the Newick file containing the phylogenetic tree.

    Returns:
        None
    """
    from Bio import Phylo
    tree = Phylo.read(file_path, "newick")
    Phylo.draw_ascii(tree)
