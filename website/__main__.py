from . import style, folders, templates, repos


to_be_rendered = [
  "index.html",
  "programming.html"
]

render_kwargs = {
  "years_coding": 6,
  "fav_lang": "Python",
  "repos": repos.data()
}


if __name__ == "__main__":
  folders.run()
  style.build(file="main.scss")

  for i in to_be_rendered:
    templates.render(i, **render_kwargs)

  with open("docs/CNAME", "wt") as fp:
    fp.write("bd103.thedev.id")
  