# 1. 자료구조 기초 (스택, 큐)
</br>

탐색 문제 유형을 풀기 위해서는 자료구조인 스택과 큐에 대한 이해가 필요하다.

## 1.1. 스택(Stack)
</br>

스택은 **후입선출(LIFO)** 구조로, 파이썬에서 스택을 이용할 때는 별도의 라이브러리를 사용할 필요가 없다. 기본 리스트에서 **append()** 와 **pop()** 메서드를 이용하면 스택 자료구조와 동일하게 동작한다.
</br>
</br>

### 스택 예제
![스택1](https://user-images.githubusercontent.com/69297345/148477172-ceb64d98-f7e0-4cca-bd15-eba9f6a4e63b.PNG)
![스택2](https://user-images.githubusercontent.com/69297345/148477174-67db54ee-b46a-4ab5-9a11-f52d7760997b.PNG)
</br>
</br>

### 스택 예제 파이썬 코드
```python
    stack = []

    stack.append(5)
    stack.append(2)
    stack.append(3)
    stack.append(7)
    stack.pop()
    stack.append(1)
    stack.append(4)
    stack.pop()
    
    print(stack) # 최하단 원소부터 출력
    print(stack[::-1]) # 최상단 원소부터 출력


    ## 출력결과
    # [5, 2, 3, 1]
    # [1, 3, 2, 5]

```
</br>
</br>
</br>

### 1.2. 큐(Queue)
</br>

큐는 **선입선출(FIFO)** 구조로, 파이썬으로 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용한다. (queue 라이브러리보다 입출력 속도 빠르고 효율적이기 때문) 또한 deque 객체를 리스트 자료형으로 변경하고자 한다면 list(queue)를 하면 리스트로 반환된다.
</br>
</br>

### 큐 예제
![큐1](https://user-images.githubusercontent.com/69297345/148478347-34bcb208-ead5-490f-bb93-765a10ca9b03.PNG)
![큐2](https://user-images.githubusercontent.com/69297345/148478361-a819ad06-fe54-4c63-a64f-d2b7f92fabba.PNG)
</br>
</br>

### 큐 예제 파이썬 코드
```python
    from collections import deque # deque 라이브러리 사용

    queue = deque() 

    queue.append(5)
    queue.append(2)
    queue.append(3)
    queue.append(7)
    queue.popleft()
    queue.append(1)
    queue.append(4)
    queue.popleft()

    print(queue)
    queue.reverse # 역순으로 바꾸기
    print(queue)

    ## 출력 결과
    # deque([3, 7, 1, 4])
    # deque([4, 1, 7, 3])

```
</br>
</br>
</br>

# 2. DFS/BFS
</br>

## 2.1. DFS
</br>

DFS(깊이 우선 탐색)은 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘으로 **스택** 자료구조를 이용한다.
</br>

- **동작과정**
1. 탐색 시작 노드를 스택에 삽입하고 방문처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접노드를 스택에 넣고 방문 처리를 하고, 없으면 최상단 노드를 꺼낸다.
3. 두번째 과정을 더 이상 수행할 수 없을 때까지 반복한다.

그래프는 **노드(node)** 와 **간선(edge)** 로 표현되며 이때 노드를 **정점(vertex)** 라고도 말한다. 또한 두 노드가 간선으로 연결되어 있다면 '두 노드는 인접하다' 라고 표현한다.
</br>

- **인접 행렬(Adjacency Matrix)** : 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식. 연결되지 않은 노드끼리는 무한의 비용이라고 작성한다. (실제 코드에서는 999999999 등 사용)
</br>

![인접행렬](https://user-images.githubusercontent.com/69297345/148480226-b2c06c1c-4e1b-4c4b-b36f-0e430c436ed7.PNG)
</br>

**파이썬 코드**
```python
    INF = 999999999 # 무한의 비용 

    graph = [
        [0, 7, 5],
        [7, 0, INF],
        [5, INF, 0]
    ]

```



- **인접 리스트(Adjacency List)** : 모든 노드에 연결된 노드에 대한 정보를 연결 리스트에 차례대로 연결하여 저장하는 방식. 파이썬에서는 2차원 리스트를 이용하면 된다.
</br>

![인접리스트](https://user-images.githubusercontent.com/69297345/148480241-6650d056-7bcd-43da-a565-c7f4970e3d28.PNG)
</br>

**파이썬 코드**
```python
    # 3행의 2차원 리스트로 인접 리스트 표현
    graph = [[] for _ in range(3)]

    graph[0].append((1, 7))
    graph[0].append((2, 5))

    graph[1].append((0, 7))

    graph[2].append((0, 5))

```
</br>
</br>

### 2.1.1. 인접 행렬과 인접 리스트의 차이점
</br>

인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을수록 메모리 낭비가 크다. 인접 리스트 방식은 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용한다. </br>
이와 같은 속성 때문에 인접 리스트 방식은 인접 행렬 방식에 비해 정보를 얻는 속도가 느리다.
</br>
</br>

## 2.1. BFS
</br>

BFS(너비 우선 탐색)은 가까운 노드부터 탐색하는 알고리즘으로 **큐** 자료구조를 이용한다.  수행시간은 **0(N)** 이며 일반적인 경우 DFS보다 수행시간이 빠른 편이다.
</br>

- **동작** 과정
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. 두번째 과정을 더 이상 수행할 수 없을 때까지 반복한다.