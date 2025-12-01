#!/usr/bin/python3
import sys
if __name__ == "__main__":
    cnt = 0
    for i in range(1, len(sys.argv)):
        cnt += int(sys.argv[i])
    print("{}".format(cnt))
