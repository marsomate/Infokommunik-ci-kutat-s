def transform_data(words):
    """Transforms the data according to specified rules."""
    for i in range(len(words)):
        words[i] = words[i].strip('"')

        # Mapping categorical values to numerical values
        if words[i] == 'F':
            words[i] = "0"
        elif words[i] == 'M':
            words[i] = "1"
        elif words[i] == 'U':
            words[i] = "0"
        elif words[i] == 'R':
            words[i] = "1"
        elif words[i] == "LE3":
            words[i] = "0"
        elif words[i] == "GT3":
            words[i] = "1"
        elif words[i] == 'A':
            words[i] = "0"
        elif words[i] == 'T':
            words[i] = "1"
        elif words[i] == "course":
            words[i] = "0"
        elif words[i] == "other":
            words[i] = "1"
        elif words[i] == "home":
            words[i] = "2"
        elif words[i] == "reputation":
            words[i] = "3"
        elif words[i] == "mother":
            words[i] = "0"
        elif words[i] == "father":
            words[i] = "1"
        elif words[i] == "no":
            words[i] = "0"
        elif words[i] == "yes":
            words[i] = "1"

    return words


def calculate_result(words):
    """Calculates the result based on the given scores."""
    if words[-1] and words[-2] and words[-3]:
        average_score = (
            (int(words[-1]) / 3) + (int(words[-2]) / 4) + (int(words[-3]) / 4)) / 3

        # Ensuring the result falls within the valid range
        if average_score > 5:
            average_score = 5
        elif average_score < 1:
            average_score = 1

        return str(int(round(average_score, 0)))
    else:
        return ''  # Or any other default value if the data is invalid


def process_file(input_file, output_file):
    """Processes the input file and writes the transformed data to the output file."""
    with open(input_file, "r") as f, open(output_file, "w") as g:
        first_line = True
        for line in f:
            words = line.split(';')
            words = transform_data(words)

            if not first_line:
                result = calculate_result(words)
                words.pop(-1)
                words.pop(-1)
                words.pop(-1)
                words.append(result)
            else:
                words.pop(-1)
                words.pop(-1)
                words.pop(-1)
                words.append("Result")
                first_line = False

            line = ','.join(words) + '\n'
            g.write(line)


# Function calls
process_file("student.csv", "selected.csv")
