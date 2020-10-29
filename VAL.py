'''
平衡树
'''
import copy
import time


def cral_time(fun):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result =  fun(*args, **kwargs)
        end_time = time.time()
        print("执行时间：", end_time - start_time)
        return result
    return wrapper


@cral_time
def num_split(n):
    if n == 1:
        li_res = []
        li_res.append([1])
        return li_res
    else:
        li_res = [[1]]
        # print(len(li_res))
        for i in range(n - 1):
            li_zj = []
            for j in range(len(li_res)):
                dep_copy = copy.deepcopy(li_res[j])
                # li_res[j].append(1)
                # li_zj.append(li_res[j])
                # print(dep_copy)
                # print(li_zj)
                for k in range(len(li_res[j])):
                    dep_copy = copy.deepcopy(li_res[j])
                    dep_copy[k] += 1
                    dep_copy.sort(reverse=True)
                    if dep_copy not in li_zj:
                        li_zj.append(dep_copy)
                li_res[j].append(1)
                li_zj.append(li_res[j])
            li_res = li_zj
        return li_res


res = num_split(31)
res.sort(key=lambda x: len(x))
print(len(res))
print(res)
