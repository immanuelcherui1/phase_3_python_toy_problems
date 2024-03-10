import random

def solution(N):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    num_letters = min(N, 26) 
    letter_count = N // num_letters
    remainder = N % num_letters


    random_letters = [random.choice(alphabet) for _ in range(num_letters)]


    result = ''.join(random.choice(random_letters) for _ in range(N))

    if remainder:
        result += random.choice(random_letters[:remainder])

    return result


N = 30
print(solution(N)) 
