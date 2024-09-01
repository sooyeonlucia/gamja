def compare_lotto(answer, my_answer):
    bonus = answer[-1]
    count1 = 0
    for i in answer[:-1]:
        for j in my_answer:
            if i == j:
                count1 += 1
    
    count2 = int(bonus in my_answer)

    return [count1, count2]