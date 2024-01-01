import markdown
import requests
import types


def hello_world(txt):
    try:
        r = requests.get("https://localhost/jjj")
    except Exception as e:
        r = types.SimpleNamespace(**{"text": "This is error"})
    return markdown.markdown(f"{txt} - {r.text}")


if __name__ == "__main__":
    print("Main")
