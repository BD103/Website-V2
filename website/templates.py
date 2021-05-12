from jinja2 import Environment, FileSystemLoader, select_autoescape
from glob import iglob
import os


env = Environment(
  loader=FileSystemLoader("templates"),
  autoescape=select_autoescape(["html", "xml"])
)


def render(filename: str, output="docs", **kwargs):
  with open(f"{output}/{filename}", "wt") as fp:
    fp.write(
      env.get_template(filename).render(**kwargs)
    )


if __name__ == "__main__":
  for i in iglob("templates/*.html"):
    render(os.path.basename(i))
