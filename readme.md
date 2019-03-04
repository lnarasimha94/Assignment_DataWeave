1. import the packages pandas and numpy and store the two files with names today.json, yesterday.json in 'data' direcory.
2. load the two json files into separate dataframes
3. find the urlh overlapping count from the indivial dataframes and combined.
4. then select the category column and extracted even the values are occured multiple times as one.
5. Unique categories are extracted from the combination of the both sorted dataframes and combined it to sort out the unique categories among both the files
6. Then by using length we can count exact unique categories.
7. Then displayed the non overlapping categories using printing statement
8. Later to fing the taxonomies first combined the both dataframes into single dataframe.
8. later apply groupby operation to the "category" and "subcategory" with detailed extraction.
9. Later organize the sorted data from the groupby with the looping , iterrows() methods. and printed using statement in the loop.
10. Later select the "mrp" column from the dataframe and replaced "0" and Non float numbers with "NA"
11. Finally the modified data of "mrp" stored into dataframe.
12. Export the complete dataframe into new csv file 
13. Result will be store as csv in output folder.
