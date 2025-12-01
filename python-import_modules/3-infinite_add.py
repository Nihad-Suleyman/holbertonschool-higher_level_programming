#!/usr/bin/python3
import sys
cnt = 0
if __name__ == "__main__":
    for i in range(0, len(sys.argv)):
        cnt += int(sys.argv[i])
    print("{}".format(cnt))
