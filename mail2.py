import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def process_file():
    file_name = file_entry.get()
    baobao = baobao_entry.get()

    with open(file_name, 'r') as input_file:
        emails = input_file.readlines()

    output_file_name = f'{baobao}.vcf'
    total_emails = len(emails)
    with open(output_file_name, 'w') as output_file:
        for i, email in enumerate(emails):
            vcard = f"BEGIN:VCARD\nVERSION:3.0\nEMAIL;TYPE=INTERNET;TYPE=HOME:{email.strip()}\nEND:VCARD\n"
            output_file.write(vcard)
            progress['value'] = (i + 1) * 100 / total_emails
            root.update_idletasks()
    
    messagebox.showinfo("处理完成", "文件处理完成！")

# 创建主窗口
root = tk.Tk()
root.title("邮箱处理工具")
root.geometry("400x250")  # 设置窗口宽度为400像素，高度为250像素

# 文件名输入框和按钮
file_label = tk.Label(root, text="请输入要处理的txt文件名：")
file_label.pack()
file_entry = tk.Entry(root)
file_entry.pack()
file_button = tk.Button(root, text="选择文件", command=lambda: file_entry.insert(0, filedialog.askopenfilename()))
file_button.pack()

# 保存后文件名输入框
baobao_label = tk.Label(root, text="请输入处理完成保存后文件名(不用后缀)：")
baobao_label.pack()
baobao_entry = tk.Entry(root)
baobao_entry.pack()

# 进度条
progress_label = tk.Label(root, text="进度：")
progress_label.pack()
progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack()

# 执行处理按钮
process_button = tk.Button(root, text="处理文件", command=process_file)
process_button.pack()

# 运行主循环
root.mainloop()
