#!/usr/bin/env python3

# Import modules we need
    # What should we import to get the job(s) done?
import argparse # Definitely need a module like argparse if we want to supply arguments--f

# Rule: Does every file have an extension?
# Rule: Every file is at least zero bytes
# Rule: There are no hidden files here
# Rule: No filename has any sort of whitespace
    # What input does this need?
    # What should the output be?

# Output report
    # What input should this get to produce a report?
    # Does it produce the whole report or does it output line by line?

# Main function
def validator():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--directory", help="Path to input directory.")
    parser.add_argument("-o","--output", help="Path to and filename for output file. If unused, output will be to stdout")
    args = parser.parse_args()

    if args.directory:
        inputDir = args.directory
    if args.output:
        outputFile = args.output

    # Some things we might want to do here:
        # Gather and check user input
        # Set up output filename (see if we're overwriting anything?)
        # Get a list of files we're working with
        # Run some rules and get feedback
        # Generate a report
    # Other things to think about
        # How should we handle unexpected input?
        # How do we write/run tests on this?

if __name__ == '__main__':
    validator()
