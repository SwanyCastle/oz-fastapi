from fastapi import APIRouter
import time
import asyncio

router = APIRouter()

# async - 비동기 -> 비동기에서는 무거운 작업 하면 안됨
@router.get('/slow-async-ping')
def slow_async_ping():
    time.sleep(10)

    return {'msg': 'pong'}

@router.get('/fast-async-ping')
async def fast_async_ping():
    await asyncio.sleep(10) # REST API 호출, 무거운 작업 X -> EventLoop 를 잡아 먹기 때문에 (성능저하)

    return {'msg': 'pongpong'}

@router.get('/cpu-bound-async')
async def cpu_bound_async():
    result = await cpu_intensive_task()  # CPU 집약적 작업
    return {"result": result}

def cpu_intensive_task():
    # 예시: 피보나치 수열의 35번째 항을 계산하는 함수
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    # 피보나치 수열의 35번째 항 계산
    result = fibonacci(35)
    return result

# 이러한 무거운 작업들을 worker (threads같은 느낌) 개념이 등장함 (멀티로 처리)
from concurrent.futures import ProcessPoolExecutor

@router.get('/cpu-bound-task')
async def cpu_bound_task():
    # 여기서부터는 하나의 워커를 만들어서 따로 진행 하겠다는 뜻
    with ProcessPoolExecutor() as executor:
        result = await asyncio.get_event_loop().run_in_executor(executor, cpu_intensive_task)
        # TypeError: coroutines cannot be used with run_in_executor() 
        # ->  async def cpu_intensive_task(): run_in_executor() 함수 안에는 async 함수 들어가면 안됨

    return {'result': result}
