from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    if (sum(queue1) + sum(queue2)) % 2 == 1:
        return -1
    goal = (sum(queue1) + sum(queue2)) / 2
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    len1 = len(queue1)
    len2 = len(queue2)    
    
    limit = len1 * 4 
    while True :   
        if len1 == 0 or len2 == 0 or answer > limit:
            answer = -1
            return answer
        if sum1 == sum2 : 
            return answer        
        if sum1 > goal : 
            a = queue1.popleft()
            queue2.append(a) 
            sum1 -= a
            sum2 += a
            len1 -= 1
            len2 += 1
        elif sum2 > goal :  
            a = queue2.popleft()
            queue1.append(a)           
            sum2 -= a
            sum1 += a
            len2 -= 1
            len1 += 1
        answer += 1
        
     

queue1 = [3,2,7,1]
queue2 = [4,6,5,2]
answer = solution(queue1,queue2)
print(answer)



