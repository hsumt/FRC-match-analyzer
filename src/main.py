from api import get_team_data, get_team_events, get_team_event_performance
from analyzer import analyze_team, compare_teams
from match_simulator import simulate_match, load_data

def main():
    while True:
        print("-------FRC Data-based Team Analyzer Tool-------")
        print("1: Get the matches of a team at an event and see history of the team overall")
        print("2: Compare six teams and their stats (2025)")
        print("3: Simulate a match between 6 teams of your choice (2025 data)")
        choice = input("Enter an option (1-3): ")

        if choice == "1":
            team_number = input("Enter a team number to load history: ")
            try:
                team_number_int = int(team_number)
            except ValueError:
                print("Team number must be an integer.")
                continue

            history_data = get_team_data(team_number)
            if not history_data:
                print("Team not found in search")
                continue

            year = input("Enter a year: ")
            try:
                year_int = int(year)
            except ValueError:
                print("Year must be an integer.")
                continue

            events = get_team_events(team_number, year_int)
            if not events:
                print(f"No events found for team {team_number} in {year_int}.")
                continue

            print(f"Events for {team_number} in {year_int}:")
            for event in events:
                print(f"{event['name']} ({event['key']})")

            event_key = input("Please input the event key you want to search through: ")
            matches = None
            for event in events:
                if event_key == event['key']:
                    matches = get_team_event_performance(f"frc{team_number}", event_key)
                    break

            if matches is None:
                print("Event not found or no match data.")
                return

            print(f"\nMatches for {team_number} at {event_key}:")
            for match in matches:
                print("---------------------------------------------")
                print(f"{match['comp_level']} {match['match_number']}")
                print(f"{match['score_breakdown']}")
                print("---------------------------------------------")
                print("---------------------------------------------")
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
            pf["num"] = pf["num"].astype(int)
            team_numbers = {}

            for alliance, i in [("Red Alliance", 1), ("Red Alliance", 2), ("Red Alliance", 3),
                                ("Blue Alliance", 1), ("Blue Alliance", 2), ("Blue Alliance", 3)]:
                while True:
                    team_input = input(f"Enter {alliance} Team {i} Number: ")
                    try:
                        team_int = int(team_input)
                    except ValueError:
                        print("Team number must be an integer.")
                        continue

                    if team_int in pf["num"].values:
                        key = f"{alliance.lower().split()[0]}{i}"
                        team_numbers[key] = team_int
                        break
                    else:
                        print("Team not found in data. Please re-enter.")

            simulate_match(team_numbers, pf)
        else:
            print("Invalid Choice. Exiting")

if __name__ == "__main__":
    main()