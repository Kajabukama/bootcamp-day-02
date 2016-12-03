# a function to determine the maximum and minimum value
# in a list and return the value in an array [min, max]

def find_max_min(alist):
	res = []
	minv = None
	maxv = None
	
	minv = min(alist)
	maxv = max(alist)

	if minv == maxv:
		res.append(minv)
		return res
	else:
		res.append(minv)
		res.append(maxv)
		return res

print find_max_min([4, 66, 6, 44, 7, 78, 8, 68, 2])