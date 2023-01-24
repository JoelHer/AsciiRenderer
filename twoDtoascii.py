import json
def makeMatrix(x, y):
  res = [[' ' for x in range(x)] for y in range(y)]
  return res
	
def matToString(matrix):
  string = ','
  
  for j in range(len(matrix[0])):
    string += '_'
  string += ',\n|'
  
  for ly in matrix:
    for lx in ly:
      string += lx
    string += '|\n|'
  
  for i in range(len(matrix[0])):
    string += '_'
  
  string += '|'
  return string


def stringToMat(string):
  # layer1.replace(',', '')
  # layer1.replace('[', '')
  # layer1.replace(']', ';')
  layer1 = json.loads(string)
  return layer1
      

def calcMatrix(input, width, height):
  matrix = makeMatrix(width, height)
  for line in input:
    x1, y1 = line[0][0] + int(width / 2), line[0][1] + int(height / 2)
    x2, y2 = line[1][0] + int(width / 2), line[1][1] + int(height / 2)
    y1, y2 = -y1, -y2
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    # print(dx, dy)
    if dx > dy: # check if x dist is greater than y dist
    	if x1 < x2:
    		for x in range(dx):
    			x += x1
    			y = round(((y1 - y2) * (x - x1)) / (x1 - x2) + y1)
    			try:
    				matrix[y][x] = '#'
    			except:
    				print('error')
    	else:
    		for x in range(dx):
    			x += x2
    			y = round(((y1 - y2) * (x - x1)) / (x1 - x2) + y1)
    			try:
    				matrix[y][x] = '#'
    			except:
    				print('error')
    else:
      if y1 < y2:
      	for y in range(dy):
        	y += y1
        	x = round(((x1 - x2) * (y - y1)) / (y1 - y2) + x1)
        	try:
        		matrix[y][x] = '#'
        	except:
        		print('error')
      else:
      	for y in range(dy):
        	y += y2
        	x = round(((x1 - x2) * (y - y1)) / (y1 - y2) + x1)
        	try:
        		matrix[y][x] = '#'
        	except:
        		print('error')
  return matrix

# print(matToString(calcMatrix(input)))
# This will be output on Discord right?