def solution(A):
    N = len(A)
    target = 10
    moves = 0
    total_bricks = sum(A)

    if total_bricks % N != 0 or total_bricks > 10 * N:
        return -1

    for i in range(N):
        if A[i] < target:
            diff = target - A[i]
            if i + 1 < N and A[i + 1] >= diff:
                A[i] += diff
                A[i + 1] -= diff
                moves += diff
            elif i + 1 >= N and A[i - 1] >= diff:
                A[i] += diff
                A[i - 1] -= diff
                moves += diff
            else:
                return -1
        elif A[i] > target:
            diff = A[i] - target
            if i + 1 < N and A[i + 1] <= target:
                A[i] -= diff
                A[i + 1] += diff
                moves += diff
            elif i + 1 >= N and A[i - 1] <= target:
                A[i] -= diff
                A[i - 1] += diff
                moves += diff
            else:
                return -1

    return moves

