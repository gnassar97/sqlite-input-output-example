awk -F':' '{print $1"\n"$2}' < terms.txt | 
sed 's/\\/ /g' | db_load -T -c duplicates=1 -t btree em.idx 
