#!/usr/bin/env python3

import argparse
import os
import re

def process_gff_file(input_file, output_file):
    """
    Process a GFF file according to the specified requirements:
    1) Remove lines starting with #
    2) Create output with 9 columns: gene_callers_id, contig, start, stop, direction, 
       partial, call_type, source, version
    3) Assign unique integer IDs starting from 1
    4) Map columns appropriately from input to output
    """
    gene_caller_id = 1
    
    # Open the input and output files
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Write header line with additional columns
        outfile.write("gene_callers_id\tcontig\tstart\tstop\tdirection\tpartial\tcall_type\tsource\tversion\n")
        
        # Process each line in the input file
        for line in infile:
            # Skip lines starting with #
            if line.startswith('#'):
                continue
            
            # Split the line by tabs
            fields = line.strip().split('\t')
            
            # Make sure we have enough fields
            if len(fields) < 8:
                print(f"Warning: Skipping line with insufficient fields: {line.strip()}")
                continue
            
            # Extract values
            contig = fields[0]
            
            # Extract source and version from column 2
            source_version = fields[1].split('_', 1)  # Split on first _
            if len(source_version) == 2:
                source = source_version[0]
                version = source_version[1]
            else:
                source = fields[1]
                version = ""
            
            feature_type = fields[2]
            start = fields[3]
            stop = fields[4]
            last_column = fields[8] if len(fields) > 8 else ""
            
            # Determine direction
            if fields[6] == '+':
                direction = 'f'
            else:
                direction = 'r'
            
            # Determine partial value
            partial = 0 if "partial=00" in last_column else 1
            
            # Determine call_type value
            call_type = 1 if feature_type == "CDS" else 2
            
            # Write the reformatted line with additional columns
            outfile.write(f"{gene_caller_id}\t{contig}\t{start}\t{stop}\t{direction}\t{partial}\t{call_type}\t{source}\t{version}\n")
            
            # Increment gene caller ID
            gene_caller_id += 1

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Reformat GFF file to custom format')
    parser.add_argument('input_file', help='Input GFF file')
    parser.add_argument('-o', '--output', help='Output file name')
    
    # Parse arguments
    args = parser.parse_args()
    
    # If output file is not specified, create default name
    if args.output is None:
        base_name = os.path.splitext(args.input_file)[0]
        args.output = f"{base_name}_reformatted.txt"
    
    # Process the file
    process_gff_file(args.input_file, args.output)
    print(f"Processing complete. Output written to: {args.output}")

if __name__ == "__main__":
    main()
