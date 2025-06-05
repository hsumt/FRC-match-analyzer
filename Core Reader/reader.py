import pandas as pd #use for column reading

import colorama as cr
# import csv. didn't use it

def team_total_score(auto, tele, end):
    return auto + tele + end

# Load CSV
pf = pd.read_csv('Book1.csv')
print(pf)

team_scores = {}
red_total = 0
blue_total = 0
red_foul_points = 0
blue_foul_points = 0

for i in range(len(pf)):
    row = pf.iloc[i]
    auto = row["auto_points"]
    tele = row["teleop_points"]
    endgame = row["endgame_points"]
    minor_fouls = row["minor_fouls"]  
    score = float(team_total_score(auto, tele, endgame))

    # Individual score (not including fouls)
    team_scores[f"Team{i+1} ({int(row['team'])})"] = score

    # FOUL POINT LOGIC
    minor_foul_points = int(2 * minor_fouls) # minor foul = 2 major =6
    if row["red?"] == 1:
        red_total += score  # red alliance gets their base score
        blue_foul_points += minor_foul_points  # fouls committed by red benefit blue
    else:
        blue_total += score  # blue alliance gets their base score
        red_foul_points += minor_foul_points  # fouls committed by blue benefit red

# Add foul points to opposing alliance totals
red_total += red_foul_points
blue_total += blue_foul_points

# Print all individual team scores
for key, value in team_scores.items():
    print(f"{key} total score: {value}")

highest = max(team_scores, key=team_scores.get)
lowest = min(team_scores, key=team_scores.get)

print(f"Highest Performing Team: {highest}")
print(f"Lowest Performing Team: {lowest}")

# Print alliance totals
print(f"\nRed Alliance Score Estimate: {round(red_total)}")
print(f"Blue Alliance Score Estimate: {round(blue_total)}")
print(f"Foul Points Awarded to the Red Alliance {red_foul_points}")
print(f"Foul points Awarded to the Blue Alliance {blue_foul_points}")






'''Archived Code
with open("Book1.csv", 'r') as file:
    csvreader = csv.DictReader(file)

    for row in csvreader:
        print(f"{row['team']}, {row["auto_points"]}")

try:
    parsedfile =  pd.read_csv('Book1.csv')
    print(parsedfile)
except FileNotFoundError:
    print("File not found. Please ensure the CSV file is in the correct directory.")

with open('Book1.csv', 'r') as file:
    data = csv.DictReader(file)
    for row in data:
        print(row["team"])    # prints the value in the "team" column'''