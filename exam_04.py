# %%
import cProfile
import pstats
import io

# 프로파일링할 함수 정의
def slow_function():
    total = 0
    for i in range(1, 10000):
        for j in range(1, 100):
            total += i * j
    return total

# cProfile을 사용하여 slow_function을 프로파일링
def profile_function():
    pr = cProfile.Profile()
    pr.enable()  # 프로파일링 시작
    slow_function()  # 프로파일링할 함수 호출
    pr.disable()  # 프로파일링 종료

    # 결과를 Stats 객체에 저장
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    
    print(s.getvalue())  # 프로파일링 결과 출력

# 프로파일링 실행
profile_function()
