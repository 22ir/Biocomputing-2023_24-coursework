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


# Drawing a phylogenetic trees for each .dnd file produced after running multiple sequence alignments on 11 sets of .fa files
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
draw_phylogenetic_tree(file_path1)
draw_phylogenetic_tree(file_path2)
draw_phylogenetic_tree(file_path3)
draw_phylogenetic_tree(file_path4)
draw_phylogenetic_tree(file_path5)
draw_phylogenetic_tree(file_path6)
draw_phylogenetic_tree(file_path7)
draw_phylogenetic_tree(file_path8)
draw_phylogenetic_tree(file_path9)
draw_phylogenetic_tree(file_path10)
draw_phylogenetic_tree(file_path11)

