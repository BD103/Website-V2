import os
import shutil


def run():
  try:
    shutil.rmtree("docs")
  except FileNotFoundError:
    pass

  os.mkdir("docs")
  os.mkdir("docs/static")


if __name__ == "__main__":
  run()
