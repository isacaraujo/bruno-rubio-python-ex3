def read_edges():
  input_file  = open('input1.txt', 'r')
  input_data  = input_file.read()
  input_list  = input_data.split("\n")
  return_list = []

  for input_row in input_list:
    row_params = input_row.split(' ')

    if len(row_params) != 3:
      break

    u = int(row_params[0])
    v = int(row_params[1])
    x = int(row_params[2])

    if u < 0 or v < 0:
      break

    if u >= v:
      break

    edge = {
      'u': u,
      'v': v,
      'x': x,
    }
    return_list.append(edge)

  return return_list

def extract_values_from_list_of_dict(list, key):
  retval = []
  for item in list:
    retval.append(item[key])
  return retval

def min(list):
  minimum = None
  for n in list:
    if minimum == None or n < minimum:
      minimum = n
  return minimum

def max(list):
  maximum = None
  for n in list:
    if maximum == None or n > maximum:
      maximum = n
  return maximum

def get_vertices_count(edges_list):
  vertices = extract_values_from_list_of_dict(edges_list, 'v')
  return max(vertices) + 1

if __name__ == "__main__":
  edges_list = read_edges()
  vertices_count = get_vertices_count(edges_list)

  print edges_list
  print vertices_count
