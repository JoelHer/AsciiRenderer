from twoDtoascii import calcMatrix, matToString
import numpy as np
import math
sin = math.sin
cos = math.cos
pi = math.pi

'''
Change the 'dots', line 35, to circle, pyramid, cube, or [] (to draw)
If you want to draw, change 'draw', line 36, to 1; please consider that more points equal worse performance; drawing happens on a fixed z, since the screen only gives x and y, so you can change this z on line 150 - 1 is standard
To change the drawing interval, change the number in line 166 (fps)or the modulus in line 146
To change rotation change the angles on lines 159 - 161 (radiants), for initial offset lines 25 - 27 (degrees)
'''

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# GREY = (100, 100, 100)


def rotate(mat, angx=0, angy=0, angz=0):
	rx = [
		[1, 0, 0],
		[0, cos(angx), -sin(angx)],
		[0, sin(angx), cos(angx)]
	]
	ry = [
		[cos(angy), 0, sin(angy)],
		[0, 1, 0],
		[-sin(angy), 0, cos(angy)]
	]
	rz = [
		[cos(angz), -sin(angz), 0],
		[sin(angz), cos(angz), 0],
		[0, 0, 1]
	]
	
	# offset
	mat = [mat[0] + 0, mat[1] + 0, mat[2] + 0]
	
	mat = np.dot(rx, mat)
	mat = np.dot(ry, mat)
	mat = np.dot(rz, mat)
	return mat
	

def rotTrue(mat, angx=0, angy=0, angz=0):
	rx = [
		[1, 0, 0],
		[0, cos(angx), sin(angx)],
		[0, -sin(angx), cos(angx)]
	]
	ry = [
		[cos(angy), 0, sin(angy)],
		[0, 1, 0],
		[-sin(angy), 0, cos(angy)]
	]
	rz = [
		[cos(angz), -sin(angz), 0],
		[sin(angz), cos(angz), 0],
		[0, 0, 1]
	]
	
	# offset
	mat = [mat[0] + 0, mat[1] + 0, mat[2] + 0]
	
	# mat = np.dot(mat, riyx)
	mat = np.dot(rz, mat)
	mat = np.dot(ry, mat)
	mat = np.dot(rx, mat)
	return mat	


def project(mat):
	pr = [
		[1, 0, 0],
		[0, 1, 0],
		[0, 0, 0]
	]
	
	mat = np.dot(mat, pr)
	return mat
	
# [[[a,b,c],[a,b,c]],[[a,b,c],[a,b,c]]]
def changeDim(matrix, scale, angx, angy, angz):
  res = []
  for line in matrix:
    respart = []
    for point in line: # always 2 points (should be)
      x, y, z = point[0] * scale, point[1] * scale, point[2] * scale
      rotated = rotTrue([x, y, z], angx, angy, angz)
      projected = project(rotated)
      respart.append([int(round(projected[0])), int(round(projected[1]))])
    res.append(respart)
  return res


def run(matrix, scale, num, angx=0, angy=0, angz=0):
  angx = angx / 180 * pi
  angy = angy / 180 * pi
  angz = angz / 180 * pi
  projcoords = changeDim(matrix, scale, angx, angy, angz)
  # print(projcoords)
  matrix = calcMatrix(projcoords, 40, 40)
  # string = matToString(calcMatrix(projcoords, 40, 40))
  # print(len(matrix), len(matrix[0]))
  return matrix