"""Pick"""
import json
def main():
    """print Yes or No and print Value"""
    text = json.loads(input())
    text2 = input()
    # เพิ่มตัวแปรcount เอาไว้เก็บค่า print
    count_print = 0
    for key in text.keys():
    	# เปลี่ยนชื่อตัวแปรให้เข้าใจง่ายๆหน่อยokนะ
        if key == text2:
            print("Yes")
            # เพิ่มบรรทัดนี้เข้าไปให้นะ เราต้องใช้ dict[key] มันจะreturn values ออกมาให
            print(text[key])
            count_print += 1
            break

    # กรณีนี้ตัวแปรkey อยู่นอกloopเราเอามาใช้ไม่ได้นะ
    # if key != text2:
    #     print("No")

    # ถ้าไม่มีปริ้นkeyเลยก็จะปิ้น No ออกมาให้
    if count_print == 0:
        print('No')
main()
