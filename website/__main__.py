from . import style, folders, templates


to_be_rendered = [
  "base.html",
  "index.html"
]


if __name__ == "__main__":
  folders.run()
  style.build(file="main.scss")

  for i in to_be_rendered:
    templates.render(i)

  with open("docs/CNAME", "wt") as fp:
    fp.write("bd103.thedev.id")