import sys

from fdroid_build_checker.fdroid_build_checker import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))
