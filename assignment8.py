# -*- coding: utf-8 -*-
import re
from html import unescape

# کلاس پایه برای متن
class cText:
    def __init__(self, text=""):
        """
        سازنده کلاس cText
        محاسبه و ذخیره تعداد کاراکتر، کلمه و پاراگراف
        """
        self.text = text
        self.char_count = len(text)
        self.word_count = len(text.split())
        self.paragraph_count = text.count('\n') + 1 if text else 0

    def read_file(self, filename):
        """
        خواندن متن از فایل با نام filename
        و بروزرسانی آمار
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.text = f.read()
                self.char_count = len(self.text)
                self.word_count = len(self.text.split())
                self.paragraph_count = self.text.count('\n') + 1 if self.text else 0
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    def write_file(self, filename):
        """
        نوشتن متن در فایل با نام filename
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.text)

# کلاس مشتق برای عملیات Regex و HTML
class cRegx(cText):
    def html_to_text(self):
        """
        تبدیل متن HTML به متن ساده
        """
        clean = re.sub(r'<[^>]+>', '', self.text)
        return unescape(clean)

    def find_emails(self):
        """
        پیدا کردن تمام ایمیل‌ها در متن
        """
        return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', self.text)

    def find_urls(self):
        """
        پیدا کردن تمام لینک‌ها (http/https) در متن
        """
        return re.findall(r'https?://[^\s]+', self.text)

    def find_dates(self):
        """
        پیدا کردن تاریخ‌ها در فرمت yyyy-mm-dd یا dd/mm/yyyy
        """
        pattern = r'\b(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})\b'
        return re.findall(pattern, self.text)

    def find_numbers(self):
        """
        پیدا کردن تمام ارقام در متن
        """
        return re.findall(r'\d+', self.text)

# نمونه تست برای اطمینان از عملکرد کلاس‌ها
if __name__ == "__main__":
    # نوشتن متن در فایل
obj.write_file("output.txt")
# خواندن دوباره فایل
obj.read_file("output.txt")
print("After reading file:", obj.text)
    sample_text = """سلام، این یک متن تست است.
تاریخ امروز 2025-12-24 است.
ایمیل من example@test.com است.
سایت ما: https://example.com
عدد: 12345"""

    # ایجاد شی از کلاس cRegx
    obj = cRegx(sample_text)

    print("Char count:", obj.char_count)
    print("Word count:", obj.word_count)
    print("Paragraph count:", obj.paragraph_count)
    print("Emails:", obj.find_emails())
    print("URLs:", obj.find_urls())
    print("Dates:", obj.find_dates())
    print("Numbers:", obj.find_numbers())
    print("HTML to text:", obj.html_to_text())

    # مثال خواندن و نوشتن فایل
    # obj.write_file("output.txt")
    # obj.read_file("output.txt")
    # print("After reading file:", obj.text)
