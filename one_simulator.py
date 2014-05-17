import subprocess


def run():
  returncode = subprocess.call(
    ["./one.sh", "-b",  "1"],
  )

  if int(returncode) != 0:
    raise 


def get_results_of_simulation(url):
  results = {}
  with open(url, 'r') as results_file:
    for line in results_file:
      # Remove newline from the line.
      if ":" in line:
        line = line.rstrip()
        kwd, v = line.split(":")
        v = v.strip()
        results[kwd] = v

  return results
