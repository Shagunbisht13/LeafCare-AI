# LeafCare AI

> An automated plant leaf disease diagnostic and treatment recommendation toolkit leveraging computer vision EDA, exploratory dataset profiling, and botanical remediation mapping.

*(Formerly repository `AI-Driven-leaf-Detection-Project`)*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Domain](https://img.shields.io/badge/Domain-AgriTech%20%7C%20Computer%20Vision-2ea44f.svg)](#)

---

## 📌 Overview

**LeafCare AI** provides data exploration, image profiling, web scraping, and remediation mapping pipelines for plant leaf disease datasets. It processes multi-split agricultural image collections (train, test, validation), inspects image dimensions and class distributions, visualizes randomly sampled infected leaf specimens, and provides an integrated agronomic treatment database mapping 60 distinct plant disease categories to actionable interventions.

---

## 🚀 Features

- **Automated Dataset Dimension Profiling (`count_images.py`)**: Computes total sample counts, minimum, maximum, and average pixel resolutions across `train`, `test`, and `validation` splits.
- **Random Sample Visualizer**: Generates annotated 3x3 Matplotlib visualization grids of diagnosed leaf samples labeled by biological disease class.
- **Agronomic Treatment Knowledge Base (`plant_disease_treatments.csv`)**: Structured reference dataset covering 60 crop disease classes (e.g., Apple Scab, Corn Northern Leaf Blight, Grape Black Rot, Tomato Early Blight) paired with recommended chemical/organic remedies.
- **Botanical Data Scraping (`SCRAPPING_PLANT.ipynb`)**: Automated crawling and Wikipedia API integration extracting scientific plant taxonomies, symptoms, and traditional treatments.
- **Image Preprocessing & Augmentation Workflows (`images_pro.ipynb`, `PROJECT.ipynb`)**: Notebook workflows for image cleaning, labeling, and preliminary dataset structuring.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Language** | Python 3.10+ |
| **Image Processing** | Pillow (PIL), Matplotlib |
| **Data Handling** | Pandas |
| **Notebook Workflows** | Jupyter Notebook |
| **Web Scraping** | BeautifulSoup4, Requests, Wikipedia-API |

---

## 📂 Project Structure

```text
LeafCare-AI/
├── .gitignore                     # Git ignore rules for large datasets and caches
├── count_images.py                # Dataset EDA: image counter, dimension profiler & sample visualizer
├── images_pro.ipynb               # Image preprocessing and data transformation notebook
├── plant_disease_treatments.csv   # Lookup table of 60 crop diseases and remediation steps
├── Project Proposal.docx          # Academic project charter and problem definition
├── PROJECT.ipynb                  # Exploratory model experimentation notebook
├── README.md                      # Project documentation
├── requirements.txt               # Python package dependencies
└── SCRAPPING_PLANT.ipynb          # Botanical web scraping and knowledge gathering
```

---

## ⚙️ Setup and Run Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Shagunbisht13/LeafCare-AI.git
cd LeafCare-AI
```

### 2. Set Up a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare Dataset

Download the [Kaggle Leaf Disease Dataset Combination](https://www.kaggle.com/datasets/asheniranga/leaf-disease-dataset-combination) and organize your image directory as follows:

```text
LeafCare-AI/
└── image data/
    ├── train/
    │   ├── Apple___Apple_scab/
    │   └── ...
    ├── test/
    └── validation/
```

*(Alternatively, set the environment variable `LEAF_DATASET_PATH` to point to any custom dataset path).*

---

## 💻 Usage

### Run Dataset Dimensional Profiling & Sample Display

Execute the automated EDA script:

```bash
python count_images.py
```

Sample CLI output:

```text
LeafCare AI - Scanning dataset at: .../image data

[Folder] .../train
Total Images: [TODO: run on local dataset]
Minimum Size: (256, 256)
Maximum Size: (256, 256)
Average Size: (256, 256)
```

### Querying Treatment Recommendations in Python

```python
import pandas as pd

df = pd.read_csv("plant_disease_treatments.csv")
remedy = df[df["Disease Name"] == "apple apple scab"]["Recommended Treatment"].values[0]
print(f"Treatment: {remedy}")
# Output: Treatment: Fungicide sprays (captan, myclobutanil)
```

---

## 📸 Screenshots

<!-- Replace placeholders with actual screenshots from your local run -->
| Dataset Sample Grid (3x3) | Treatment Lookup & EDA |
| :---: | :---: |
| `![Sample Grid Placeholder](https://via.placeholder.com/450x300.png?text=LeafCare+AI+Sample+Grid)`<br>*(Annotated 9-sample leaf disease visualizer)* | `![Treatment Lookup Placeholder](https://via.placeholder.com/450x300.png?text=Treatment+Lookup+Table)`<br>*(Agronomic treatment advisory mapping)* |

---

## ⚠️ Limitations

- **Dataset Size**: High-resolution leaf imagery cannot be hosted directly inside this Git repository due to GitHub file size constraints; users must supply their own local directory or Kaggle dataset.
- **Notebook-Centric Inference**: Model experimentation is currently contained in Jupyter notebooks (`PROJECT.ipynb`, `images_pro.ipynb`) and requires an active Jupyter kernel rather than a single turnkey command.
- **Benchmark Accuracy**: [TODO: add test accuracy / validation F1 score once final model training benchmark is finalized].

---

## 🔮 Future Improvements

- [ ] Wrap the image preprocessing and treatment lookup into a standalone interactive **Streamlit web application**.
- [ ] Export trained deep learning weights into an **ONNX / TensorFlow Lite** model for offline mobile inference on edge devices.
- [ ] Implement an automated REST endpoint using **FastAPI** to accept camera uploads from farmers and return disease predictions with recommended treatments in JSON.
