import markdown
import requests

def hello_world(txt):
    r = requests.get("https://httpbin.org/uuid")
    return markdown.markdown(f'{txt} - {r.text}')

if __name__ == "__main__":
    print("Main")
