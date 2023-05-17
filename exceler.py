import xlrd

# Open the workbook
workbook = xlrd.open_workbook('schedules\Raspisanie-FIT-ochnaya-f.o-22_23-vesenniy-sem.-IYUN.xls')

# Define the sheet indices
sheet_indices = [0, 1, 2, 3, 4]  # Index 0 corresponds to the first sheet, index 1 to the second sheet, and so on

# Iterate over each sheet index
for sheet_index in sheet_indices:
    # Select the sheet by index
    sheet = workbook.sheet_by_index(sheet_index)

    # Get the number of rows and columns in the sheet
    num_rows = sheet.nrows
    num_cols = sheet.ncols

    # Define the column indices for the groups
    group_columns = [0, 1, 2, 3, 4]  # Adjust these indices as per your column positions

    # Iterate over each group column
    for col in group_columns:
        group_info = []
        # Extract the group information from the column
        for row in range(num_rows):
            group_value = sheet.cell_value(row, col)
            group_info.append(group_value)

        # Normalize the consecutive empty spaces to a maximum of two
        normalized_group_info = []
        empty_space_count = 0
        for info in group_info:
            if info == "":
                empty_space_count += 1
                if empty_space_count <= 2:
                    normalized_group_info.append(info)
            else:
                empty_space_count = 0
                normalized_group_info.append(info)

        # Print the group information
        print(f"Sheet Index: {sheet_index}, Column: {col+1}")
        for info in normalized_group_info:
            print(info)
        print()
