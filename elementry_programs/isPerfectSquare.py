def isPerfectSqure(xmin,ymin,xmax,ymax):
	x = xmax - xmin
	y = ymax - ymin
	if x > y:
		if (y/float(x) > 0.8) and (y/float(x) <= 1.0) :
			return True
			
		else:
			return False

	else :
		if (x/float(y) > 0.8) and (x/float(y) <= 1.0) :
			return True
		else:
			return False


if __name__ == "__main__":
	l = [0, 2, 6, 6]
	if isPerfectSqure(l[0],l[1],l[2],l[3]):
		print("yes")
	else:
		print("no")