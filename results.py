FILE = "results.csv"
import csv


def get(x_kwd, y_kwd, z_kwd):
  x = []
  y = []
  z = []
  with open(FILE, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
      x.append(float(row[x_kwd]))
      y.append(float(row[y_kwd]))
      z.append(float(row[z_kwd]))
  return x, y, z
