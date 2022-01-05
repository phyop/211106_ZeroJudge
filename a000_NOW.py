from datetime import datetime

result = datetime.now().strftime("%Y-%m-%d %w %H:%M:%S %p")
print(result)

# sys.stdout.write就不會換行
# sympy在解跟質數相關的題目真的很好用 :D

"""
《f'' 字串》
https://iter01.com/585538.html
>>> f"{2 * 37}"
'74'
使用大寫字母也是有效的F
>>> f"Hello, {name}. You are {age}."
>>> F"Hello, {name}. You are {age}."
'Hello, Eric. You are 74.'
也可以呼叫函式
>>> def to_lowercase(input):
...     return input.lower()
>>> name = "Eric Idle"
>>> f"{to_lowercase(name)} is funny."
'eric idle is funny.
需要在多行字串的每一行前面放一個f
>>> message = (
...     f"Hi {name}. "
...     f"You are a {profession}. "
... )
多行字串可使用()或是轉義字元 \
>>> message = f"Hi {name}. " \
...           f"You are a {profession}. " \
...           f"You were in {affiliation}."
...
'Hi Eric. You are a comedian. You were in Monty Python.'
"""

----------------------------------

"""
《正則》
https://blog.csdn.net/u014550838/article/details/103726462?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.pc_relevant_paycolumn_v2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.pc_relevant_paycolumn_v2&utm_relevant_index=2
“\”为转义字符，如果需要匹配文本中的字符“\”，在正则表达式中需要4个“\”，
前2个“\”和后两个“\”在python解释器中「分别」转义成一个“\”，
然后转义后的2个“\”再經過正则转义成一个“\”

r'字串內容' 表示原生字符串（rawstring），
python解釋器不再轉義，只需要經過正則轉義，
所以用2個"\"就可以匹配文本中一個字符“\”
"""

----------------------------------

"""
《vi 全選》
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