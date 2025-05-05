import pandas as pd




df1 = pd.read_csv("c:/Users/archi/Desktop/Fiverr/Sanledes/cefr_word_data.csv")  # Make sure this file exists
df2 = pd.read_csv("c:/Users/archi/Desktop/Fiverr/Sanledes/cefr2.csv")  # Make sure this file exists
df3 = pd.read_csv("c:/Users/archi/Desktop/Fiverr/Sanledes/cefr3.csv")  # Make sure this file exists
df4 = pd.read_csv("c:/Users/archi/Desktop/Fiverr/Sanledes/cefr4.csv")  # Make sure this file exists


df1['word'] = df1['word'].str.lower().str.strip().str.replace('[^a-z]+', '', regex=True)
df3['headword'] = df3['headword'].str.lower().str.strip().str.replace('[^a-z]+', '', regex=True)
df4['headword'] = df4['headword'].str.lower().str.strip().str.replace('[^a-z]+', '', regex=True)



merged_1_3 = pd.merge(df1, df3, left_on='word', right_on='headword', how='left')
merged_1_3 = pd.merge(merged_1_3, df4, left_on='word', right_on='headword', how='left')



# Split shorthand code at the first dot
df2['AfterDot'] = df2['Shorthand Code'].str.split('.', n=1).str[1]

# Split remaining part on '.' and explode into rows
df2['Shorthand Split'] = df2['AfterDot'].str.split('.')
df2_exploded = df2.explode('Shorthand Split')

# Clean the shorthand: lowercase and strip
df2_exploded['Shorthand Clean'] = df2_exploded['Shorthand Split'].str.lower().str.strip()

# Step 4: Clean each shorthand: lowercase + replace _ with space + strip
df2_exploded['Shorthand Clean'] = (
    df2_exploded['Shorthand Split']
    .str.lower()
    .str.replace('_', ' ', regex=False)
    .str.strip()
)

# (Optional) Drop helper columns if you want a cleaner result
#df2_exploded = df2_exploded.drop(columns=['AfterDot', 'Shorthand Split'])

print(df2_exploded)
print(merged_1_3)


merged_all = pd.merge(merged_1_3, df2_exploded, left_on='word', right_on='Shorthand Split', how='left')

print(merged_all)

merged_all.to_csv("cefr_data.csv", index=False)
