from api import get_team_data, get_team_events, get_team_event_performance
from analyzer import analyze_team, compare_teams
from match_simulator import simulate_match, load_data

def main():
    while True:
        print("FRC Statbotics-based Team Analyzer Tool")
        print("1: Get the history of a team at an event and see history of the team overall")
        print("2: Compare six teams and their stats (2025)")
        print("3: Simulate a match between 6 teams of your choice (2025 data)")
        choice = input("Enter an option (1-3): ")

        if choice == "1":
            team_number = input("Enter a team number to load history: ")
            year = input ("Enter a year: ")
            history_data = get_team_data(team_number)
            events = get_team_events(team_number, year)
            print(f"Events for {team_number} in {year}:")
            for event in events:
                print(f"{event['name']} ({event['key']})")

            # Optionally fetch matches from one event:
            
            event_key = input("Please input the event key you want to search through: ")
            matches = None
            for event in events:
                if event_key == event['key']:
                    matches = get_team_event_performance(f"frc{team_number}", event_key)
                    break

            if matches is None:
                print("Event not found")
                exit()


            print(f"\nMatches for {team_number} at {event_key}:")
            for match in matches:
                print(f"{match['comp_level']} {match['match_number']}")
            analyze_team(team_number, history_data)
        elif choice == "2":
            pf = load_data()  # Make sure pf is loaded here!
            teams = []
            for i in range(6):
                while True:
                    t = input(f"Enter team {i+1}'s number: ")
                    try:
                        t_int = int(t)
                    except ValueError:
                        print("Team number must be an integer")
                        continue
                    if t_int in pf["num"].values:
                        teams.append(t_int)
                        break
                    else:
                        print(f"Team not found in data. Please re-enter.")
            compare_teams(teams)
        elif choice =="3":

            pf = load_data()
            team_numbers =  {"red1": 1, "red2": 4, "red3": 16,
                    "blue1": 33, "blue2": 78, "blue3": 148}
            team_numbers["red1"] = input("Enter Red Alliance Team 1 Number: ")
            team_numbers["red2"] = input("Enter Red Alliance Team 2 Number: ")
            team_numbers["red3"] = input("Enter Red Alliance Team 3 Number: ")
            team_numbers["blue1"] = input("Enter Blue Alliance Team 1 Number: ")
            team_numbers["blue2"] = input("Enter Blue Alliance Team 2 Number: ")
            team_numbers["blue3"] = input("Enter Blue Alliance Team 3 Number: ")
            simulate_match(team_numbers, pf)
        else:
            print("Invalid Choice. Exiting")

if __name__ == "__main__":
    main()