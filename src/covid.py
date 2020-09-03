def symptoms():
    file = open('symptoms.txt', 'r')
    text = ''
    for i in file.readlines():
        text += i
    return text
        
def preventions():
    file = open('preventions.txt', 'r')
    text = ''
    for i in file.readlines():
        text += i
    return text