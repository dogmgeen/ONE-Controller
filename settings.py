def get_settings(size_in_bytes, ttl, scenario_name):
  with open("settings.template", "r") as f:
    settings_raw = f.read().format(
      size_in_bytes=size_in_bytes,
      ttl=ttl,
      scenario_name=scenario_name
    )

  return settings_raw


def write_settings(settings_raw, outfile="default_settings.txt"):
  with open(outfile, 'w') as f:
    f.write(settings_raw)


if __name__ == "__main__":
  settings = get_settings(
    size_in_bytes="TEST_BYTES",
    ttl="TEST_TTL",
    scenario_name="TEST_NAME"
  )

  write_settings(settings)
