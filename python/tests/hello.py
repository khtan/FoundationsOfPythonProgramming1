# python flexible indenting occurs in blocks
# but the first char of first line needs to exist
for num in range(3):
        print("hello world")

def headline(text: str, align: bool =True) -> str:
        if align:
                return f"{text.title()}\n{'-' * len(text)}"
        else:
                return f"{text.title()}".center(50, "o")

title = "python type checking"
print(headline(title))
print(headline(title, align=False))
print(headline(title, align="center"))

