# Salary Prediction using Machine Learning

Dự án xây dựng mô hình phân loại để dự đoán một người có mức thu nhập **trên 50.000 USD/năm (`>50K`) hay không (`<=50K`)**, dựa trên các đặc trưng về tuổi, học vấn, nghề nghiệp và thông tin xã hội. Dự án bao gồm bước khám phá và xử lý dữ liệu, huấn luyện/đánh giá nhiều thuật toán Machine Learning, lưu mô hình đã huấn luyện và một ứng dụng desktop đơn giản bằng Tkinter.

> **Lưu ý:** Đây là dự án học tập/thử nghiệm. Kết quả dự đoán không phải đánh giá chính xác về thu nhập thực tế và không nên dùng làm căn cứ duy nhất cho quyết định tuyển dụng, tín dụng hoặc các quyết định quan trọng khác.

## Mục lục

- [Tính năng](#tính-năng)
- [Công nghệ sử dụng](#công-nghệ-sử-dụng)
- [Cấu trúc dự án](#cấu-trúc-dự-án)
- [Dữ liệu](#dữ-liệu)
- [Các mô hình](#các-mô-hình)
- [Cài đặt](#cài-đặt)
- [Chạy ứng dụng dự đoán](#chạy-ứng-dụng-dự-đoán)
- [Làm việc với Jupyter Notebook](#làm-việc-với-jupyter-notebook)
- [Đánh giá mô hình](#đánh-giá-mô-hình)
- [Hạn chế và hướng phát triển](#hạn-chế-và-hướng-phát-triển)

## Tính năng

- Đọc và khám phá bộ dữ liệu thu nhập.
- Làm sạch dữ liệu và chuyển đổi các biến phân loại thành đặc trưng số.
- Huấn luyện, tinh chỉnh và so sánh nhiều thuật toán phân loại.
- Đánh giá mô hình bằng Accuracy, Precision, Recall, F1-score và Confusion Matrix.
- Lưu các mô hình đã huấn luyện dưới định dạng `.pkl` bằng `joblib`.
- Cung cấp giao diện desktop Tkinter để nhập thông tin và xem kết quả dự đoán.

## Công nghệ sử dụng

- **Python**
- **Pandas, NumPy** — xử lý dữ liệu.
- **Matplotlib, Seaborn** — trực quan hóa dữ liệu và kết quả.
- **Scikit-learn** — huấn luyện, đánh giá và tối ưu mô hình.
- **XGBoost, LightGBM** — các thuật toán boosting.
- **Joblib** — lưu và tải mô hình.
- **Tkinter** — giao diện desktop.
- **Jupyter Notebook** — thực nghiệm và phân tích.

## Cấu trúc dự án

```text
final-project-v2/
├── app.py                         # Ứng dụng desktop dự đoán thu nhập
├── final-project-v3.ipynb          # Phân tích dữ liệu, huấn luyện và tối ưu mô hình
├── test-model.ipynb                # Tải các mô hình đã lưu và kiểm tra trên tập test
├── Checklist_Hệ HTQD_v4.xlsx       # Tệp checklist/tài liệu đi kèm
├── data/
│   ├── salary.csv                  # Dữ liệu gốc
│   ├── cleaned_salary.csv          # Dữ liệu sau xử lý
│   ├── X_test.csv                  # Đặc trưng của tập kiểm thử đã mã hóa
│   └── y_test.csv                  # Nhãn của tập kiểm thử
└── model/
    ├── gbm_model.pkl
    ├── grid_gb_model.pkl
    ├── grid_knn_model.pkl
    ├── grid_lr_model.pkl
    ├── grid_svm_model.pkl
    ├── rf_model.pkl
    └── xgb_model.pkl
```

## Dữ liệu

Dự án sử dụng dữ liệu dạng bảng về thu nhập với nhãn mục tiêu `salary`.

| Tệp | Kích thước quan sát được | Mục đích |
|---|---:|---|
| `data/salary.csv` | 32.561 dòng, 15 cột | Dữ liệu ban đầu |
| `data/cleaned_salary.csv` | 30.137 dòng, 13 cột | Dữ liệu sau xử lý |
| `data/X_test.csv` | 9.053 dòng, 94 đặc trưng | Đầu vào kiểm thử đã mã hóa |
| `data/y_test.csv` | 9.053 dòng, 1 cột | Nhãn kiểm thử |

Các thuộc tính trong dữ liệu gốc bao gồm tuổi (`age`), loại hình việc làm (`workclass`), trọng số mẫu (`fnlwgt`), trình độ học vấn (`education`), số năm học quy đổi (`education-num`), tình trạng hôn nhân (`marital-status`), nghề nghiệp (`occupation`), quan hệ gia đình (`relationship`), chủng tộc (`race`), giới tính (`sex`), lãi vốn (`capital-gain`), lỗ vốn (`capital-loss`), số giờ làm mỗi tuần (`hours-per-week`), quốc gia (`native-country`) và nhãn thu nhập (`salary`).

Notebook có bước tiền xử lý để chuyển các biến phân loại thành các đặc trưng số. Khi suy luận, dữ liệu đầu vào phải có cùng tập đặc trưng và đúng thứ tự như lúc huấn luyện mô hình.

## Các mô hình

Notebook thực nghiệm nhiều thuật toán, bao gồm:

- K-Nearest Neighbors (KNN)
- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- LightGBM
- Naive Bayes

Dự án có sử dụng các kỹ thuật tìm kiếm siêu tham số như `GridSearchCV` và `RandomizedSearchCV` cho một số mô hình. Các tệp trong thư mục `model/` là các mô hình đã được tuần tự hóa để tải lại và đánh giá hoặc dùng cho dự đoán.

Trong các kết quả đã lưu trong notebook, một số mô hình đạt độ chính xác khoảng **88–89%** trên tập kiểm thử. Đây là kết quả thực nghiệm của lần chạy notebook tương ứng, không phải cam kết hiệu năng trên dữ liệu mới. Hãy chạy lại toàn bộ quy trình và kiểm tra đúng mô hình/nhãn trước khi đưa ra kết luận so sánh.

## Cài đặt

Khuyến nghị sử dụng Python 3.10 hoặc 3.11 trong môi trường ảo. Tạo môi trường ảo tại thư mục dự án:

```bash
python -m venv .venv
```

Kích hoạt môi trường:

**Windows (Command Prompt):**
```bat
.venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

Cài các thư viện cần thiết:

```bash
python -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scikit-learn joblib xgboost lightgbm jupyter openpyxl
```

> Phiên bản thư viện dùng để tạo các tệp `.pkl` có thể ảnh hưởng đến khả năng tải mô hình. Nếu gặp lỗi khi chạy `joblib.load`, hãy thử môi trường tương thích với phiên bản scikit-learn/XGBoost/LightGBM được dùng lúc lưu mô hình.

## Chạy ứng dụng dự đoán

Từ thư mục gốc `final-project-v2`, chạy:

```bash
python app.py
```

Ứng dụng Tkinter cho phép nhập các trường số:

- `age`
- `fnlwgt`
- `education-num`
- `hours-per-week`

và chọn các trường phân loại như `workclass`, `education`, `marital-status`, `occupation`, `relationship`, `race`, `sex`, `native-country`. Nhấn **Dự đoán** để xem mô hình phân loại mức thu nhập `>50K` hay `<=50K`.


## Làm việc với Jupyter Notebook

Khởi chạy Jupyter từ thư mục gốc:

```bash
jupyter notebook
```

Mở `final-project-v3.ipynb` để xem các bước phân tích dữ liệu, tiền xử lý, huấn luyện, tinh chỉnh và đánh giá mô hình.

Mở `test-model.ipynb` để tải các mô hình trong `model/`, dự đoán trên `data/X_test.csv` và so sánh với `data/y_test.csv`.

Đảm bảo các đường dẫn tương đối trong notebook được chạy từ thư mục gốc của dự án. Một số cell trong notebook kiểm thử cần được rà soát để chắc chắn biến mô hình được tải và sử dụng đúng tên; nếu không, báo cáo đánh giá có thể vô tình phản ánh mô hình khác với tiêu đề phần.

## Đánh giá mô hình

Các chỉ số được sử dụng trong notebook:

- **Accuracy:** tỷ lệ dự đoán đúng trên toàn bộ mẫu.
- **Precision:** trong các mẫu được dự đoán thuộc một lớp, tỷ lệ mẫu đúng.
- **Recall:** trong các mẫu thực sự thuộc một lớp, tỷ lệ được mô hình nhận diện đúng.
- **F1-score:** trung bình điều hòa giữa Precision và Recall.
- **Confusion Matrix:** thể hiện số dự đoán đúng và sai theo từng lớp.

Khi so sánh mô hình, cần đánh giá trên cùng tập test, kiểm tra cách mã hóa nhãn và xác nhận rằng mỗi báo cáo được tạo từ đúng biến dự đoán. Không nên chỉ chọn mô hình dựa trên Accuracy.

## Hạn chế và hướng phát triển

- Đóng gói tiền xử lý và mô hình thành một `Pipeline` duy nhất để tránh sai lệch giữa dữ liệu huấn luyện và dữ liệu nhập từ giao diện.
- Chuyển đường dẫn mô hình sang đường dẫn tương đối, bổ sung kiểm tra dữ liệu đầu vào và thông báo lỗi dễ hiểu.
- Đồng bộ danh mục trong giao diện với dữ liệu huấn luyện; cân nhắc xử lý giá trị chưa từng xuất hiện.
- Kiểm tra lại các cell trong notebook kiểm thử để mỗi mô hình được đánh giá bằng chính mô hình đó.
- Bổ sung bảng tổng hợp metric cho tất cả mô hình và lưu kết quả thực nghiệm.
- Kiểm tra tính công bằng, độ lệch dữ liệu và khả năng khái quát trước khi ứng dụng vào bối cảnh thực tế.


