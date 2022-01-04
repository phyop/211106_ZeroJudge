from datetime import datetime

result = datetime.now().strftime("%Y-%m-%d %w %H:%M:%S %p")
print(result)

# sys.stdout.write就不會換行
# sympy在解跟質數相關的題目真的很好用 :D

"""
https://knowledge.chinesewords.org/319502-67.html
ggVG vim全選 
gg 讓光標移到首行，在vim才有效，vi中無效
V 是進入Visual(可視）模式
G 光標移到最後一行

:1,$y 全部復制
dG 刪除光標所在行到最後一行的內容（包括光標所在行的內容）

d 刪除選中內容
y 復制選中內容到0號寄存器
"+y 復制選中內容到＋寄存器，也就是系統的剪貼板
"""