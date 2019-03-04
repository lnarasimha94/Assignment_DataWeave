import pandas as pd
import numpy as np
df_today= pd.read_json('data/today.json', lines=True)
df_yesterday= pd.read_json('data/yesterday.json', lines=True)

#No of URLH which are overlapping.
no_overlapp=df_today.duplicated(['urlh']).sum()+ df_yesterday.duplicated(['urlh']).sum()+2;
print("No of URLH which are overlapping including both files",no_overlapp)
tdata=df_today[df_today.duplicated('urlh', keep=False) == True]
ydata=df_yesterday[df_yesterday.duplicated('urlh', keep=False) == True]
c_t=list(tdata['category'].unique()).copy()
c_y=list(ydata['category'].unique()).copy()
uniq_cat = c_t + list(set(c_y) - set(c_t))
#No of Unique categories in both files
print("No of Unique categories in both files : ", len(uniq_cat))
#List of categories which is not overlapping
print ("List of categories which is not overlapping :\n ", uniq_cat)
# Generate the stats with count for all taxonomies
frames = [df_today, df_yesterday]
result = pd.concat(frames)
fdata=result.groupby("subcategory")['category'].describe().reset_index()
for index, row in fdata.iterrows():
    print (index+1,row["top"],">",row["subcategory"],":",row["freq"])
#Generation of a new file csv where mrp is normalized
max_value = result['mrp'].max()
min_value = result['mrp'].min()
result['mrp'] = (result['mrp'] - min_value) / (max_value - min_value)
#0 or a non-float value or the key doesn't exist, make it "NA"
result['mrp']=result['mrp'].replace(0,"NA")
result['mrp']=result['mrp'].replace("","NA")
result['mrp']=result['mrp'].replace(np.nan,"NA")
result.to_csv('out/nomralized.csv', sep='\t', encoding='utf-8')
