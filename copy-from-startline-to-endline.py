#!/usr/bin/python3

# method1
with open('/path/to/input') as infile, open('/path/to/output', 'w') as outfile:
    copy = False
    for line in infile:
        if line.strip() == "Start":
            copy = True
        elif line.strip() == "End":
            copy = False
        elif copy:
            outfile.write(line)


# method2
with open('input.txt') as myfile:
    content = myfile.read()

text = re.search(r'Start\n.*?End', content, re.DOTALL).group()

with open("output.txt", "w") as myfile2:
    myfile2.write(text)


# method3
import itertools
with open('input.txt', 'r') as f, open('output.txt', 'w') as fout:
    while True:
        it = itertools.dropwhile(lambda line: line.strip() != 'Start', f)
        if next(it, None) is None: break
        fout.writelines(itertools.takewhile(lambda line: line.strip() != 'End', it))


# other shell perl

sed -n '/Start/,/End/p' input.txt | grep -Ev '(Start|End)'

sed -e '1,/Start/d' -e '/End/,$d' input.txt

awk /Start/,/End/ input.txt | grep -Ev '(Start|End)'

awk '/Start/{flag=1;next} /End/{flag=0} flag{ print }' input.txt

awk '/End/{flag=0} flag; /Start/{flag=1}' input.txt

perl -lne 'print if((/Start/../End/) && !(/Start/||/End/))' input.txt









