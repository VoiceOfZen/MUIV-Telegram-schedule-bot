import pandas as pd

df = pd.read_excel(r'schedules\Raspisanie-FIT-ochnaya-f.o-22_23-vesenniy-sem.-IYUN.xls')

# Search for a specific text in the DataFrame
search_text = 'your_search_text'
found_rows = df[df.astype(str).apply(lambda row: row.str.contains(search_text, case=False).any(), axis=1)]

# Print the found rows
print(found_rows)
