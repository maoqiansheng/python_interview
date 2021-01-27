

# with open('/Users/maoqiansheng/interview/interview_test.py', 'r') as f:
#     lines = len(f.readline())
# print(lines)

def block(file, size=65536):
    while True:
        nb = file.read(size)
        if not nb:
            break
        yield nb


def getLineCount(filename):

    with open(filename, "r", encoding="utf-8") as f:
        for line in block(f):
            lines = line.replace('\n', ',')
            list1 = lines.split(',')
            list2 = [int(x) for x in list1]
            top_10 = sorted(list2, reverse=True)[0:10]
        return top_10

        # return sum(line.count("\n") for line in block(f))


print(getLineCount('/Users/maoqiansheng/python_interview/text.txt'))



