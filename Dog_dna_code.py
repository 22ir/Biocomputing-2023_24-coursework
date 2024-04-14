import Dog_dna_modules 

# Create smaller .fa files containing 10 sequences (myster.fa seq + 9 other dog breed sequences)
Dog_dna_modules.add_mystery_to_split_breeds("mystery.fa", "dog_breeds.fa", "dog_breeds_subset", 9)

# performing multiple sequence alignments
input_file_path1 = "./combined_breeds_subset_1.fa"
stdout, stderr = Dog_dna_modules.run_clustalw(input_file_path1)

input_file_path2 = "./combined_breeds_subset_2.fa"
stdout, stderr = Dog_dna_modules.run_clustalw(input_file_path2)

input_file_path3 = "./combined_breeds_subset_3.fa"
stdout, stderr = Dog_dna_modules.run_clustalw(input_file_path3)

input_file_path4 = "./combined_breeds_subset_4.fa"
stdout, stderr = Dog_dna_modules.run_clustalw(input_file_path4)

input_file_path5 = "./combined_breeds_subset_5.fa"
stdout, stderr = Dog_dna_modules.run_clustalw(input_file_path5)

input_file_path6 = "./combined_breeds_subset_6.fa"
stdout, stderr = Dog_dna_modules.run_clustalw(input_file_path6)

input_file_path7 = "./combined_breeds_subset_7.fa"
stdout, stderr = Dog_dna_modules.run_clustalw(input_file_path7)

input_file_path8 = "./combined_breeds_subset_8.fa"
stdout, stderr = Dog_dna_modules.run_clustalw(input_file_path8)

input_file_path9 = "./combined_breeds_subset_9.fa"
stdout, stderr = Dog_dna_modules.run_clustalw(input_file_path9)

input_file_path10 = "./combined_breeds_subset_10.fa"
stdout, stderr = Dog_dna_modules.run_clustalw(input_file_path10)

input_file_path11 = "./combined_breeds_subset_11.fa"
stdout, stderr = Dog_dna_modules.run_clustalw(input_file_path11)


# Drawing phylogenetic trees for each .dnd file produced after running multiple sequence alignments on 11 sets of .fa files
file_path1 = "./combined_breeds_subset_1.dnd"
file_path2 = "./combined_breeds_subset_2.dnd"
file_path3 = "./combined_breeds_subset_3.dnd"
file_path4 = "./combined_breeds_subset_4.dnd"
file_path5 = "./combined_breeds_subset_5.dnd"
file_path6 = "./combined_breeds_subset_6.dnd"
file_path7 = "./combined_breeds_subset_7.dnd"
file_path8 = "./combined_breeds_subset_8.dnd"
file_path9 = "./combined_breeds_subset_9.dnd"
file_path10 = "./combined_breeds_subset_10.dnd"
file_path11 = "./combined_breeds_subset_11.dnd"
Dog_dna_modules.draw_phylogenetic_tree(file_path1)
Dog_dna_modules.draw_phylogenetic_tree(file_path2)
Dog_dna_modules.draw_phylogenetic_tree(file_path3)
Dog_dna_modules.draw_phylogenetic_tree(file_path4)
Dog_dna_modules.draw_phylogenetic_tree(file_path5)
Dog_dna_modules.draw_phylogenetic_tree(file_path6)
Dog_dna_modules.draw_phylogenetic_tree(file_path7)
Dog_dna_modules.draw_phylogenetic_tree(file_path8)
Dog_dna_modules.draw_phylogenetic_tree(file_path9)
Dog_dna_modules.draw_phylogenetic_tree(file_path10)
Dog_dna_modules.draw_phylogenetic_tree(file_path11)

# Manually create closest_in_phyl_tree.fa FASTA file adding your mystery sequence and the sequences chosen after visual analysis of
# the phylogenetic trees and selection of breeds closest to your mystery sequence paying attention to the branch lengths 
# (This can be done by opening FASTA files on VScode)

# Pausing execution and instructing the user
input("Please create closest_in_phyl_tree.fa FASTA file and press Enter to continue...")

# Performing multiple sequence alignment on a FASTA file with all sequences closest to mystery sequence in phylogenetic trees
closest_in_phyl_tree_path = "./closest_in_phyl_tree.fa"
stdout, stderr = Dog_dna_modules.run_clustalw(closest_in_phyl_tree_path)

# Drawing a phylogenetic tree for the .dnd file produced after running multiple sequence alignments on closest_in_phyl_tree.fa file
closest_matches_tree_path = "./closest_in_phyl_tree.dnd"
Dog_dna_modules.draw_phylogenetic_tree(closest_matches_tree_path)
