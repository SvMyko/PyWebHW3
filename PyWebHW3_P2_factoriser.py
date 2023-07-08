from multiprocessing import Pool, cpu_count
import time

# Execution Time (Parallel): 0.5539989471435547 seconds
def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(*numbers):
    pool = Pool(cpu_count())
    results = pool.map(factorize, numbers)
    pool.close()
    pool.join()
    return results

if __name__ == '__main__':
    start_time = time.time()
    a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)
    end_time = time.time()

    execution_time_parallel = end_time - start_time
    print("Execution Time (Parallel):", execution_time_parallel, "seconds")

    print("Results:")
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)


# Execution Time (Synchronous): 0.3276998996734619 seconds
# import time
#
# def factorize(number):
#     factors = []
#     for i in range(1, number + 1):
#         if number % i == 0:
#             factors.append(i)
#     return factors
#
# if __name__ == '__main__':
#     start_time = time.time()
#     a, b, c, d = factorize(128), factorize(255), factorize(99999), factorize(10651060)
#     end_time = time.time()
#
#     execution_time_sync = end_time - start_time
#     print("Execution Time (Synchronous):", execution_time_sync, "seconds")
#
#     print("Results:")
#     print("a:", a)
#     print("b:", b)
#     print("c:", c)
#     print("d:", d)
