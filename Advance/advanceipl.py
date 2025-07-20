import pandas as pd

file_path =  r"C:\Users\Ram\ShadowFox\Advance\advance_ipl.xlsx"

try:
    summary_df = pd.read_excel(file_path, sheet_name='Sheet1')
    events_df = pd.read_excel(file_path, sheet_name='Both Innings')
except Exception as e:
    print("Error loading Excel file:", e)
    exit()

summary_df.columns = summary_df.columns.str.strip()
events_df.columns = events_df.columns.str.strip()
summary_df.fillna(0, inplace=True)
events_df.fillna('', inplace=True)

input_name = input("Enter the fielder's name: ").strip().lower()
summary_df['name_lower'] = summary_df['Player Name'].str.strip().str.lower()
events_df['name_lower'] = events_df['Player Name'].str.strip().str.lower()

matched_summary = summary_df[summary_df['name_lower'] == input_name]
matched_events = events_df[events_df['name_lower'] == input_name]

if matched_summary.empty:
    print(f"No matching fielder found for: {input_name}")
    exit()

row = matched_summary.iloc[0]
ps = (
    row['Clean Picks'] * 1 +
    row['Good Throws'] * 1 +
    row['Catches'] * 3 +
    row['Dropped Catches'] * -3 +
    row['Stumping'] * 3 +
    row['Runouts'] * 3 +
    row['Missed Run Out'] * -2 +
    row['Direct Hits'] * 2 +
    row['Runs Saved']
)

position_data = matched_events.groupby('Position')['Runs'].sum().reset_index()

print(f"\n Fielding Report for: {row['Player Name']}")
print(f" Performance Score: {ps}")
print(f" Total Runs Saved: {row['Runs Saved']}\n")

print(" Runs Saved by Position:")
if not position_data.empty:
    for _, pos_row in position_data.iterrows():
        print(f"  - {pos_row['Position']}: {pos_row['Runs']} runs saved")
else:
    print("  - No position data found")
print("\nSpecial Efforts Fielding:")
print(f" Catches: {int(row['Catches'])}")
print(f" Dropped Catches: {int(row['Dropped Catches'])}")
print(f" Stumpings: {int(row['Stumping'])}")
print(f" Run Outs: {int(row['Runouts'])}")
print(f" Missed Run Outs: {int(row['Missed Run Out'])}")
print(f" Direct Hits: {int(row['Direct Hits'])}")

#---------------OUTPUT-----------------------------
#Enter the fielder's name: Abhishek Porel

# Fielding Report for: Abhishek Porel
# Performance Score: 16.0
# Total Runs Saved: 4

 #Runs Saved by Position:
 # - Keeper: 4 runs saved

#Special Efforts Fielding:
# Catches: 1
# Dropped Catches: 0
# Stumpings: 0
# Run Outs: 0
# Missed Run Outs: 0
# Direct Hits: 0 