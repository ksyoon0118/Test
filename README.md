# 과제3

# top
top명령어는 현재 os의 상태를 알려주는 명령어이다.
top명령어를 사용하면 먼저 요약영역에 시간, 유저, 로드 에버리지(Load Average), 테스크(Tasks), CPU, 메모리(memory) 등에 대한 정보가 나온다.
다음으로 디테일 영역에는 각 프로세스에 대한 상세한 내용이 나온다. 프로세스 ID인 PID, USER의 이름, 메모리와 관련된 VIRT, RES, SHR, %MEM 등의 내용이 차례대로 나온다.
# ps
ps 명령어는 Process State의 약자로 현재 실행 중인 프로세스와 상태를 출력하는 명령어이다. 주로 grep과 많이 사용된다.
ps 명령어는 USER,PID,PPID,%CPU,%MEM,VSZ(가상 메모리 사용량),RSS(실제 메모리 사용량),TTY(프로세스와 연결된 터미널),TIME,COMMAND,STIME,F(플래그),PRI(실제 실행 우선순위) 등을 출력한다.
# jobs
jobs는 job의 목록을 확인하는 명령어로 여기서 job이란 셀에서의 처리 단위를 말한다. $ job -l을 사용하면 프로세스 ID가 함께 출력된다.
# kill
kill은 프로세스 종료 명령어로  $ kill <프로세스 ID> 의 형식으로 사용한다. 다른사용자가 실행중인 프로세스는 함부로 종료할 수 없다는 점을 유의해야한다.
