# 📌 Question Classification

## 🔍 Overview
This project focuses on classifying Vietnamese questions into predefined categories using **Natural Language Processing (NLP)**. The model was trained on a custom dataset and optimized to improve classification accuracy for better information retrieval.

## ✨ Features
- ✅ **Multi-class Text Classification** – Categorizes questions into **8 predefined types** (e.g., Who, What, Why, When).
- 📊 **Custom Dataset** – Built with **1,200 labeled questions** specifically for Vietnamese text processing.
- 🔠 **Feature Engineering** – Utilized **TF-IDF vectorization** and **word embeddings** for better text representation.
- 🤖 **Machine Learning Models** – Implemented and compared **Logistic Regression, SVM, and LSTM-based models**.
- 🎯 **Performance Evaluation** – Achieved **90% accuracy** on the test dataset.

## 🛠 Technologies Used
- 🐍 **Programming Language**: Python
- 📚 **Libraries**: NLTK, Scikit-learn, TensorFlow, Pandas, NumPy
- 🔡 **Text Processing**: TF-IDF, Word2Vec, FastText
- 🤖 **Machine Learning Models**: Logistic Regression, SVM, LSTM

## 🚀 Installation
### 🔧 Prerequisites
Ensure Python is installed (recommended version: **3.8+**)

```bash
pip install nltk scikit-learn tensorflow pandas numpy
```

## ▶️ Usage
1. 📥 Clone the repository:
```bash
git clone https://github.com/yourusername/Question-Classification.git
cd Question-Classification
```
2. 🏃 Open and run the `logistic_regression.ipynb` notebook:
   - Modify the code to input your own question for classification.
   - Alternatively, use `new_data.xlsx` to classify multiple questions at once.
3. ⚙️ Adjust preprocessing or model hyperparameters in the notebook as needed.
Run the `logistic_regression.ipynb` notebook. Modify the code to input your desired question for classification, or use the `new_data.xlsx` file to classify multiple questions at once.

## 📝 Example Input & Output
```python
question = "Nếu được cho 5 điều ước, bạn sẽ ước gì?"
predicted_label = predict_question_type(question)

print(f"Câu hỏi: {question}")
print(f"Dự đoán nhãn: {predicted_label}")
```
**🟢 Output:**
```
Câu hỏi: Nếu được cho 5 điều ước, bạn sẽ ước gì?
Dự đoán nhãn: What
```

## 🔮 Future Improvements
- 📈 Expand the dataset to cover more complex question structures.
- ⚡ Implement transformer-based model like **PhoBERT for improved performance.
- 🌐 Develop a web API for real-time classification.

