import run_clustalw from my_modules
import draw_phylogenetic_tree from my_modules

# performing multiple sequence alignments
input_file_path1 = "./combined_breeds_first_10.fa"
stdout, stderr = run_clustalw(input_file_path1)

input_file_path2 = "./combined_breeds_2nd_set.fa"
stdout, stderr = run_clustalw(input_file_path2)

input_file_path3 = "./combined_breeds_3rd_set.fa"
stdout, stderr = run_clustalw(input_file_path3)

input_file_path4 = "./combined_breeds_4th_set.fa"
stdout, stderr = run_clustalw(input_file_path4)

input_file_path5 = "./combined_breeds_5th_set.fa"
stdout, stderr = run_clustalw(input_file_path5)

input_file_path6 = "./combined_breeds_6th_set.fa"
stdout, stderr = run_clustalw(input_file_path6)

input_file_path7 = "./combined_breeds_7th_set.fa"
stdout, stderr = run_clustalw(input_file_path7)

input_file_path8 = "./combined_breeds_8th_set.fa"
stdout, stderr = run_clustalw(input_file_path8)

input_file_path9 = "./combined_breeds_9th_set.fa"
stdout, stderr = run_clustalw(input_file_path9)

input_file_path10 = "./combined_breeds_10th_set.fa"
stdout, stderr = run_clustalw(input_file_path10)

input_file_path11 = "./combined_breeds_11th_set.fa"
stdout, stderr = run_clustalw(input_file_path11)


# Drawing a phylogenetic trees for each .dnd file produced after running multiple sequence alignments on 11 sets of .fa files
file_path1 = "./combined_breeds_first_10.dnd"
file_path2 = "./combined_breeds_2nd_set.dnd"
file_path3 = "./combined_breeds_3rd_set.dnd"
file_path4 = "./combined_breeds_4th_set.dnd"
file_path5 = "./combined_breeds_5th_set.dnd"
file_path6 = "./combined_breeds_6th_set.dnd"
file_path7 = "./combined_breeds_7th_set.dnd"
file_path8 = "./combined_breeds_8th_set.dnd"
file_path9 = "./combined_breeds_9th_set.dnd"
file_path10 = "./combined_breeds_10th_set.dnd"
file_path11 = "./combined_breeds_11th_set.dnd"
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

