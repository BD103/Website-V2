from glob import iglob
import sass
import os


def build(folder="sass", file="[!_]*.scss", output="docs/static"):
  for i in iglob(f"{folder}/{file}"):
    with open(f"{output}/{os.path.basename(i).rsplit('.', 1)[0]}.css", "wt") as fp:
      fp.write(
        sass.compile(
          filename=i,
          output_style="compressed"
        )
      )


if __name__ == "__main__":
  build(file="main.scss")
