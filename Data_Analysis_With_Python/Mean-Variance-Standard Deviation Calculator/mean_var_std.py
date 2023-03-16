import numpy as np


def calculate(ls):
  if len(ls) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    data = np.array(
      [[ls[0], ls[1], ls[2]],
       [ls[3], ls[4], ls[5]],
       [ls[6], ls[7], ls[8]]])

  calculations = {
    'mean': [list(data.mean(axis=0)), list(data.mean(axis=1)), np.mean(data)],
    'variance': [list(data.var(axis=0)), list(data.var(axis=1)), np.var(data)],
    'standard deviation': [list(data.std(axis=0)), list(data.std(axis=1)), data.std()],
    'max': [list(data.max(axis=0)), list(data.max(axis=1)), data.max()],
    'min': [list(data.min(axis=0)), list(data.min(axis=1)), data.min()],
    'sum': [list(data.sum(axis=0)), list(data.sum(axis=1)), data.sum()]
  }

  return calculations