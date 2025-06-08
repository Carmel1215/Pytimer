import time
import functools

def timer(func=None, *, ns=False):

    """
    함수 실행 시간을 측정하고 출력하는 데코레이터
    사용법:
    @timer          # ms 단위 출력
    @timer(ns=True) # ns 단위 출력
    :param ns:
    :return:
    """
    def decorator(inner_func):
        @functools.wraps(inner_func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter_ns if ns else time.perf_counter
            start = now()
            result = inner_func(*args, **kwargs)
            end = now()
            elapsed = end - start

            if ns:
                print(f"[ScriptTimer] {inner_func.__name__} 실행 시간: {elapsed} ns")
            else:
                print(f"[ScriptTimer] {inner_func.__name__} 실행 시간: {elapsed * 1000:.3f} ms" if now == time.perf_counter else f"[ScriptTimer] {inner_func.__name__} 실행 시간: {elapsed:.3f} ms")
            return result
        return wrapper

    return decorator if func is None else decorator(func)