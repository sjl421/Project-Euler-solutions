# 
# Solution to Project Euler problem 7
# by Project Nayuki
# 
# http://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 

import eulerlib


def compute():
	n = 2
	count = 0
	while True:
		if eulerlib.is_prime(n):
			count += 1
			if count == 10001:
				break
		n += 1
	return str(n)


if __name__ == "__main__":
	print(compute())
