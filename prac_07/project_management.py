import datetime

from project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    filename = "projects.txt"
    print("Welcome to Pythonic Project Management")
    projects = load_projects(filename)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename: ")
            projects = load_projects(filename)
        elif choice == "S":
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        print(MENU)
        choice = input(">>> ").upper()


def load_projects(filename):
    """Load projects from file"""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], datetime.datetime.strptime(parts[1], "%d/%m/%Y").date(), int(parts[2]),
                              float(parts[3]), int(parts[4]))
            projects.append(project)
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def save_projects(filename, projects):
    """Save projects to file."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime("%d/%m/%Y")}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)
    print(f"Saved {len(projects)} projects to {filename}")


def display_projects(projects):
    complete_projects = [project for project in projects if project.is_complete()]
    complete_projects.sort()
    incomplete_projects = [project for project in projects if not project.is_complete()]
    incomplete_projects.sort()
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)
    print("Completed projects:")
    for project in complete_projects:
        print(project)


def filter_projects_by_date(projects):
    date = input("Show projects that are after start date (dd/mm/yy): ")
    filtered_projects = [project for project in projects if project.start_date >
                         datetime.datetime.strptime(date, "%d/%m/%Y").date()]
    for project in filtered_projects:
        print(project)


main()
