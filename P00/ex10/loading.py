import sys
import time

def ft_progress(lst):
    for i in lst:
        print("i = ", i)
        yield i

def main():
    # if len(sys.argv) == 1:
    #     ac = input("Give me a number please :\n")
    # elif (len(sys.argv) == 2):
    #     ac = argv[1]
    # else:
    #     print("Wrong number of arguments, try again")
    listy = range(10)
    ret = 0
    for elem in ft_progress(listy):
        print("crotte")
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)

if __name__ == "__main__":
    main()

sys.exit(1)


# import sys, time

# def ft_progress(lst):
#     start_time = time.time()
#     for i in range(len(lst)):
        
#         sys.stdout.write('\r')
#         sys.stdout.write("[%-20s] %d%%" % ('=' * int(20 * i / len(lst)), 1 * i / len(lst) * 100))
#         sys.stdout.write(" [%d/%d]" % (i, len(lst)))
#         sys.stdout.write(" elapsed time %d seconds" % (time.time() - start_time))
#         sys.stdout.flush()
#         yield i
#     i += 1
#     sys.stdout.write('\r')
#     sys.stdout.write("[%-20s] %d%%" % ('=' * int(20 * i / len(lst)), 1 * i / len(lst) * 100))
#     sys.stdout.write(" elapsed time %d seconds" % (time.time() - start_time))
#     sys.stdout.write(" [%d/%d]" % (i, len(lst)))


# def main():
#     listy = range(500)
#     ret = 0
#     for elem in ft_progress(listy):
#         ret += (elem + 3) % 5
#         time.sleep(0.01)
#     print()
#     print(ret)

# if __name__=="__main__":
#     main()