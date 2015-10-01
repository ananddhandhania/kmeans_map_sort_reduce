# kmeans_map_sort_reduce
This repository contains python code to perform K-Means Clustering on N dimensional data using MapReduce Model.


Usage:
echo "$(cat mapper_data)" | python mapper.py | python sortKeys.py | python reducer.py 

You can check the intermediate outputs as well. The dimensions field has to be update in both mapper and reducer. This code needs some cleaning.
