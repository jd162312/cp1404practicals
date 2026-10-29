"""
Wimbledon
Estimate: 30 min
Actual: 38 min
"""
FILENAME = "wimbledon.csv"
CHAMPION_INDEX = 2
COUNTRY_INDEX = 1


def main():
    wimbledon_data = load_file()
    champion_to_count, countries = process_wimbledon_data(wimbledon_data)
    display_results(champion_to_count, countries)


def load_file():
    wimbledon_data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip()
            parts = line.split(",")
            wimbledon_data.append(parts)
    return wimbledon_data


def process_wimbledon_data(wimbledon_data):
    champion_to_count = {}
    countries = set()
    for record in wimbledon_data:
        countries.add(record[COUNTRY_INDEX])
        champion = record[CHAMPION_INDEX]
        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(champion, count)
    print()
    print(f"These {len(countries)} countries have won Wimbledon")
    print(", ".join(sorted(countries)))


main()
