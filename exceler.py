import xlrd

# Open the workbook
workbook = xlrd.open_workbook('schedules\Raspisanie-FIT-ochnaya-f.o-22_23-vesenniy-sem.-IYUN.xls')

# Define the sheet index and group name
sheet_index = 2  # Index 2 corresponds to the third sheet (2 курс)
group_name = "о. ИД 23.4/Б-21"

# Select the sheet by index
sheet = workbook.sheet_by_index(sheet_index)

# Get the number of rows and columns in the sheet
num_rows = sheet.nrows
num_cols = sheet.ncols

# Find the row indices for the group name
group_row_indices = []
for row in range(num_rows):
    cell_value = sheet.cell_value(row, 6)  # Assuming group name is in column G (index 6)
    if cell_value == group_name:
        group_row_indices.append(row)

if group_row_indices:
    # Print the group information
    print(f"Group: {group_name}")

    # Define the column indices for the days of the week
    day_column_indices = [1, 2, 3, 4, 5]  # Adjust these indices as per your column positions

    for group_row_index in group_row_indices:
        # Iterate over the day column indices
        for day_column_index in day_column_indices:
            # Get the day of the week
            day_of_week = sheet.cell_value(group_row_index, day_column_index)

            # Get the schedule for the day
            schedule = []
            time_column_index = 7  # Starting column index for time slots (adjust as per your column position)
            while time_column_index < num_cols:
                time_slot = sheet.cell_value(group_row_index, time_column_index)
                if time_slot:
                    schedule.append(time_slot)
                time_column_index += 1

            # Print the schedule for the day
            print(f"\nDay of the Week: {day_of_week}")
            for time_slot in schedule:
                print(time_slot)

        # Get the dates for the group
        dates = []
        row_index = group_row_index + 1
        while row_index < num_rows:
            date = sheet.cell_value(row_index, 6)
            if date:
                dates.append(date)
            row_index += 1

        # Print the dates for the group
        print("\nDates:")
        for date in dates:
            print(date)
        print()

else:
    print(f"Group {group_name} not found in the sheet.")
