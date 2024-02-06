import uproot
import numpy as np

#opens root file, open a branch, create histo with data and find the number of counts in the most populated bin
def find_max_count(root_file_name, tree_name, branch_name, bin):

    with uproot.open(root_file_name) as file:
        tree = file[tree_name]
        branches = tree.keys()
        tot_en_cry = tree[branch_name].array()

    counts, bin_edges = np.histogram(tot_en_cry, bin)
    max = np.max(counts)
    return max


    


