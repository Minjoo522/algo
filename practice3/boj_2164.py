"""
다음의 행동을 카드가 1장 남을 때까지 반복한다
1. N 장의 카드 중 제일 위의 카드를 버린다
2. 제일 위에 있는 카드를 제일 밑으로 옮긴다
"""

from collections import deque

N = int(input())
cards = [i for i in range(1, N + 1)]
deque_cards = deque(cards)

while len(deque_cards) != 1:
    deque_cards.popleft()
    first = deque_cards.popleft()
    deque_cards.append(first)

print(*deque_cards)