import re


def obj_to_list(obj_file):
  vertices = []
  with open(obj_file, 'r') as file:
    for line in file:
      if line.startswith('v '):
        vertex = [float(x) for x in re.findall(r"[-+]?\d*\.\d+|\d+", line)]
        vertices.append([
          vertex[0] / max(vertices)[0], vertex[1] / max(vertices)[1],
          vertex[2] / max(vertices)[2]
        ])
  return vertices
