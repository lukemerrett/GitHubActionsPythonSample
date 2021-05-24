import re

def convert_file_to_csv_using_regex_groups(
    grouping_regex, source_filename, destination_filename
):
    """
    Uses a regex containing groups to pull each line of a file into a csv.  Particularly useful for parsing log files
    :param grouping_regex: The regex containing a list of groups to pull out.
    :param source_filename: The file to pull the data from.
    :param destination_filename: The destination file to create.
    """
    if not isinstance(grouping_regex, str):
        raise TypeError("grouping_regex must be a string")

    if not isinstance(source_filename, str):
        raise TypeError("source_filename must be a string")

    if not isinstance(destination_filename, str):
        raise TypeError("destination_filename must be a string")

    if not re.match(r"\(\)", grouping_regex):
        raise RegexContainsNoGroups()

    compiled_regex = re.compile(grouping_regex)
    output_lines = []

    with open(source_filename, "r") as f:
        file_contents = f.readlines()

        for line in file_contents:
            parsed_groups = compiled_regex.match(line)
            if parsed_groups:
                line = ",".join(parsed_groups.groups())
                output_lines.append(line)

    with open(destination_filename, "w", newline="") as f:
        f.writelines(output_lines)

class RegexContainsNoGroups(Exception):
    """
    Exception raised when a provided regular expression contains no defined groups.
    """
    def __init__(self):
        super(RegexContainsNoGroups, self).__init__(
            "Provided grouping_regex does not contain any regex groups, e.g: (?'MyGroupName'.*)"
        )

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--groupingregex", dest="grouping_regex",
        help="Regular expression containing a set of groups showing how to extract the data from each line of the file.",
    )
    parser.add_argument(
        "--sourcefile",
        dest="source_filename", help="Location of the source file to extract the data from.",
    )
    parser.add_argument( "--destinationfile",
        dest="destination_filename",
        help="Where the resulting csv should be outputted to.",
    )
    args = parser.parse_args()

    convert_file_to_csv_using_regex_groups(
        args.grouping_regex,
                args.source_filename,
    args.destination_filename)