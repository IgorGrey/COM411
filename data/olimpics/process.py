import tui

def list_year(data):
    tui.started("Following years:")
    years = set()
    for column in data:
        year = column[9]
        years.add(year)
    tui.display_years(years)
    tui.completed()

def tally_medals(data):
    tui.started("Tallying medals for each team")
    medals_count = {}
    for column in data():
        team = column(6)
        medal = column(9)

        if medal not in ("Gold", "Silver", "Bronze"):
            continue

        if team in medals_count:
            medals_count[team][medal] += 1
        else:
            medals_count[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            medals_count[team][medal] += 1

    tui.display_team_medal_tally(medals_count)
    tui.completed()

