import csv
from sys import argv
from sys import exit


def main():

    # TODO: Check for command-line usage
    if len(argv) != 3:
        exit("Usage: python dna.py databases/large.csv sequences/5.txt")

    # TODO: Read database file into a variable
    database = []
    file = open(argv[1], "r")
    file_reader = csv.DictReader(file)
    for row in file_reader:
        database.append(row)
    file.close()
    # TODO: Read DNA sequence file into a variable
    file = open(argv[2], "r")
    dna_reader = file.read()
    file.close()
    # TODO: Find longest match of each STR in DNA sequence
    subsequences = list(database[0].keys())[1:]

    result = {}
    for subsequence in subsequences:
        result[subsequence] = longest_match(dna_reader, subsequence)
    # TODO: Check database for matching profiles
    for person in database:
        match_count = 0
        for subsequence in subsequences:
            if int(person[subsequence]) == result[subsequence]:
                match_count += 1
        if match_count == len(subsequences):
            print(person['name'])
            return
    print("No match")

    
def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
