# https://school.programmers.co.kr/learn/courses/30/lessons/86971

"""
dfs xx => 시간초과 O(N**2)

✨ 위상 정렬 : 자동차 공정, 과정과 과정이 합쳐지고 합쳐져서 완성되는 거
화살표가 뒤로 돌아오지 않음
DAG(Directed Acyclic Graph) : 유방향 비순환 그래프
진입 차수가 0인 애들 = 시작

큐
1. 진입 차수가 0인 애들을 고른다(선행 공정이 없는 애들) ➡️ 시작 노드
2. pop(0)
3. destination에 해당하는 진입 차수를 하나 줄임
4. 줄면서 0이 되면 큐에 넣기

역행하는 경우는 없다!
https://www.acmicpc.net/problem/1005


중복된 노드를 방문하지 않도록(다시 돌아오지 않음)
✨ 진입 차수가 1인 애들을 찾는다(양방향 그래프)
"""


# 인접 리스트

def dfs(start_node, adj_list, n):
    visited = set()
    stack = [start_node]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)

            for destination in adj_list[current]:
                if destination not in visited:
                    stack.append(destination)

    return abs(len(visited) * 2 - n)


def solution(n, wires):
    answer = 101
    adj_list = [[] for _ in range(n + 1)]  # wire가 1부터 시작하므로

    for start, end in wires:
        adj_list[start].append(end)
        adj_list[end].append(start)

    for n1, n2 in wires:
        cut1 = adj_list[n1].pop(adj_list[n1].index(n2))
        cut2 = adj_list[n2].pop(adj_list[n2].index(n1))
        answer = min(answer, dfs(n1, adj_list, n))
        adj_list[cut1].append(cut2)
        adj_list[cut2].append(cut1)

    return answer