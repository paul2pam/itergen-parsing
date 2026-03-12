from lark import Lark
import requests

with open("grammar.lark", "r") as f:
    grammar = f.read()

with open("itergen-agent/prompt.txt", "r") as f:
    prompt = f.read()



while(True):
    try: 
        response = requests.post("http://localhost:11434/api/generate", json={
        "model": "qwen2.5",
        "prompt": prompt,
        "stream": False,
        "temperature": 0.0
        })
        msg = response.json()["response"]
        print(msg)
        parser = Lark(grammar)
        tree = parser.parse(msg)
        print(tree.pretty())
        break
    except Exception as e:
        print(f"{e} retrying...")
        print("-" * 16)