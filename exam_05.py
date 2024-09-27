import tracemalloc

# 메모리 추적 시작
tracemalloc.start()

def memory_leak_function():
    # 대량의 데이터를 생성하여 메모리를 차지함
    data = [i for i in range(100000)]
    return data

# 메모리 사용 현황 추적
def profile_memory():
    snapshot1 = tracemalloc.take_snapshot()  # 초기 스냅샷
    memory_leak_function()  # 메모리 사용 함수 호출
    snapshot2 = tracemalloc.take_snapshot()  # 함수 호출 후 스냅샷

    # 스냅샷 비교
    top_stats = snapshot2.compare_to(snapshot1, 'lineno')

    print("[ Top memory blocks ]")
    for stat in top_stats[:10]:  # 상위 10개 메모리 블록 출력
        print(stat)

# 메모리 프로파일링 실행
profile_memory()

# 메모리 추적 종료
tracemalloc.stop()
