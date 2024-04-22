f = open("student.csv", "r")
g = open("selected.csv", "w")

line = f.readline()
firstLine = True

while line:

    words = line.split(';')

    for i in range(len(words)):
        words[i] = words[i].strip('"')

        if (words[i] == 'F'):
            words[i] = "0"
        elif (words[i] == 'M'):
            words[i] = "1"
        elif (words[i] == 'U'):
            words[i] = "0"
        elif (words[i] == 'R'):
            words[i] = "1"
        elif (words[i] == "LE3"):
            words[i] = "0"
        elif (words[i] == "GT3"):
            words[i] = "1"
        elif (words[i] == 'A'):
            words[i] = "0"
        elif (words[i] == 'T'):
            words[i] = "1"
        elif (words[i] == "course"):
            words[i] = "0"
        elif (words[i] == "other"):
            words[i] = "1"
        elif (words[i] == "home"):
            words[i] = "2"
        elif (words[i] == "reputation"):
            words[i] = "3"
        elif (words[i] == "mother"):
            words[i] = "0"
        elif (words[i] == "father"):
            words[i] = "1"
        elif (words[i] == "no"):
            words[i] = "0"
        elif (words[i] == "yes"):
            words[i] = "1"

    words.pop(7)
    words.pop(7)

    if (not firstLine):
        if words[len(words)-1] and words[len(words)-2] and words[len(words)-3]:
            x = ((int(words[len(words)-1]) / 3) + (int(words[len(words)-2]) / 4) +
                 (int(words[len(words)-3]) / 4)) / 3
            if x > 5:
                x = 5
            if x < 1:
                x = 1

            x = str(int(round(x, 0)))
        else:
            x = ''  # Vagy valamilyen más alapértelmezett érték, ha az adat nem érvényes

        words.pop(len(words) - 1)
        words.pop(len(words) - 1)
        words.pop(len(words) - 1)

        words.append(x)
    else:
        words.pop(len(words) - 1)
        words.pop(len(words) - 1)
        words.pop(len(words) - 1)

        words.append("Result")

    line = ','.join(words) + '\n'

    g.write(line)

    line = f.readline()
    firstLine = False

f.close()
g.close()
