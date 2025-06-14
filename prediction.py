# --------------------------------------------
# Proyek Penerapan Data Science:
# Prediksi Attrition (Pengunduran Diri Karyawan)
# Studi Kasus: Perusahaan Jaya Jaya Maju
# Disusun oleh: Muchammad Wildan Alkautsar
# --------------------------------------------

import pandas as pd
import pickle

# --------------------------------------------
# Load model yang sudah disimpan (Pipeline Logistic Regression)
# --------------------------------------------
MODEL_PATH = "model/attrition_model.pkl"

try:
    with open(MODEL_PATH, "rb") as file_model:
        model = pickle.load(file_model)
except FileNotFoundError:
    print(f"File model tidak ditemukan di: {MODEL_PATH}")
    exit(1)

# --------------------------------------------
# Data baru untuk diprediksi (satu orang karyawan)
# --------------------------------------------
data_baru = pd.DataFrame(
    [
        {
            "DistanceFromHome": 10,
            "EnvironmentSatisfaction": 3,
            "JobInvolvement": 3,
            "JobLevel": 1,
            "JobSatisfaction": 3,
            "MonthlyIncome": 2000,
            "OverTimeNum": 1,
            "PerformanceRating": 3,
            "PercentSalaryHike": 117,
            "RelationshipSatisfaction": 4,
            "TotalWorkingYears": 20,
            "WorkLifeBalance": 4,
            "YearsAtCompany": 3,
            "YearsSinceLastPromotion": 6,
        }
    ]
)

# --------------------------------------------
# Prediksi dan interpretasi hasil
# --------------------------------------------
prediksi = model.predict(data_baru)[0]
probabilitas = model.predict_proba(data_baru)[0]

status = "LEAVE (Mengundurkan Diri)" if prediksi == 1 else "STAY (Tetap Bekerja)"

print("===== HASIL PREDIKSI ATTRITION =====")
print(f"Prediksi Karyawan: {prediksi} → {status}")
print(f"Probabilitas [Stay, Leave]: {probabilitas}")
print("====================================")
