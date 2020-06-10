import random
import sys

def generate_random_number():
  # -1~1の数値をランダムに生成する
  num = random.randint(-1, 1)
  if num == -1:
    raise Exception("-1 is generated")
  return num

print("メッセージ：" + sys.argv[1])
print(generate_random_number())
