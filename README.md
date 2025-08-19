# 🔐 SBF - Slow Brute Force

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)]()

---

## 👾 نظرة عامة

**SBF (Slow Brute Force)** هي أداة مكتوبة بلغة Python لتنفيذ **هجمات brute force بطيئة** على واجهات تسجيل الدخول.  
تم تصميمها خصيصًا لتجاوز أنظمة الحماية (IDS/IPS) ومنع القفل التلقائي للحسابات أثناء الاختبار.  
الأداة موجهة للباحثين الأمنيين وطلاب الأمن السيبراني.

---

## ⚡ الميزات

- 📝 دعم **wordlists** جاهزة مدمجة:
  - `top100.txt`
  - `rockyou-50.txt`
  - `simple-pass.txt`
- 📂 إمكانية اختيار **wordlist مخصصة**.
- 🐌 هجوم بطيء قابل للتحكم عبر تأخير زمني.
- 🔗 دعم العمل مع **proxy** (http/socks4/socks5).
- 🧵 استخدام **Threads** لتجربة كلمات مرور متعددة.
- 💾 تخزين النتيجة في ملف `found.txt` عند النجاح.

---

## 🛠️ المتطلبات

- Python **3.8+**
- مكتبات:
  - `requests`
  - `threading`
  - `time`
  - (موجودة مع Python افتراضيًا باستثناء `requests`)

لتثبيت المتطلبات:
```bash
pip install requests
```

---

## 🚀 طريقة الاستخدام

لتشغيل الأداة:

```bash
python3 slow_brute_force.py
```

بعد التشغيل، ستظهر واجهة تفاعلية تطلب منك إدخال:

1. **رابط صفحة تسجيل الدخول (Login URL)**.  
2. **اسم الحقل الخاص بالمستخدم** (مثل: `username` أو `email`).  
3. **اسم الحقل الخاص بكلمة المرور** (مثل: `password`).  
4. **البريد الإلكتروني / اسم المستخدم المستهدف**.  
5. اختيار **wordlist** من الخيارات المدمجة أو إدخال مسار ملف خارجي.  
6. إدخال **زمن التأخير** بين المحاولات (بالثواني).  
7. تحديد ما إذا كنت تريد استخدام **Proxy**.  

---

## 📌 مثال عملي (خطوات التشغيل)

```
$ python3 slow_brute_force.py

[+] Enter login URL: http://example.com/login
[+] Enter user field name: email
[+] Enter password field name: password
[+] Enter target username/email: admin@example.com

[+] Choose a wordlist:
  1) top100.txt
  2) rockyou-50.txt
  3) simple-pass.txt
  4) Custom path
>> 2

[+] Delay between attempts (seconds): 2
>> Use proxy? (y/n): n

[+] Starting threaded brute force...
```

عند العثور على كلمة مرور صحيحة، سيتم حفظها في:
```
found.txt
```

---

## 📜 الترخيص

تم إصدار SBF بموجب رخصة **MIT License** – يمكن استخدام الأداة والتعديل عليها بحرية مع الحفاظ على حقوق النشر.

---

⚠️ **تنبيه**: هذه الأداة للتعليم والاختبارات الأمنية المصرح بها فقط.  
🚫 استخدام الأداة ضد أنظمة بدون إذن صريح يعرضك للمساءلة القانونية.
