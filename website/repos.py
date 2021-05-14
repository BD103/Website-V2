import requests


def data():
  params = {
    "sort": "updated",
    "per_page": 5
  }
  return requests.get(
    "https://api.github.com/users/BD103/repos",
    params=params
  ).json()