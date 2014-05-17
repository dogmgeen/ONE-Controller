import itertools
from settings import get_settings
from settings import write_settings
import time
from one_simulator import run
from one_simulator import get_results_of_simulation
import os
import csv


TTLs = range(20, 340, 20)
BUFFER_SIZES = range(100, 1800, 100)
NAME = "Epidemic_b{bufferSize}_ttl{ttl}"


def write_out_csv(results):
  with open("results.csv", "w") as f:
    writer = csv.DictWriter(f, results[0].keys())
    writer.writeheader()
    writer.writerows(results)


# Iterate through permutations of TTL and buffer size.
results = []
n = len(TTLs) * len(BUFFER_SIZES)
i = 0

for ttl, bufferSize in itertools.product(TTLs, BUFFER_SIZES):
  i += 1
  start = time.time()
  print(
    "Completion := {0:.0%}\n"
    "TTL := {1}\n"
    "BUF := {2}\n".format(float(i)/n, ttl, bufferSize)
  )
  scenarioName = NAME.format(bufferSize=bufferSize, ttl=ttl)

  # Feed pair into settings generator.
  settings = get_settings(
    size_in_bytes=bufferSize,
    ttl=ttl,
    scenario_name=scenarioName
  )
  write_settings(settings)

  # Run the ONE simulation.
  try:
    run()

  except:
    print("Problem with TTL := {0}, BUF := {1}".format(ttl, bufferSize))

  else:
    # Grab the results from the simulation and append to a single file.
    results_from_sim = get_results_of_simulation(
      os.path.join(
        "reports",
        "{scenarioName}_MessageStatsReport.txt".format(
          scenarioName=scenarioName
        )
    ))
    duration = int(time.time() - start)
    results_from_sim.update({
      "TTL": ttl,
      "bufferSize": bufferSize,
      "RunningTime": duration
    })
    results.append(results_from_sim)
    print("Done! {0} seconds".format(duration))

write_out_csv(results)

