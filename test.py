import tkinter as tk
from tkinter import messagebox


# ==========================================
# ФУНКЦИИ РАСЧЕТА
# ==========================================


def X_0():
    try:
        weight = float(entry_Weight.get())
        force_p = float(entry_P.get())
        side_oa = float(entry_OA.get())
        side_ab = float(entry_AB.get())
        side_oc = float(entry_OC.get())

        if any(x < 0 for x in [weight, force_p, side_oa, side_ab, side_oc]):
            messagebox.showwarning("Внимание", "Значения не могут быть отрицательными!")
            return

        if any(x == 0 for x in [side_oa, side_ab, side_oc]):
            messagebox.showerror("Ошибка", "Стороны не могут быть равны нулю!")
            return

        result = -force_p * (side_ab / (side_oa**2 + side_ab**2) ** 0.5)
        result_label.config(text=f"{result:.1f} H")

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


def calculate_all():
    X_0()
    Y_c()
    Y_0()


def Y_c():
    global result_1
    try:
        weight = float(entry_Weight.get())
        force_p = float(entry_P.get())
        side_oa = float(entry_OA.get())
        side_ab = float(entry_AB.get())
        side_oc = float(entry_OC.get())

        if any(x < 0 for x in [weight, force_p, side_oa, side_ab, side_oc]):
            messagebox.showwarning("Внимание", "Значения не могут быть отрицательными!")
            return

        if any(x == 0 for x in [side_oa, side_ab, side_oc]):
            messagebox.showerror("Ошибка", "Стороны не могут быть равны нулю!")
            return

        result_1 = (
            2 * side_oa * weight
            + 3 * (((side_oa**2 + side_ab**2) ** 0.5) / 2) * force_p
        ) / (3 * side_oc)

        result_label_1.config(text=f"{result_1:.1f} H")

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


def Y_0():
    try:
        weight = float(entry_Weight.get())
        force_p = float(entry_P.get())
        side_oa = float(entry_OA.get())
        side_ab = float(entry_AB.get())
        side_oc = float(entry_OC.get())

        if any(x < 0 for x in [weight, force_p, side_oa, side_ab, side_oc]):
            messagebox.showwarning("Внимание", "Значения не могут быть отрицательными!")
            return

        if any(x == 0 for x in [side_oa, side_ab, side_oc]):
            messagebox.showerror("Ошибка", "Стороны не могут быть равны нулю!")
            return

        result2 = (
            force_p * (side_oa / (side_oa**2 + side_ab**2) ** 0.5) + weight - result_1
        )

        result_label_2.config(text=f"{result2:.1f} H")

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


        
    

def clear_fields():
    """Очистка всех полей и сброс ползунков"""
    entries = [entry_Weight, entry_P, entry_OA, entry_AB, entry_OC]
    scales = [scale_Weight, scale_P, scale_OA, scale_AB, scale_OC]
    defaults = [5, 10.4, 24, 10, 8]

    for entry, scale, default in zip(entries, scales, defaults):
        entry.delete(0, tk.END)
        entry.insert(0, str(default))
        scale.set(default)

    result_label.config(text="")
    result_label_1.config(text="")
    result_label_2.config(text="")


# ==========================================
# ФУНКЦИИ СВЯЗИ ПОЛЗУНКОВ И ПОЛЕЙ
# ==========================================


def update_entry_from_scale(val, entry):
    """Когда двигаем ползунок -> обновляется цифра в поле (мгновенно)"""
    value = float(val)
    # Округляем до целого если нет дробной части
    if value == int(value):
        entry.delete(0, tk.END)
        entry.insert(0, str(int(value)))
    else:
        entry.delete(0, tk.END)
        entry.insert(0, f"{value:.1f}")


def update_scale_from_entry(*args):
    """Когда вводим цифру в поле -> обновляется ползунок"""
    try:
        for entry, scale, min_val, max_val in zip(
            entries_list, scales_list, mins_list, maxs_list
        ):
            val = float(entry.get())
            # Ограничиваем значениями ползунка
            if val < min_val:
                val = min_val
            if val > max_val:
                val = max_val
            scale.set(val)
    except ValueError:
        pass


# ==========================================
# ОТКРЫТИЕ ОКНА С ЗАДАЧЕЙ
# ==========================================


def open_task_window():
    global entry_Weight, entry_P, entry_OA, entry_AB, entry_OC
    global scale_Weight, scale_P, scale_OA, scale_AB, scale_OC
    global result_label, result_label_1, result_label_2
    global entries_list, scales_list, mins_list, maxs_list

    task_window = tk.Toplevel(window)
    task_window.title("Решение задачи")
    task_window.geometry("1520x1080")
    task_window.resizable(width=False, height=False)
    task_window.config(bg="#e8e8e8")

    # Заголовок задачи
    Label_1 = tk.Label(
        task_window,
        text="Однородная пластинка весом 5Н, имеющая форму прямоугольного треугольника, шарнирно прикреплена к опоре О и свободно опирается на гладкую опору С. "
        "АВ = 10 см, ОА = 24 см, ОС = 8 см. Перпендикулярно к стороне ОВ приложена сила Р = 10.4Н. "
        "OD = BD. Определить реакции опор.",
        bg="white",
        fg="black",
        font=("Arial", 14),
        wraplength=1200,
        justify="left",
    )
    Label_1.pack(pady=10)

    line = tk.Frame(task_window, height=2, bg="black")
    line.pack(fill="x", padx=10, pady=5)

    # Фрейм для полей ввода и ползунков
    frame_inputs = tk.Frame(task_window, bg="#e8e8e8")
    frame_inputs.pack(pady=20)

    # Списки для хранения ссылок
    entries_list = []
    scales_list = []
    mins_list = []
    maxs_list = []

    # Настройки для каждого параметра
    inputs_config = [
        ("Cторона OC (см):", 1, 50, 8),
        ("Cторона AB (см):", 1, 100, 10),
        ("Cторона OA (см):", 1, 100, 24),
        ("Вес пластины (Н):", 0.1, 100, 5),
        ("Сила P (Н):", 0.1, 50, 10.4),
    ]

    global entry_OC, entry_AB, entry_OA, entry_Weight, entry_P
    global scale_OC, scale_AB, scale_OA, scale_Weight, scale_P

    for i, (text, min_v, max_v, default) in enumerate(inputs_config):
        # Метка
        lbl = tk.Label(frame_inputs, text=text, bg="#e8e8e8", font=("Arial", 12))
        lbl.grid(row=i, column=0, padx=10, pady=5, sticky="e")

        # Поле ввода (Entry)
        ent = tk.Entry(frame_inputs, width=10, font=("Arial", 14), justify="center")
        ent.insert(0, str(default))
        ent.grid(row=i, column=1, padx=10, pady=5)

        # Ползунок (Scale) - обновляется МГНОВЕННО при перетаскивании
        scl = tk.Scale(
            frame_inputs,
            from_=min_v,
            to=max_v,
            orient="horizontal",
            length=300,
            resolution=0.1,
            font=("Arial", 10),
            # command вызывается непрерывно при перетаскивании!
            command=lambda val, e=ent: update_entry_from_scale(val, e),
        )
        scl.set(default)
        scl.grid(row=i, column=2, padx=10, pady=5)

        # Сохраняем в списки
        entries_list.append(ent)
        scales_list.append(scl)
        mins_list.append(min_v)
        maxs_list.append(max_v)

        # Сохраняем переменные глобально
        if i == 0:
            entry_OC, scale_OC = ent, scl
        if i == 1:
            entry_AB, scale_AB = ent, scl
        if i == 2:
            entry_OA, scale_OA = ent, scl
        if i == 3:
            entry_Weight, scale_Weight = ent, scl
        if i == 4:
            entry_P, scale_P = ent, scl

        # Привязка события изменения текста в поле к ползунку
        var = tk.StringVar()
        var.trace_add("write", lambda *args: update_scale_from_entry())
        ent.config(textvariable=var)

    # Кнопки
    btn_frame = tk.Frame(task_window, bg="#e8e8e8")
    btn_frame.pack(pady=20)

    button = tk.Button(
        btn_frame,
        text="Решить",
        font=("Arial", 14, "bold"),
        command=calculate_all,
        width=15,
        bg="#000000",
        fg="white",
    )
    button.grid(row=0, column=0, padx=10)

    button1 = tk.Button(
        btn_frame,
        text="Oчистить",
        font=("Arial", 14, "bold"),
        command=clear_fields,
        width=15,
        bg="#666666",
        fg="white",
    )
    button1.grid(row=0, column=1, padx=10)

    # Поля вывода ответов
    result_frame = tk.Frame(task_window, bg="#e8e8e8")
    result_frame.pack(pady=20)

    tk.Label(result_frame, text="X₀ =", font=("Arial", 16, "bold"), bg="#e8e8e8").grid(
        row=0, column=0, padx=10
    )
    result_label = tk.Label(
        result_frame,
        text="",
        font=("Arial", 18),
        bg="white",
        width=15,
        height=2,
        relief="sunken",
    )
    result_label.grid(row=0, column=1, padx=10)

    tk.Label(result_frame, text="Yc =", font=("Arial", 16, "bold"), bg="#e8e8e8").grid(
        row=1, column=0, padx=10, pady=10
    )
    result_label_1 = tk.Label(
        result_frame,
        text="",
        font=("Arial", 18),
        bg="white",
        width=15,
        height=2,
        relief="sunken",
    )
    result_label_1.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(result_frame, text="Y₀ =", font=("Arial", 16, "bold"), bg="#e8e8e8").grid(
        row=2, column=0, padx=10
    )
    result_label_2 = tk.Label(
        result_frame,
        text="",
        font=("Arial", 18),
        bg="white",
        width=15,
        height=2,
        relief="sunken",
    )
    result_label_2.grid(row=2, column=1, padx=10)


# ==========================================
# ГЛАВНОЕ ОКНО (МЕНЮ)
# ==========================================

window = tk.Tk()
window.title("Механика")
window.geometry("1520x1080")
window.resizable(width=False, height=False)

bg_color = "#e8e8e8"
window.config(bg=bg_color)

lbl_header = tk.Label(
    window,
    text="ПРОЕКТНАЯ РАБОТА — 2026",
    bg=bg_color,
    font=("Arial", 16, "bold"),
    fg="#333",
)
lbl_header.place(relx=0.98, rely=0.03, anchor="ne")

lbl_version = tk.Label(
    window, text="ВЕРСИЯ 1-0-0", bg=bg_color, font=("Arial", 10), fg="#555"
)
lbl_version.place(relx=0.02, rely=0.98, anchor="sw")

lbl_status = tk.Label(
    window, text="ГОТОВ К РАБОТЕ ●", bg=bg_color, font=("Arial", 10), fg="#555"
)
lbl_status.place(relx=0.98, rely=0.98, anchor="se")

btn_main = tk.Button(
    window,
    text="РЕШИТЬ ЗАДАЧУ!",
    font=("Arial", 20, "bold"),
    bg="#2b2b2b",
    fg="white",
    activebackground="#444",
    activeforeground="white",
    relief=tk.FLAT,
    cursor="hand2",
    command=open_task_window,
)
btn_main.place(relx=0.5, rely=0.4, anchor="center", width=500, height=80)

menu_frame = tk.Frame(window, bg=bg_color)
menu_frame.place(relx=0.5, rely=0.55, anchor="center")

btn_style = {
    "font": ("Arial", 14),
    "bg": "white",
    "fg": "black",
    "activebackground": "#f0f0f0",
    "relief": tk.SOLID,
    "bd": 1,
    "highlightthickness": 1,
    "highlightbackground": "#999",
    "width": 25,
    "cursor": "hand2",
}

tk.Button(menu_frame, text="О ПРОГРАММЕ", **btn_style).pack(pady=10)
tk.Button(menu_frame, text="НАСТРОЙКИ", **btn_style).pack(pady=10)
tk.Button(menu_frame, text="ВЫХОД", **btn_style, command=window.quit).pack(pady=10)


window.mainloop()
