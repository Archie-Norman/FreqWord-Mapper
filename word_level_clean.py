import os
import re
import pandas as pd

# POS tag mapping
pos_map = {
    'n.': 'noun',
    'v.': 'verb',
    'adj.': 'adjective',
    'adv.': 'adverb',
    'conj.': 'conjunction',
    'det.': 'determiner',
    'pron.': 'pronoun',
    'prep.': 'preposition',
    'num.': 'number',
    'interj.': 'interjection',
    'aux.': 'auxiliary verb',
    'modal.': 'modal verb',
    'exclam.': 'exclamation',
    'phr.': 'phrase',
    'prep./adv.': 'preposition/adverb',
    'det./pron.': 'determiner/pronoun',
    'v. phr.': 'verb phrase',
    'n. phr.': 'noun phrase',
    'adv. phr.': 'adverb phrase',
    'adj. phr.': 'adjective phrase',
    'v./n.': 'verb/noun',
    'adj./adv.': 'adjective/adverb',
    'pron./det.': 'pronoun/determiner',
    'modal v.': 'modal verb',
    'aux. v.': 'auxiliary verb',
    'auxiliary v.': 'auxiliary verb',
    'be v.': 'verb (be)',
    'an indefinite article': 'article',
    'possessive adjective': 'possessive adjective',
    'possessive pronoun': 'possessive pronoun',
    'reflexive pronoun': 'reflexive pronoun',
    'demonstrative pronoun': 'demonstrative pronoun',
    'relative pronoun': 'relative pronoun',
    'interrogative pronoun': 'interrogative pronoun',
    'indefinite pronoun': 'indefinite pronoun',
}

# Folder containing files
folder_path = "c:/Users/archi/Desktop/Fiverr/Sanledes/word_levels"
rows = []

# Loop through all .txt files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        level = filename.replace(".txt", "").upper()
        with open(os.path.join(folder_path, filename), encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):
                # Remove anything inside parentheses, like (money), before splitting
                clean_line = re.sub(r'\([^)]*\)', '', line).strip()
                parts = clean_line.split()

                if len(parts) >= 2:
                    word = parts[0]
                    raw_pos = ' '.join(parts[1:])
                    
                    # Split on slashes or commas
                    pos_tags = re.split(r'[/,]', raw_pos)
                    pos_full_list = []

                    for tag in pos_tags:
                        tag = tag.strip()
                        if tag in pos_map:
                            pos_full_list.append(pos_map[tag])
                        else:
                            pos_full_list.append("NA")  # Assign "NA" if POS tag not found
                            print(f"⚠️ Unknown POS tag '{tag}' in file '{filename}', line {line_number}. Assigned 'NA'.")

                    pos_full = ', '.join(pos_full_list)
                    rows.append({
                        "word": word,
                        "level": level,
                        "pos": pos_full
                    })

# Create DataFrame and export
df = pd.DataFrame(rows)
df.to_csv("cefr_word_data.csv", index=False)
print("✅ Successfully saved to 'cefr_word_data.csv'")