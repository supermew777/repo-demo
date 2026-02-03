# To-Do List Application (OOP & Git)
This is a simple To-Do List application built with Python.

## 1. คำอธิบายโปรเจกต์ (Project Description)
แอปพลิเคชันสำหรับจัดการรายการงานที่ต้องทำ (To-Do List) พัฒนาด้วยภาษา Python โดยใช้หลักการเขียนโปรแกรมเชิงวัตถุ (OOP) เพื่อให้โค้ดมีความเป็นระเบียบและง่ายต่อการขยายผล โปรแกรมนี้ใช้คลาส `Task` ในการแทนข้อมูลแต่ละรายการ และใช้ไฟล์ JSON ในการจัดเก็บข้อมูลเพื่อให้ผู้ใช้งานสามารถบันทึกและโหลดข้อมูลกลับมาใช้ใหม่ได้ตลอดเวลา

## 2. วิธีการรันโปรแกรม (How to Run)
1. ตรวจสอบว่าเครื่องของคุณติดตั้ง Python 3 เรียบร้อยแล้ว
2. ดาวน์โหลดไฟล์ `todo_app.py` และ `my_tasks.json` มาไว้ในโฟลเดอร์เดียวกัน
3. เปิด Terminal หรือ Command Prompt แล้วเข้าไปยังโฟลเดอร์นั้น
4. รันโปรแกรมด้วยคำสั่ง:
   ```bash
   python todo_app.py


## ตัวอย่าง Input และ Output (Example Usage)
ตัวอย่างการเพิ่มงาน (Input):

เลือกเมนู: 1

พิมพ์ชื่อพิมพ์งาน: Finish my homework
ตัวอย่างการแสดงผล (Output):
1. Add Task | 2. View Tasks | 3. Exit

Select: 2
1. Finish my homework [Wait]
   
## อธิบายการใช้ Git (Git Version Control)
Commits: มีการทำ Commit มากกว่า 10 ครั้ง โดยระบุข้อความ (Commit Message) ที่ชัดเจนและสื่อความหมายถึงสิ่งที่ทำในแต่ละขั้นตอน เช่น Feat:, Fix:, Docs:

Branching: มีการสร้าง Branch ชื่อ add-readme เพื่อแยกการเขียนเอกสารประกอบโปรเจกต์ออกจากสายงานหลัก (master) เพื่อลดความเสี่ยงที่จะกระทบกับโค้ดที่ทำงานได้จริง

Merging: หลังจากตรวจสอบความเรียบร้อยใน Branch ย่อยแล้ว ได้ทำการ Merge งานกลับเข้าสู่สายหลักเพื่อให้ GitHub Repository มีข้อมูลที่สมบูรณ์
