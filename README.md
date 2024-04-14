# Biocomputing-2023_24-coursework/dog dna identification tool
## Introduction
This is a dog dna identification tool that can assist in comparing the similarity between an unknown dog breed dna sequence and dog breed dna database 

## External programs and libraries used:
1. ClustalW2
2. Biopython

## Workflow summary
1. Install ClustalW2
2. Split dog_breeds.fa file into files with less sequences (e.g 10 in each file, including the mystery.fa sequence as the first sequence)
3. Perform multiple sequence alignments (ClustalW2) on all generated files
4. Draw phylogenetic trees for each .dnd file generated during multiple sequence alignments
5. Visually analyse phylogenetic trees and select breeds closest to your mystery sequence paying attention to the branch lengths
6. Manually create closest_in_phyl_tree.fa FASTA file adding your mystery sequence and the sequences chosen during step 5 (This can be done by opening FASTA files on VScode)
7. Perform multiple sequence alignment on a closest_in_phyl_tree.fa file
8. Draw a phylogenetic tree for the .dnd file generated during multiple sequence alignments in step 7
9. Visually analyse the phylogenetic tree and decide which dog breed sequence has most similarity to your unknown sequence


