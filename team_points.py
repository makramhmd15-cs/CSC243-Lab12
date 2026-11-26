def points_by_team(scores, teams):
    result = {}

    for team in teams:
        total = 0

        for player in teams[team]:
            total += scores[player]

        result[team] = total

    return result


def main():
    scores = {}
    teams = {}

    with open("players.txt", "r") as file:
        for line in file:
            if line.strip() == "":
                continue

            fields = line.split()

            name = fields[0]
            points = int(fields[1])
            team = fields[2]

            scores[name] = points

            if team not in teams:
                teams[team] = []

            teams[team].append(name)

    print("Scores:", scores)
    print("Teams:", teams)

    result = points_by_team(scores, teams)

    print("Points by team:", result)


main()
