def main():
    records = []

    # Part 2.a: Reading records
    try:
        with open("scores.txt", "r") as file:
            for line in file:
                fields = line.strip().split(",")

                name = fields[0]

                try:
                    score = int(fields[1])
                except ValueError:
                    continue

                records.append([name, score])

    except FileNotFoundError:
        print("File not found.")
        return

    # Find Karim's score
    for record in records:
        if record[0] == "Karim":
            print(record[1])

    # Count valid scores
    print(len(records))

    # Part 2.b: Updating the scoreboard
    updated_records = []

    for record in records:
        if record[0] == "Maya":
            record[1] = 88

        if record[0] != "Nour":
            updated_records.append(record)

    # Write updated scores.txt
    with open("scores.txt", "w") as file:
        for record in updated_records:
            file.write(record[0] + "," + str(record[1]) + "\n")

    # Write pass.txt
    with open("pass.txt", "w") as file:
        for record in updated_records:
            if record[1] >= 60:
                file.write(record[0] + "\n")


main()
