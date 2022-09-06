# Comparing the connectome similarity of monozygotic twins

This paper studies the similarity between connectomes (brain networks) of monozygotic twins pairs and those of nontwins. It also explores possible relationships with connectomic similarity and age as well as sex. These similarites are then investigated for dizygotic twins as well.

It is discovered that the monozygotic twins have much higher connectomic similarity than that of the average of other nontwins, with an effect size of 1.56 and 
p < 10-6. The same was observed with dizygotic twins although to a lesser degree, with an effect size of 0.647 and a p-value of 0.00065. 

No relationship was observed between monozygotic and dizygotic twin pair’s connectome correlation with each other and sex or age. We assume that monozygotic twin brain 
networks are very similar because of their nearly identical genetic origin, while dizygotic twin brain networks are similar because of their familial relationship.

# Data

The data processed with this code and subsequently used in the paper is not included in this repository, but can be found here: https://zenodo.org/record/4733297#.YxbHVqHMJPY. The files used in this study were 
- HCP_HCPMMP1ANDfslatlas20_iFOD2_NOSIFT_standard.mat (for connectome data)
- twinCovariatesDWI_only_twin.mat (for monozygotic and dizygotic twin matching)

The connectome data Matlab file was downgraded to MatLab 7.2 to allow a more simple import using scipy into python. This downgraded matlab file is called loadable2.mat in the code.

This data was based on the Human Connectome Project (HCP) and was processed and prepared by the authors of the paper "Genetic influences on hub connectivity of the human connectome" (https://doi.org/10.1038/s41467-021-24306-2).

As referenced in the code, the original connectome data has 380 reigons despite using the HCPMMP1 parcellation atlas (360 reigons). The additional 20 reigons are subcortical reigons and are removed in the code for this paper.

# Thanks

Special thanks to Aurina Arnatkeviciute for her help with understanding how the connectome data is structured and for her paper.
Special thanks to Yusuf Osmanlioglu for his invalueable asssitance guiding this study and teaching me about the domain of computational neuroscience.

This paper is not published in any journal.
