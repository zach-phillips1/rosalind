################
# Problem
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
# Given: A DNA string s
# of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
################

file_path = "rosalind_dna.txt"

try:
    with open(file_path, 'r') as file:
        line = file.readline()
except FileNotFoundError:
    print(f"The file at '{file_path}' was not found.")
except Exception as e:
    print(f"An error occured: ")

line_cleaned = line.strip()

a_count, c_count, g_count, t_count = 0,0,0,0

for char in line:
    match char:
        case "A":
            a_count+=1
        case "C":
            c_count+=1
        case "G":
            g_count+=1
        case "T":
            t_count+=1
        case _:
            break

print(f"{a_count} {c_count} {g_count} {t_count}")