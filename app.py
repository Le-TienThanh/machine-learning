import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import pandas as pd
import joblib

# ===== LOAD MODEL =====
model = joblib.load('E:/PYTHON/final-project-v2/model/xgb_model.pkl')

# ===== CÁC TRƯỜNG NHẬP LIỆU =====
categorical_fields = {
    'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Federal-gov', 'Local-gov', 'Self-emp-inc'],
    'education': ['Bachelors', 'HS-grad', '11th', 'Masters', '9th', 'Some-college', 'Assoc-acdm', 
                    'Assoc-voc', '7th-8th', 'Doctorate', 'Prof-school'],
    'marital-status': ['Never-married', 'Married-civ-spouse', 'Divorced', 'Separated', 'Widowed', 'Married-spouse-absent'],
    'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Prof-specialty', 'Other-service'],
    'relationship': ['Not-in-family', 'Husband', 'Wife', 'Own-child', 'Unmarried'],
    'race': ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other'],
    'sex': ['Male', 'Female'],
    'native-country': ['United-States', 'Cuba', 'Jamaica', 'India', 'Mexico', 'Philippines', 'Germany', 'Canada']
}

numerical_fields = ['age', 'fnlwgt', 'education-num', 'hours-per-week']

# ===== TẠO GIAO DIỆN =====
root = tk.Tk()
root.title("Dự đoán mức lương >50K$")

entries = {}

def predict():
    try:
        # Tạo dict chứa dữ liệu nhập
        input_data = {}
        for field in numerical_fields:
            val = float(entries[field].get())
            input_data[field] = val

        # One-hot cho dữ liệu phân loại
        for field in categorical_fields:
            selected = entries[field].get()
            for cat in categorical_fields[field]:
                col = f"{field}_{cat}"
                input_data[col] = 1 if cat == selected else 0

        # Xây DataFrame và thêm thiếu cột (nếu có)
        df = pd.DataFrame([input_data])
        for col in model.feature_names_in_:
            if col not in df.columns:
                df[col] = 0
        df = df[model.feature_names_in_]

        # Dự đoán
        pred = model.predict(df)[0]
        msg = "Lương > 50K $" if pred == 1 else "Lương <= 50K $"
        messagebox.showinfo("Kết quả", msg)
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Layout form
row = 0
for field in numerical_fields:
    tk.Label(root, text=field).grid(row=row, column=0)
    entries[field] = tk.Entry(root)
    entries[field].grid(row=row, column=1)
    row += 1

for field in categorical_fields:
    tk.Label(root, text=field).grid(row=row, column=0)
    cb = ttk.Combobox(root, values=categorical_fields[field])
    cb.grid(row=row, column=1)
    cb.current(0)
    entries[field] = cb
    row += 1

tk.Button(root, text="Dự đoán", command=predict).grid(row=row, column=0, columnspan=2)
root.mainloop()

# import tkinter as tk
# from tkinter import ttk, messagebox
# import numpy as np
# import pandas as pd
# import joblib

# # Load mô hình và dữ liệu
# model = joblib.load("E:/PYTHON/final-project-v2/model/xgb_model.pkl")
# # scaler = joblib.load("scaler.pkl")
# # columns = joblib.load("feature_columns.pkl")

# # Các lựa chọn mặc định
# education_levels = ['Bachelors', 'HS-grad', '11th', 'Masters', '9th', 'Some-college', 'Assoc-acdm', 
#                     'Assoc-voc', '7th-8th', 'Doctorate', 'Prof-school']
# workclasses = ['State-gov', 'Self-emp-not-inc', 'Private', 'Federal-gov', 'Local-gov', 'Self-emp-inc']
# marital_statuses = ['Never-married', 'Married-civ-spouse', 'Divorced', 'Separated', 'Widowed', 'Married-spouse-absent']
# occupations = ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Prof-specialty', 'Other-service']
# relationships = ['Not-in-family', 'Husband', 'Wife', 'Own-child', 'Unmarried']
# races = ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other']
# sexes = ['Male', 'Female']
# countries = ['United-States', 'Cuba', 'Jamaica', 'India', 'Mexico', 'Philippines', 'Germany', 'Canada']

# num_cols = ['age', 'fnlwgt', 'education-num', 'hours-per-week']

# # Khởi tạo giao diện
# app = tk.Tk()
# app.title("Dự đoán mức lương >50K")
# app.geometry("600x600")

# def predict():
#     try:
#         input_dict = {
#             'age': float(entry_age.get()),
#             'fnlwgt': float(entry_fnlwgt.get()),
#             'education-num': float(entry_edu_num.get()),
#             'hours-per-week': float(entry_hours.get()),
#             'education': combo_edu.get(),
#             'workclass': combo_wc.get(),
#             'marital-status': combo_ms.get(),
#             'occupation': combo_occu.get(),
#             'relationship': combo_rela.get(),
#             'race': combo_race.get(),
#             'sex': combo_sex.get(),
#             'native-country': combo_country.get()
#         }

#         input_df = pd.DataFrame([input_dict])
#         input_df = pd.get_dummies(input_df)
#         # input_df[num_cols] = scaler.transform(input_df[num_cols])
#         for col in columns:
#             if col not in input_df.columns:
#                 input_df[col] = 0
#         input_df = input_df[columns]

#         pred = model.predict(input_df)[0]
#         result = "Mức lương >50K" if pred == 1 else "Mức lương ≤50K"
#         messagebox.showinfo("Kết quả dự đoán", result)
#     except Exception as e:
#         messagebox.showerror("Lỗi", str(e))

# tk.Label(app, text="Tuổi:").pack()
# entry_age = tk.Entry(app); entry_age.pack()

# tk.Label(app, text="Fnlwgt:").pack()
# entry_fnlwgt = tk.Entry(app); entry_fnlwgt.pack()

# tk.Label(app, text="Education-num:").pack()
# entry_edu_num = tk.Entry(app); entry_edu_num.pack()

# tk.Label(app, text="Giờ làm mỗi tuần:").pack()
# entry_hours = tk.Entry(app); entry_hours.pack()

# def make_combobox(label, values):
#     tk.Label(app, text=label).pack()
#     cb = ttk.Combobox(app, values=values)
#     cb.current(0)
#     cb.pack()
#     return cb

# combo_edu = make_combobox("Trình độ học vấn", education_levels)
# combo_wc = make_combobox("Workclass", workclasses)
# combo_ms = make_combobox("Tình trạng hôn nhân", marital_statuses)
# combo_occu = make_combobox("Nghề nghiệp", occupations)
# combo_rela = make_combobox("Mối quan hệ", relationships)
# combo_race = make_combobox("Chủng tộc", races)
# combo_sex = make_combobox("Giới tính", sexes)
# combo_country = make_combobox("Quốc gia", countries)

# tk.Button(app, text="Dự đoán", command=predict).pack(pady=10)

# app.mainloop()


# import tkinter as tk
# from tkinter import ttk, messagebox
# import pandas as pd
# import joblib

# # ===== LOAD MODEL =====
# model = joblib.load('E:/PYTHON/final-project-v2/model/xgb_model.pkl')

# # ===== CÁC TRƯỜNG NHẬP LIỆU =====
# categorical_fields = {
#     'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Federal-gov', 'Local-gov', 'Self-emp-inc'],
#     'education': ['Bachelors', 'HS-grad', '11th', 'Masters', '9th', 'Some-college', 'Assoc-acdm', 
#                   'Assoc-voc', '7th-8th', 'Doctorate', 'Prof-school'],
#     'marital-status': ['Never-married', 'Married-civ-spouse', 'Divorced', 'Separated', 'Widowed', 'Married-spouse-absent'],
#     'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Prof-specialty', 'Other-service'],
#     'relationship': ['Not-in-family', 'Husband', 'Wife', 'Own-child', 'Unmarried'],
#     'race': ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other'],
#     'sex': ['Male', 'Female'],
#     'native-country': ['United-States', 'Cuba', 'Jamaica', 'India', 'Mexico', 'Philippines', 'Germany', 'Canada']
# }

# numerical_fields = ['age', 'fnlwgt', 'education-num', 'hours-per-week']

# # ===== TẠO GIAO DIỆN =====
# root = tk.Tk()
# root.title("Dự đoán mức lương >50K$")
# root.geometry("500x700")
# root.configure(bg="#f0f4f7")

# title_label = tk.Label(root, text="DỰ ĐOÁN MỨC LƯƠNG", font=("Helvetica", 16, "bold"), fg="#333", bg="#f0f4f7")
# title_label.pack(pady=10)

# form_frame = tk.Frame(root, bg="#f0f4f7")
# form_frame.pack(pady=10)

# entries = {}

# def add_field(label_text, widget):
#     row = tk.Frame(form_frame, bg="#f0f4f7")
#     row.pack(fill="x", pady=5, padx=20)

#     lbl = tk.Label(row, text=label_text, width=20, anchor="w", bg="#f0f4f7", font=("Helvetica", 10))
#     lbl.pack(side="left")

#     widget.pack(side="right", expand=True, fill="x")

# # Numerical fields
# for field in numerical_fields:
#     entry = tk.Entry(form_frame, font=("Helvetica", 10))
#     entries[field] = entry
#     add_field(field, entry)

# # Categorical fields
# for field in categorical_fields:
#     cb = ttk.Combobox(form_frame, values=categorical_fields[field], font=("Helvetica", 10))
#     cb.current(0)
#     entries[field] = cb
#     add_field(field, cb)

# # Predict function
# def predict():
#     try:
#         input_data = {}
#         for field in numerical_fields:
#             val = float(entries[field].get())
#             input_data[field] = val

#         for field in categorical_fields:
#             selected = entries[field].get()
#             for cat in categorical_fields[field]:
#                 col = f"{field}_{cat}"
#                 input_data[col] = 1 if cat == selected else 0

#         df = pd.DataFrame([input_data])
#         for col in model.feature_names_in_:
#             if col not in df.columns:
#                 df[col] = 0
#         df = df[model.feature_names_in_]

#         pred = model.predict(df)[0]
#         msg = "Lương > 50K $" if pred == 1 else "Lương <= 50K $"
#         messagebox.showinfo("Kết quả", msg)
#     except Exception as e:
#         messagebox.showerror("Lỗi", str(e))

# # Button
# btn = tk.Button(root, text="Dự đoán", command=predict, font=("Helvetica", 12, "bold"),
#                 bg="#4CAF50", fg="white", padx=10, pady=5)
# btn.pack(pady=20)

# root.mainloop()
