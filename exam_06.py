import tracemalloc

# 메모리 추적 시작
tracemalloc.start()

def memory_leak_generator():
    # 대량의 데이터를 제너레이터로 생성
    for i in range(100000):
        yield i

# 메모리 사용 현황 추적
def profile_memory():
    snapshot1 = tracemalloc.take_snapshot()  # 초기 스냅샷
    generator = memory_leak_generator()  # 제너레이터 생성
    for value in generator:  # 제너레이터에서 값 사용
        pass  # 실제로 사용할 수 있는 부분 (여기서는 단순히 패스)
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
