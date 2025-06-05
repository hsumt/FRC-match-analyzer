from api import get_team_data, get_team_events, get_team_event_performance
from analyzer import analyze_team, compare_teams
from match_simulator import simulate_match, load_data

def main():
    print("FRC Statbotics-based Team Analyzer Tool")
    print("1: Get, analyze, and see history of one team")
    print("2 Compare six teams and their stats")
    print("3 Simulate a match between 6 teams of your choice")
    choice = input("Enter an option (1-3): ")

    if choice == "1":
        team_number = input("Enter a team number to load history: ")
        year = input ("Enter a year")
        history_data = get_team_data(team_number)
        events = get_team_events(team_number, year)
        print(f"Events for {team_number} in {year}:")
        for event in events:
            print(f"{event['name']} ({event['key']})")

        # Optionally fetch matches from one event:
        event_key = events[0]["key"]
        matches = get_team_event_performance(f"frc{team_number}", event_key)

        print(f"\nMatches for {team_number} at {event_key}:")
        for match in matches:
            print(f"{match['comp_level']} {match['match_number']}: {match['score_breakdown']}")
        analyze_team(team_number, history_data)
    elif choice == "2":
        teams = []
        for i in range(len(teams)):
            t = input(f"Enter team {i+1}'s number: ")
            teams.append(t)
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
       exit()

if __name__ == "__main__":
    main()