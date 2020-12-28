size=int(input(""))
for i in range(size):
        print("%2d:"%i, end=" ")
        #오른쪽 직각삼각형은 size가 10인 경우, 1번라인에 1개, 2번라인에 2개, ..., 10번라인에 10개의 숫자가 있어야 하며, 숫자는 오른쪽으로 정렬되어야 한다.
        #즉, 숫자 오른쪽부터 채우기 위해 1번라인에 빈칸이 9개, 2번라인에 빈칸이 8개, ..., 10번라인에 빈칸이 0개가 위치해야한다.
        #따라서 j는 0부터 1씩 증가하다가 size-i가 되면 반복문을 종료한다. (1번라인의 빈칸 9개는 10-1, 2번라인의 빈칸 8개는 10-2, ...로 size-i이다.)
        for j in range(0,size-i,1):
            print(end="  ")
       
        #1번라인에 9개의 빈칸과 1개의 숫자를 채우는데, 빈칸은 위의 for문으로 채웠으므로 이번 for문에는 숫자를 써야한다.
        #1번라인에 1개의 숫자, 2번라인에 2개의 숫자...이렇게 채우다보면 i번 라인에는 i개의 숫자를 채워야한다.
        #이번엔 k는 i부터 시작해 1씩 작아지다 k가 -1이 되면 반복문을 종료한다. 
        #오른쪽 정렬효과를 주려면 큰 수가 먼저 출력되어야 하므로 range(0,i,1)이 아닌 (i,-1,-1)
        for k in range(i,-1,-1):      
            print(k, end=" ")
        #한 개의 라인에 빈칸과 숫자를 모두 적었으므로 다음 라인으로 넘어가기 위해 한줄을 띄운다.
        print()
        
