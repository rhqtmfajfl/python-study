#이진 탐색 특정 데이터 정렬되고 있는 데이터에서 특정 데이터를 찾을 수 잇게 해준다.
#정렬되어 있

#이진 탐색 코드

#이진 탐색 소스코드 구현

def binary_search(array, target, start, end): #array 탐색 배열, target 찾고자 하는 숫자. start와 end 탐색범위
    if start > end:
        return None #start가 end 보다 크다면 찾고자 하는 숫자가 범위에 있다.

    mid = (start + end) //2

#찾은 경우 중간점 인덱스 반환
    if array[mid] == target: 
        return mid
#중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid -1)
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid +1, end)

    #n(원소의 개수)과 targert(찾고자 하는 문자열)을 입력 받기
    n, target = list(map(int, input().split()))

    #전체 원소 입력 받기
    array = list(map(int, input().split()))

    #이진 탐색 수행 결과 출력
    result = binary_search(array, target, 0, n-1)
    if result == None:
        print('원소가 존재하지 않습니다.')
    else:
        print(result +1)
        


































