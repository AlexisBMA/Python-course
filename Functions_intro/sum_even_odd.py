def sum_eo(n: int, t: str) -> int:
    answer = 0
    if 'e' in t:
        for num in range(0, n, 2):
            answer = answer + num
    elif 'o' in t:
        answer = 0
        for num in range(1, n, 2):
            answer = answer + num
    else:
        return -1
    return answer


print(sum_eo(7, 'o'))
