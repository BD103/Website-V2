import requests
import json


def get_data(username="BD103"):
  data = json.loads(requests.get(
    "https://api.github.com/users/BD103/repos",
    params = {
      "sort": "updated",
      "per_page": 5
    }
  ).text)

  return data


if __name__ == "__main__":
  print(get_data())