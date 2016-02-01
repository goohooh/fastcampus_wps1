#주석은 수업시간에 이해한 내용을 단 주석입니다.
##2개의 주석을 단 경우는 이 후에 혼자 공부할때 내가 뭔가를 까먹을 때를 대비해서 예비용 설명을 내 식대로 써서 단 주석입니다.
class Empty(Exception):
    pass
#링크드 리스트는 배열과 다르게 Value값에 특정한 index가 존재 하지 않은 채 값들이 서로 링크로 연결되어있는 자료 구조를 말한다.
#그렇기 때문에 수정과 삭제를 할때 인덱스 번호에 맞춰서 Value들을 일일이 인덱스를 당겨서 맞출 필요 없이
#그냥 링크를 끊고 연결함을 통해서 데이터를 바꾸면 되기 때문에 수정 삭제에 용이하지만
#인덱스 값이 없어서 리스트 중 특정 Value를 찾고 싶으면 무조건 처음이나 끝에서 부터 수를 찾기 시작하여 일일이 도달할 때 까지
#가야 하기 때문에 장단점이 공존하는 자료구조입니다.
class LinkedList :
#거대한 리스트라는 클래스

    class _Node:#리스트 내에 선언된 '노드'를 만들어 내는 내부 클래스'
        #이것이 있음으로써 링크스택 클래스 내부에서 특정하게 쓰이는 클래스가 선언된 것이라고 볼 수 있다.
        ##노드 생성하는 클래스를 선언 함으로써 내부에서 노드를 만들어 구현합니다.

        def __init__(self, element, next=None):
            self._element = element#노드는 정보값과
            self._next = next#다음 노드를 가르키는 값을 갖는다.
        ##여기까지가 노드 클래스를 구연한 것입니다.
        ##노드클래스 안에는 노드의 속성값(element)와 다음 값을 보는 값(next)값을 갖습니다.

    ##밑의 함수는 linkedList의 생성자 함수 입니다. 생성자이기 때문에 클래스가 생성되자 마자 이 내부 함수에 선언된
    ##변수들은 모두 초기화가 됩니다.(그 이유는 바로 생성자 함수니까,,, 그게 이유입니다.)
    ##이 함수 안에는 자료구조 속의 맨 첫번째 값과 맨 마지막 값, 그리고 자료구조의 전체 크기 값을 소유하고 있습니다.
    ##하지만 현재는 초기화 상태입니다.(생성자 함수 내부에 있기 때문이지요)
    def __init__(self):
        self._head=None#링크드리스트 속 클래스 안에는 머릿부분을 가르키는 머릿값이 들어있다.
        self._size =0#이 리스트의 크기가 얼마인지도 알아야하기 때문에
        self._tail =None# 꼬릿값도 필요하다.

    ##이 함수는 함수의 전체 길이를 반환하는 함수 입니다.(len이 아니라 __len__으로 구현된 이유는 len이라는 메소드가
    ##이미 python내부에서 정의 되어 있기 때문에 그런것입니다.) 실제로 len으로 구현했다가는 기존에 내부 메소드로 정의
    ##되어 있는 len메소드는 자신의 속성을 잃어버리게 될 것입니다.
    def __len__(self):
        return self._size

    ##이 함수는 현재 자료 구조안에 있는 모든 자료들을 출력해주는 역할을 합니다.
    def print_list(self):
        probe = self._head#현재 첫번째 노드의 값(head)을 probe에 저장합니다.
        while probe is not self._tail:#이 head값이 꼬리값에 다다를 때 까지 반복문을 돌립니다.
            print(probe._element,'->',end='')#head값을 시작으로 element(Value가 저장됨)을 출력합니다.
            probe = probe._next #현재 probe에 저장된 노드의 다음값을 probe로 저장합니다.
        print(probe._element)

    def is_empty(self):#리스트가 비어있는지 확인하는 메소드입니다.(비어있으면 True)
        if self._size == 0:
            return True
        else :
            return False


    ##head노드 앞에 새로운 노드를 추가해 줍니다.
    ##" 여기에 추가 " -> (기존head노드) -> (next노드)
    def add_first(self, element):
        node = self._Node(element)#내부 클래스(node)를 만들어 node인스턴스를 생성합니다.111111111111111111111
        #노드에 새로운 값을 넣어주고
        if self._size == 0:#만약에 링크드리스트 안에 아무런 노드도 없을 경우에는
            self._head = node#머릿값에다가 새로 만든 노드를 넣어준다.
            self._tail = node#꼬릿값도 마찬가지다 어짜피 리스트 안에 노드가 한 개밖에 없어서 머리도, 꼬리도 된다.
            self._size+=1
        else:
            node._next = self._head##현재 head값을 새로 만든 노드의 다음(next)로 만들어버림
            self._head = node##이제부터 'node는 head이다'라고 선언해줌(혹시 헷갈릴까봐 써놓지만 여기 node는 새로 선언한거다11111111을 봐라)
            self._size+=1



    def add_last(self, element):
        node = self._Node(element)
        #노드에 새로운 값을 넣어주고
        if self._size == 0:
            self._head = node#머릿값에 새로운 노드를 넣어줌
            self._tail = node#꼬리도 마찬가지
            self._size+=1
        else :
            node._next = None
            self._tail._next = node#꼬리 부분에 있는 노드의 next는 새로 만든 노드!
            self._tail = node#이제 부터 꼬리는 새로만든 노드임
            self._size+=1

    ##head노드를 삭제합니다.
    def remove_first(self):
        if self._size==0:#노드에 아무것도 없으면 그냥 없다고 출력하면 됩니다.
            print("No Value")
        else:
            self._head = self._head._next
            self._size-=1

    def remove_last(self):
        if(self._size == 0):
            raise("error")

        elif(self._size == 1):
            self.remove_first()

        else:
            temp = self._head

            while(temp._next != self._tail):
                temp = temp._next


            self._tail = temp
            self._tail._next = None

    def head(self):
        return self._head._element
    def tail(self):
        return self._tail._element

lst = LinkedList()
print(lst.is_empty()) #True
lst.add_first(1)  #1
print(lst.head()) #return 1
lst.add_first(2)  #2->1
lst.add_first(3)  #3->2->1
#print(lst.tail()) #return 1
lst.print_list()
lst.add_last(4)  #3->2->1->4
lst.add_last(5)  #3->2->1->4->5
lst.add_last(6)  #3->2->1->4->5->6
lst.print_list()

lst.remove_first()  #2->1->4->5->6
lst.remove_last()  #2->1->4->5
lst.print_list()

#lst.print_list()  #2->1->4->5
#print(lst.is_empty()) #False
print(len(lst))  #return 4