import sys

sys.path.insert(0, "../utils/py")
import utils


measure_time = utils.stopwatch()


@measure_time
def parse(raw_data):
    return [list(x) for x in raw_data.split("\n")]


# PART 1
@measure_time
def solve1(data):
    debug = False
    length = len(data)
    visible = 0
    for i in range(0,length):
        for j in range(0,length):
            if i % (length - 1)  != 0 and j % (length - 1) != 0:
                #print(i, j)
                tree = int(data[i][j])
                left = int(max(data[i][:j:]))
                right = int(max(data[i][j + 1::]))
                top = int(*max(*[[data[iidx][jidx] for jidx in range(0,length) if jidx == j] for iidx in range(0, i)]))
                down = int(*max(*[[data[iidx][jidx] for jidx in range(0,length) if jidx == j] for iidx in range(i + 1, length)]))
                if left < tree or right < tree or top < tree or down < tree:
                    visible += 1
                if debug:
                    print(f'tree: {tree},\tleft: {left},\tright: {right},\ttop: {top},\tdown: {down},\tVisible: {visible}')

    return visible + ((length * 4) - 4)


# PART 2
@measure_time
def solve2(data):
    pass


if __name__ == "__main__":
    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("\nTime taken:")
    for func, time in measure_time.times:
        print(f"{func:8}{time}s")
    print("----------------")
    print("total   {}s".format(sum(t for _, t in measure_time.times)))
