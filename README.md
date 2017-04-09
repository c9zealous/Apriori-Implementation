# Apriori-Implementation
Apriori Implementation using python
**************************************************************************************************************************************************************************************************************
Definition: Association rule mining is used to find frequent item sets from large transactional databases. Apriori is specifically designed to handle large databases containing transactions. The associations discovered using apriori help in discovering how the items are linked to each other. For example in a grocery store items which are associated can be placed next to each other. Further associations can be determined using three techniques :
support - an indication of how popular an item set is, thereby providing its significance in comparison with other items.
confidence - an indicator of how likely an item Y is purchased when item X is purchased indicated as X->Y.
lift - indicates how likely item Y is purchased when item X is purchased, while controlling how popular item Y is.
The apriori algorithm reduces the number of item sets we need to examine. I.E. if a given itemset is infrequent then all of its subsets are also infrequent.

Problem statement for the assignment: Given a transactional dataset of retail market basket data find the frequent itemsets from the database and generate rules using the minimum confidence value.

Description: 
The problem is tackled in the following manner in the program:
•	In the script apriori.py the dataset retail.dat is initially passed using the command line. This dataset is then read line by line and each individual transaction is identified inside transactions. 
•	After this the minimum support and confidence is stored in min_support and min_confidence which is taken from the user as input. 
•	After this the aprioriloop function is used to run the apriori algorithm on each transaction of the dataset. The candidate sets and frequency sets for every pass are generated in the while loops. The frequencyset obtained has all the minimum support key value pairs. 
•	Using this frequencyset and the final apriori result are then passed to the rulegeneration function. This function based on the number of keys in the final apriori results generates the association rules along with their corresponding confidence values.
•	After that using the pandas dataframe we load the rules into the variable df in the item value pairs. The value of df is then displayed in the command line.
•	The displayed values are nothing but the rules with their corresponding confidence values.
