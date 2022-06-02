import sys #sys참조


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def push(self, e):
        self.items.append(e)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print('Stack is empty')

    def size(self):
        return len(self.items)

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.items[-1]


def parenthesesBalance(list):

    s = Stack() #스택선언
    
    index = Stack()
    line = Stack()
    openParenthesis = '({['  # openParenthesis = ('(','{','[')
    closeParenthesis = ')}]'
    for i in range(1, len(list)+1):
        count = 1
        for ch in list[i-1]:

            if ch in openParenthesis:  # if ch == '(' or ch == '{' or ch == '['
                s.push(ch)
                index.push(count)
                line.push(i)
            elif ch in closeParenthesis:
                if s.isEmpty():
                    if(ch == ')'):
                        print("error 1: ) at position", count, "in line", i)
                        return False
                    if(ch == '}'):
                        print("error 2: } at position", count, "in line", i)
                        return False
                    if(ch == ']'):
                        print("error 3: ] at position", count, "in line", i)
                        return False

                else:
                    openCh = s.pop()
                    if (ch == ')' and openCh != '('):
                        print("error 1: ) at position", count, "in line", i)
                        return False
                    elif(ch == '}' and openCh != '{'):
                        print("error 2: } at position", count, "in line", i)
                        return False
                    elif (ch == ']' and openCh != '['):
                        print("error 3: ] at position", count, "in line", i)
                        return False
                    line.pop()
                    index.pop()
            count += 1

    if s.isEmpty():
        return s.isEmpty()
    else:
        a = s.pop()
        b = index.pop()
        c = line.pop()+1
        if (a == '('):
            print("error 4: ( at position", b, "in line", c)
            return False
        elif (a == '{'):
            print("error 5: { at position", b, "in line", c)
            return False
        elif (a == '['):
            print("error 6: [ at position", b, "in line", c)
            return False


str = sys.stdin.readlines()
while True:
    for i in range(len(str)):
        str[i] = str[i].strip()


    if parenthesesBalance(str):
        print("성공")
        break
    else:
        print("실패,다시 입력하세요")
