import datetime

from project import Project


def main():
    projects = load_projects("projects.txt")
    # for line in projects:
    #     print(line)


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
    return projects


main()
