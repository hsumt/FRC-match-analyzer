# Match Analyzer

Match Analyzer is a Python-based CLI tool for analyzing and simulating FRC (First Robotics Competition) teams and matches using team insights and API data from Statbotics.io and TheBlueAlliance

## 🔧 Current Main Features

- Load team data from CSV
- Input alliance team numbers
- Validate team numbers against data
- Call Statbotics.io API for real-time data
- Simulate match outcomes with scoring breakdown
- Modular design for possible future interface or dashboard integration

## Future Plans
It is likely this project will not be touched for the current being. The future depends on whether an AI assistant would be recommendable or a smart picklisting function could be integrated within a dashboard.

## File Structure
match-analyzer/
```
├── data/
│   ├── 2025_insights.csv         # Full team performance dataset
│   └── 2025_insightsmini.csv     # Minimal version for quick testing if you need less data.

├── src/
│   ├── analyzer.py               # Core analysis functions
│   ├── api.py                    # Handles Statbotics API calls
│   ├── match_simulator.py        # Match scoring logic and simulation
│   └── main.py                   # CLI entry point

├── .gitignore
├── requirements.txt
├── README.md
```


## How to Get Started with usage
1. Clone the Repo
2. Install Dependencies
    Use requirements.txt and install the necessary libraries by running
    "pip install -r requirements.txt"
3. Run the CLI

Actively pulls data from Statbotics and TheBlueAlliance. Thanks to them for providing the public APIs for usage. Sadly Statbotics does not let me pull directly from the team stats real time.

## Documentation
### Final v1.1 6/6/2025
I'm planning to wrap up this project for now. Unfortunately, the raw data issue will need to be solved a different time. It's time to start another project. Core functionality all works and I'm really happy about it.


### v1.0.1 6/5/2025
Added main functionality of Get and Analyzing history of a team. Raw data for event data by year is not parsed at all so its all raw data from a singular event for now. Added the compare_teams function but is blank as I figure out how to best do it. There is NOW a main menu for using the tool. Maybe I'll make an interface too.


### v1.0.0 6/3/2025
Match Simulator works. Public Release.
