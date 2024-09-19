import time

word = "postgrab" * 1000

# [::-1] 방식
start = time.time()
for _ in range(10000):
    reversed_word = word[::-1]
end = time.time()
print(f"슬라이싱 방식: {end - start:.5f}초")

# list.reverse() 방식
start = time.time()
for _ in range(10000):
    reversed_word = reversed(list(word))
end = time.time()
print(f"리스트 변환 방식: {end - start:.5f}초")
