import pandas as pd
from sklearn.model_selection import train_test_split
import os
import re

# Đường dẫn đến thư mục data
data_dir = "Data"
raw_file_path = os.path.join(data_dir, "D:\\NLP NMH\\Data\\raw_data.xlsx")

# Đọc dữ liệu từ raw_data.xlsx
data = pd.read_excel(raw_file_path)

# Kiểm tra dữ liệu
print(f"Tổng số mẫu: {len(data)}")
print(data.head())

# Hàm tiền xử lý dữ liệu
def preprocess_text(text):
    text = re.sub(r'\s+', ' ', str(text))  # Loại bỏ khoảng trắng thừa
    text = text.strip().lower()           # Chuyển về chữ thường
    text = re.sub(r'[^\w\s]', '', text)   # Loại bỏ ký tự đặc biệt
    return text

# Tạo dataframe mới với dữ liệu đã tiền xử lý
preprocessed_data = pd.DataFrame({
    'Processed_Question': data['Question'].apply(preprocess_text),
    'Label': data['Label']
})

# Đường dẫn lưu tệp dữ liệu đã xử lý
preprocessed_file_path = os.path.join(data_dir, "preprocessed_data.xlsx")

# Lưu dữ liệu đã xử lý vào tệp Excel
preprocessed_data.to_excel(preprocessed_file_path, index=False)
print(f"Dữ liệu đã xử lý được lưu vào: {preprocessed_file_path}")

# Chia dữ liệu thành train (70%), val (15%), test (15%)
train, temp = train_test_split(data, test_size=0.3, random_state=42, stratify=data['Label'])
val, test = train_test_split(temp, test_size=0.5, random_state=42, stratify=temp['Label'])

# In số lượng mẫu trong từng tập
print(f"Số lượng mẫu trong tập train: {len(train)}")
print(f"Số lượng mẫu trong tập validation: {len(val)}")
print(f"Số lượng mẫu trong tập test: {len(test)}")

# Đường dẫn lưu các tệp mới
train_path = os.path.join(data_dir, "train.xlsx")
val_path = os.path.join(data_dir, "val.xlsx")
test_path = os.path.join(data_dir, "test.xlsx")

# Lưu dữ liệu ra các tệp Excel
train.to_excel(train_path, index=False)
val.to_excel(val_path, index=False)
test.to_excel(test_path, index=False)

print("Dữ liệu đã được chia và lưu vào các tệp:")
print(f"- {train_path}")
print(f"- {val_path}")
print(f"- {test_path}")

# Kiểm tra lại các biến sau khi chia và lưu tệp
assert os.path.exists(train_path), "Tệp train.xlsx không tồn tại!"
assert os.path.exists(val_path), "Tệp val.xlsx không tồn tại!"
assert os.path.exists(test_path), "Tệp test.xlsx không tồn tại!"