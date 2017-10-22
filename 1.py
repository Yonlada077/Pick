"""Pick"""
import json
def main():
    """print Yes or No and print Value"""
    text = json.loads(input())
    text2 = input()
    for text3 in text.keys():
        if text3 == text2:
            print("Yes")
            break
    if text3 != text2:
        print("No")
main()