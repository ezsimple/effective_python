# %%
import subprocess
from time import sleep

def run_sleep(time):
    return subprocess.Popen(['sleep', str(time)])

proc = run_sleep(10000)

try:
	proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
	proc.terminate()
	proc.wait()

print('Exit status', proc.poll())
# %%
import threading
import time

# 공유 자원
shared_counter = 0
lock = threading.Lock()

def increment_counter():
    global shared_counter
    for _ in range(100000):
        # Lock을 획득
        lock.acquire()
        try:
            # 공유 자원 수정
            shared_counter += 1
        finally:
            # Lock을 해제
            lock.release()

start_time = time.time()  # 시작 시간 기록
# 스레드 생성
threads = []
for _ in range(10):  # 두 개의 스레드 생성
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

# 모든 스레드가 종료될 때까지 대기
for thread in threads:
    thread.join()

end_time = time.time()  # 종료 시간 기록
elapsed_time = end_time - start_time  # 경과 시간 계산

# 시, 분, 초, 밀리초로 변환
hours = int(elapsed_time // 3600)
minutes = int((elapsed_time % 3600) // 60)
seconds = int(elapsed_time % 60)
milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)

# 결과 출력
print(f"경과 시간: {hours}시간 {minutes}분 {seconds}초 {milliseconds}ms")
print("최종 카운터 값:", shared_counter)

# %%
import time
shared_counter = 0

def measure_time(task, *args, **kwargs):
    """지정된 작업(task)의 경과 시간을 측정하고 시, 분, 초, 밀리초로 표시합니다."""
    start_time = time.time()  # 시작 시간 기록

    # 지정된 작업 실행
    task(*args, **kwargs)

    end_time = time.time()  # 종료 시간 기록
    elapsed_time = end_time - start_time  # 경과 시간 계산

    # 시, 분, 초, 밀리초로 변환
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)

    # 결과 출력
    print(f"경과 시간: {hours}시간 {minutes}분 {seconds}초 {milliseconds}ms")

# 예시 작업 함수
def example_task():
    global shared_counter
    for _ in range(100000 * 10):
      shared_counter += 1
    
measure_time(example_task)
print("최종 카운터 값:", shared_counter)
# %%

import threading
from queue import Queue

# 공유 자원을 위한 Queue 생성
queue = Queue()

def increment_counter():
    for _ in range(100000):
        # Queue에 아이템 추가
        queue.put(1)

def worker():
    while True:
        try:
            # Queue에서 아이템 가져오기
            queue.get(timeout=1)  # 1초 동안 대기 후 timeout
            # 카운터 증가
            global shared_counter
            shared_counter += 1
            queue.task_done()  # 작업 완료 표시
        except:
            break  # Queue가 비어있으면 종료

# 공유 카운터 초기화
shared_counter = 0
start_time = time.time()  # 시작 시간 기록

# 스레드 생성
threads = []
for _ in range(10):  # 두 개의 스레드 생성
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

# 작업자가 Queue에서 작업을 수행하도록 하는 스레드 생성
worker_threads = []
for _ in range(2):  # 두 개의 작업자 스레드 생성
    worker_thread = threading.Thread(target=worker)
    worker_threads.append(worker_thread)
    worker_thread.start()

# 모든 스레드가 종료될 때까지 대기
for thread in threads:
    thread.join()

# Queue가 비어질 때까지 대기
queue.join()  # 모든 작업이 완료될 때까지 대기

for worker_thread in worker_threads:
    worker_thread.join()

end_time = time.time()  # 종료 시간 기록
elapsed_time = end_time - start_time  # 경과 시간 계산

# 시, 분, 초, 밀리초로 변환
hours = int(elapsed_time // 3600)
minutes = int((elapsed_time % 3600) // 60)
seconds = int(elapsed_time % 60)
milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)

# 결과 출력
print(f"경과 시간: {hours}시간 {minutes}분 {seconds}초 {milliseconds}ms")
print("최종 카운터 값:", shared_counter)
# %%
import nest_asyncio
import time

# nest_asyncio를 활성화
nest_asyncio.apply()

# 제너레이터 함수
def number_generator():
    n = 0
    while True:
        yield n
        n += 1

# 코루틴 함수
async def consume_numbers(gen):
    async for number in gen:
        if number >= 1000000:
            print(f"{number}, 종료합니다.")
            break  # 1,000,000에 도달하면 종료
        # print(f"소비된 숫자: {number}")
        # await asyncio.sleep(1)  # 비동기적으로 1초 대기

# 제너레이터를 비동기적으로 래핑하는 함수
async def async_generator(gen):
    while True:
        yield next(gen)

# 메인 코루틴
async def main():
    gen = number_generator()  # 제너레이터 생성
    async_gen = async_generator(gen)  # 제너레이터를 비동기적으로 래핑

    # 소비하는 코루틴 호출
    await consume_numbers(async_gen)

# 코루틴 실행
start_time = time.time()  # 시작 시간 기록

await main()

end_time = time.time()  # 종료 시간 기록
elapsed_time = end_time - start_time  # 경과 시간 계산

# 시, 분, 초, 밀리초로 변환
hours = int(elapsed_time // 3600)
minutes = int((elapsed_time % 3600) // 60)
seconds = int(elapsed_time % 60)
milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)

# 결과 출력
print(f"경과 시간: {hours}시간 {minutes}분 {seconds}초 {milliseconds}ms")

# %%
import concurrent.futures
import time

# 작업할 함수
def square(n):
    time.sleep(1)  # 작업 시뮬레이션을 위해 1초 대기
    return n * n

# 메인 함수
def main():
    numbers = [1, 2, 3, 4, 5]  # 처리할 숫자 목록

    # ProcessPoolExecutor를 사용하여 병렬 처리
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # 각 숫자에 대해 square 함수 실행
        results = list(executor.map(square, numbers))
    
    print("결과:", results)

# 실행
if __name__ == "__main__":
    main()
