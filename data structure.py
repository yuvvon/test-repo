#자료구조
#stack.py파일 참조<- 추상적자료형 구현파일 
#이진트리 활용 학생 조회 
class Student:
    def __init__(self, st_no, name, dept, grade, score=None):
        self.st_no = st_no
        self.name = name
        self.dept = dept  # 학과
        self.grade = grade  # 학년
        self.score = score  # 성적

    def return_student(self):
        if self.score == None:
            print(self.st_no, self.name, self. dept, self.grade)
        elif self.score != None:
            print(self.st_no, self.name, self. dept, self.grade, self.score)


class Node:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class Course:  # 수업
    def __init__(self):
        self.root = None
        self.size = 0
        self.deptList = []

    def register(self, num, name, dept, grade):
        Student(num, name, dept, grade)
        self.root = self._insertSubtree(
            self.root, num, Student(num, name, dept, grade))

    def _insertSubtree(self, node, key, value):
        if node == None:
            self.size += 1
            return Node(key, value)
        elif key < node.key:
            node.left = self._insertSubtree(node.left, key, value)
        elif key > node.key:
            node.right = self._insertSubtree(node.right, key, value)
        else:
            print("error1")
            pass
        return node

    def _minNode(self, node):
        if node.left == None:
            return node
        else:
            return self._minNode(node.left)

    def withdraw(self, num):    #
        self.size -= 1
        self.root = self._deleteSubtree(self.root, num)

    def _deleteSubtree(self, node, key):
        if node == None:
            self.size += 1
            print("error2")
            return None
        if key < node.key:    # 삭제할 키의 노드가 node의 왼쪽 부트리인 경우
            node.left = self._deleteSubtree(node.left, key)
            return node
        elif key > node.key:  # 삭제할 키의 노드가 node의 오른쪽 부트리인 경우
            node.right = self._deleteSubtree(node.right, key)
            return node
        else:                     # node가 삭제할 키의 노드인 경우
            if node.right == None:  # node의 오른쪽 자식노드가 없을 경우
                return node.left
            if node.left == None:    # node의 왼쪽 자식노드가 없을 경우
                return node.right
        rightMinNode = self._minNode(node.right)  # node의 오른쪽 부트리에서 최소키의 노드를 찾음
        # node의 오른쪽 부트리에서 최소키의 노드를 복사 node에 복사
        node.key = rightMinNode.key
        node.data = rightMinNode.data
        node.right = self._deleteSubtree(node.right, rightMinNode.key)
        return node

    def modify(self, num, new_score):
        node = self.root
        while node is not None:
            if num == node.key:
                node.data.score = new_score
                return
            elif num < node.key:
                node = node.left
            else:
                node = node.right
        print("error2")
        return

    def inquire(self, num):
        node = self.root
        while node is not None:
            if num == node.key:
                node.data.return_student()
                return
            elif num < node.key:
                node = node.left
            else:
                node = node.right
        print("error2")
        return None

    def print_studnet(self):
        print(self.size)
        if self.root is not None:
            self.inorder(self.root)

    def inorder(self, node):
        if node.left is not None:
            self.inorder(node.left)

        node.data.return_student()
        if node.right is not None:
            self.inorder(node.right)

    def print_deptStudnet(self, dept):
        self.deptList = []
        if self.root is not None:
            self.inorder_dept(self.root, dept)
        print(len(self.deptList))
        for i in range(len(self.deptList)):
            self.deptList[i].return_student()

    def inorder_dept(self, node, dept):
        if node.left is not None:
            self.inorder_dept(node.left, dept)

        if node.data.dept == dept:
            self.deptList.append(node.data)
        if node.right is not None:
            self.inorder_dept(node.right, dept)


# main 프로그램

clas = Course()

#무한루프문 사용
while True:
    command = input().split()
    if command[0] == 'N':
        clas.register(command[1], command[2], command[3], command[4])
    elif command[0] == 'C':
        clas.withdraw(command[1])
    elif command[0] == 'R':
        clas.inquire(command[1])
    elif command[0] == 'G':
        clas.modify(command[1], command[2])
    elif command[0] == 'D':
        clas.print_deptStudnet(command[1])
    elif command[0] == 'P':
        clas.print_studnet()
    elif command[0] == 'Q':
        break
