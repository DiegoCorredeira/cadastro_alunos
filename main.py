import tkinter as tk
from tkinter import Image, ttk
import sqlite3
from PIL import ImageTk, Image


def create_table():
    conn = sqlite3.connect("clientes.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS vendas (
            nome TEXT, 
            quantidade INTEGER,
            saldo_devedor REAL,
            data_pagamento TEXT,
            data_venda TEXT,
            pago INTEGER
        )"""
    )
    conn.commit()
    conn.close()


def add_venda():
    nome = entry_nome.get()
    quantidade = entry_quantidade.get()
    saldo_devedor = entry_saldo_devedor.get()
    data_pagamento = entry_data_pagamento.get()
    data_venda = entry_data_venda.get()
    pago = chekbox_pago.get()

    conn = sqlite3.connect("clientes.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO vendas (nome, quantidade, saldo_devedor, data_pagamento, data_venda, pago) VALUES (?, ?, ?, ?, ?, ?)",
        (nome, quantidade, saldo_devedor, data_pagamento, data_venda, pago),
    )
    conn.commit()
    conn.close()

    entry_nome.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_saldo_devedor.delete(0, tk.END)
    entry_data_pagamento.delete(0, tk.END)
    entry_data_venda.delete(0, tk.END)
    chekbox_pago.set(0)

    label_status["text"] = "Venda adicionada com sucesso!"

def vendas_output():
    conn = sqlite3.connect("clientes.db")
    c = conn.cursor()
    c.execute("SELECT * FROM vendas")
    vendas = c.fetchall() 
    conn.close()

    output.delete('1.0', tk.END)

    for venda in vendas:
        nome = venda[0]
        quantidade = venda[1]
        saldo_devedor = venda[2]
        data_pagamento = venda[3]
        data_venda = venda[4]
        pago = "SIM" if venda[5] else "NÃO"

        output.insert(tk.END, f"Nome: {nome}\n")
        output.insert(tk.END, f"Quantidade: {quantidade}\n")
        output.insert(tk.END, f"Saldo devedor: {saldo_devedor}\n")
        output.insert(tk.END, f"Data do pagamento: {data_pagamento}\n")
        output.insert(tk.END, f"Data da venda: {data_venda}\n")
        output.insert(tk.END, f"Pago: {pago}\n\n") 
        output.insert(tk.END, f"-------------------------\n\n") 



root = tk.Tk()
root.title("Pagamentos de clientes")
root.geometry("327x500")


style = ttk.Style()
style.configure("TLable", background="#F0F0F0")
style.configure("TButton", background="#FFD700")


main_frame = ttk.Frame(root, padding=20)
main_frame.grid()


label_nome = ttk.Label(main_frame, text="Nome do cliente: ")
label_nome.grid(row=0, column=0, sticky="W")

label_quantidade = ttk.Label(main_frame, text="Quantidade adquirida: ")
label_quantidade.grid(row=1, column=0, sticky="W")

label_saldo_devedor = ttk.Label(main_frame, text="Saldo devedor do cliente: ")
label_saldo_devedor.grid(row=2, column=0, sticky="W")

label_data_venda = ttk.Label(main_frame, text="Data da venda: ")
label_data_venda.grid(row=3, column=0, sticky="W")

label_data_pagamento = ttk.Label(main_frame, text="Data do pagamento: ")
label_data_pagamento.grid(row=4, column=0, sticky="W")

# Entrada dos labels
entry_nome = ttk.Entry(main_frame)
entry_nome.grid(row=0, column=1)

entry_quantidade = ttk.Entry(main_frame)
entry_quantidade.grid(row=1, column=1)

entry_saldo_devedor = ttk.Entry(main_frame)
entry_saldo_devedor.grid(row=2, column=1)

entry_data_venda = ttk.Entry(main_frame)
entry_data_venda.grid(row=3, column=1)

entry_data_pagamento = ttk.Entry(main_frame)
entry_data_pagamento.grid(row=4, column=1)


chekbox_pago = tk.BooleanVar()
chekbox_pago.set(False)
checkbox = ttk.Checkbutton(
    main_frame, text="Pago?", variable=chekbox_pago, style="TCheckbutton"
)
checkbox.grid(row=5, column=1, sticky="W")

button_adicionar = ttk.Button(
    main_frame, text="Adicionar venda", command=add_venda, style="TButton"
)
button_adicionar.grid(row=6, column=0, columnspan=2, pady=10)

button_exibir_clientes = ttk.Button(main_frame, text="Exibir clientes", style="TButton", command=vendas_output)
button_exibir_clientes.grid(row=7, column=0, columnspan=2, pady=10)

label_status = ttk.Label(main_frame, text="")
label_status.grid(row=8, column=0, columnspan=2)


output_frame = ttk.Frame(root)
output_frame.grid(row=9, column=0, columnspan=2)
output_frame.configure(borderwidth=1, relief="solid")

output = tk.Text(output_frame, width=40, height=10)
output.pack()

create_table()
root.mainloop()
