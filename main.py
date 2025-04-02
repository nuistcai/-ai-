import tkinter as tk

from tkinter import ttk, messagebox

import requests

# DeepSeek API的URL和API密钥

DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

API_KEY = "xxxxxxxxxx"  # 请替换为您的实际API密钥

# 定义分析流量的函数

def analyze_traffic():

    # 获取用户输入的流量包

    traffic_data = traffic_input.get("1.0", tk.END).strip()

    if not traffic_data:

        messagebox.showwarning("输入错误", "请输入HTTP流量包")

        return

    # 准备API请求的headers和payload

    headers = {

        "Authorization": f"Bearer {API_KEY}",

        "Content-Type": "application/json"

    }

   

    # 根据DeepSeek API的要求构造请求体

    payload = {

        "model": "deepseek-chat",  # 假设模型名称是deepseek-chat，请根据实际情况调整

        "messages": [

            {"role": "system", "content": "你是一个网络安全分析助手，负责分析HTTP流量是否为攻击流量。"},

            {"role": "user", "content": f"分析以下HTTP流量是否为攻击流量：\n{traffic_data}"}

        ],

        "max_tokens": 500  # 根据需要调整生成的最大token数

    }

   

    try:

        # 发送请求到DeepSeek API

        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)

        response.raise_for_status()  # 检查请求是否成功

       

        # 解析API响应

        result = response.json()

        # 假设API返回的结果在choices字段中

        analysis_result = result["choices"][0]["message"]["content"]

       

        # 显示分析结果

        result_label.config(text=f"分析结果: {analysis_result}")

   

    except requests.exceptions.RequestException as e:

        messagebox.showerror("API错误", f"无法连接到DeepSeek API: {e}")

    except KeyError as e:

        messagebox.showerror("解析错误", f"无法解析API响应: {e}")

# 创建主窗口

root = tk.Tk()

root.title("DeepSeek 流量分析工具")

root.geometry("800x600")

root.configure(bg="#0A0A0A")

# 设置科技感主题

style = ttk.Style()

style.theme_use('alt')

style.configure('TLabel', background='#0A0A0A', foreground='#00FF00', font=('Helvetica', 12, 'bold'))

style.configure('TButton', background='#00FF00', foreground='#0A0A0A', font=('Helvetica', 12, 'bold'))

style.configure('TText', background='#1E1E1E', foreground='#00FF00', font=('Courier', 10))

# 创建输入框和标签

traffic_label = ttk.Label(root, text="请输入HTTP流量包:")

traffic_label.pack(pady=20)

traffic_input = tk.Text(root, height=15, width=80, bg="#1E1E1E", fg="#00FF00", insertbackground='#00FF00')

traffic_input.pack(pady=10)

# 创建分析按钮

analyze_button = ttk.Button(root, text="分析流量", command=analyze_traffic)

analyze_button.pack(pady=20)

# 创建结果显示标签

result_label = ttk.Label(root, text="分析结果: ", wraplength=700)

result_label.pack(pady=20)

# 运行主循环

root.mainloop()

                        
