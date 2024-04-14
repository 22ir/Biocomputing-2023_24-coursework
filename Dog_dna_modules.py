"""
my_modules file contains the following functions:
run_clustalw, draw_phylogenetic_tree 

"""

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
