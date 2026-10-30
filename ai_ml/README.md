# AI/ML

A comprehensive learning and experimentation workspace for AI/ML. This repository features educational notebooks on core ML/data science libraries, real-world data analysis projects, custom ML algorithm implementations, and structured coursework from the Coursera Machine Learning Specialization.

## 🎯 Overview

This project serves as both a learning hub and a practical workspace for exploring machine learning concepts. It includes:
- **Educational experiments** with NumPy, Pandas, Seaborn, and Scikit-learn
- **Real-world projects** including house price prediction, Pokémon analysis, and Spotify track analysis
- **Custom ML implementations** built from scratch to understand algorithms deeply

## 🛠️ Technology Stack

| Library             | Version | Purpose                                    |
| ------------------- | ------- | ------------------------------------------ |
| **NumPy**           | 2.4.4   | Numerical computing and array operations   |
| **Pandas**          | 3.0.2   | Data manipulation and analysis             |
| **Scikit-learn**    | 1.8.0   | Machine learning algorithms and utilities  |
| **TensorFlow**      | 2.19.0  | Deep learning and neural network framework |
| **Matplotlib**      | 3.10.8  | Data visualization                         |
| **Seaborn**         | 0.13.2  | Statistical data visualization             |
| **SciPy**           | 1.17.1  | Scientific computing and statistics        |
| **IPython/Jupyter** | Latest  | Interactive computing environment          |


## 📁 Project Structure

```
AI-ML/
├── experiments/                          # Educational notebooks and course materials
│   ├── 01_numpy.ipynb                    # NumPy fundamentals
│   ├── 02_pandas.ipynb                   # Pandas essentials
│   ├── 03_seaborn.ipynb                  # Statistical visualization
│   ├── 04_sklearn.ipynb                  # Scikit-learn basics
│   ├── house_price_eda.ipynb             # Housing EDA
│   ├── numpy_business_example.ipynb      # Business case study
│   └── coursera_ml_course_lab/           # Structured coursework
│       └── 01_supervise_ml_regression_classification/
│           ├── 01_week/labs/             # Week 1: Python & Jupyter foundations
│           ├── 02_week/labs/             # Week 2: NumPy, multiple variables, feature scaling
│           └── 03_week/labs/             # Week 3: Classification, overfitting, regularization
├── projects/                             # Applied ML and data analysis projects
│   ├── house_price_prediction/           # Linear regression from scratch
│   ├── pokemon_analysis/                 # Pokémon EDA
│   └── spotify_track_analysis/           # Spotify track analysis
├── data/
│   ├── raw/                              # Original datasets
│   ├── processed/                        # Processed NumPy arrays
│   └── external/                         # External resources
├── notes/                                # ML concept documentation
├── outputs/                              # Reports and visualizations
├── requirements.txt                      # Python dependencies
└── README.md                             # This file
```

## 🎓 Experiments (`/experiments/`)

### Core Library Notebooks

Educational notebooks covering fundamental ML and data science libraries:

| Notebook                         | Topics                                                                | Dataset             |
| -------------------------------- | --------------------------------------------------------------------- | ------------------- |
| **01_numpy.ipynb**               | Arrays, operations, indexing, reshaping, broadcasting, linear algebra | Generated data      |
| **02_pandas.ipynb**              | DataFrames, Series, filtering, grouping, data manipulation, joins     | Sample data         |
| **03_seaborn.ipynb**             | Scatter plots, violin plots, histograms, heatmaps, distributions      | Built-in datasets   |
| **04_sklearn.ipynb**             | Logistic regression, encoding, train-test split, model evaluation     | Classification data |
| **house_price_eda.ipynb**        | Statistical summaries, distributions, correlations, visualizations    | `Housing.csv`       |
| **numpy_business_example.ipynb** | Real-world NumPy calculations and business insights                   | Synthetic data      |


### Coursera Machine Learning Course (`/experiments/coursera_ml_course_lab/`)

Structured labs from the Coursera Machine Learning Specialization (Supervised Learning: Regression & Classification)

#### Course 1: Supervised Learning - Regression & Classification
**Location:** `experiments/coursera_ml_course_lab/01_supervise_ml_regression_classification/`

**Week 1: Machine Learning Foundations**
- **Lab 01:** Python & Jupyter Notebook setup
- **Lab 02:** Model representation and linear regression
- **Lab 03:** Cost function derivation and implementation
- **Lab 04:** Gradient descent optimization algorithm

**Week 2: Advanced Regression Techniques**
- **Lab 01:** NumPy vectorization for efficient computation
- **Lab 02:** Multiple variable regression (multivariate)
- **Lab 03:** Feature scaling and learning rate optimization
- **Lab 04:** Feature engineering and polynomial regression
- **Lab 05:** Scikit-learn gradient descent implementation
- **Lab 06:** Scikit-learn normal equation approach

**Week 3: Classification & Regularization**
- **Lab 05:** Classification cost function (logistic regression)
- **Lab 06:** Gradient descent for classification
- **Lab 07:** Scikit-learn classification models
- **Lab 08:** Overfitting detection and analysis
- **Lab 09:** Regularization techniques (L1/L2)

**Utility Files:**
- `lab_utils_common.py` — Common utilities for all labs
- `lab_utils_uni.py` — Univariate regression utilities
- `plt_*.py` — Visualization helpers for logistic loss, overfit, etc.
- `deeplearning.mplstyle` — Custom Matplotlib styling
- `data.txt` — Dataset for labs

## 🚀 Projects (`/projects/`)

Applied machine learning and data analysis projects demonstrating real-world workflows.

### 1. House Price Prediction
**Location:** `projects/house_price_prediction/`

A custom implementation of linear regression with gradient descent optimization built from scratch to deeply understand the algorithm mechanics.

**Purpose:** Educational implementation demonstrating ML fundamentals and optimization techniques.

**Files:**
- `model.py` — Linear regression model with gradient descent implementation
- `train.py` — Training script with sample data and hyperparameters
- `visualize.py` — Cost function visualization (cost vs. iterations)

**Data:** `data/raw/Housing.csv`

**Technologies:** NumPy, Matplotlib

---

### 2. Pokémon Analysis
**Location:** `projects/pokemon_analysis/`

Exploratory data analysis of Pokémon statistics and characteristics.

**Purpose:** Practice EDA techniques, data visualization, and statistical analysis.

**Files:**
- `pokemon_analysis.ipynb` — Comprehensive EDA with statistics and visualizations

**Data:** `data/raw/pokemon_complete_2025.csv`

**Technologies:** Pandas, NumPy, Matplotlib, Seaborn

---

### 3. Spotify Track Analysis
**Location:** `projects/spotify_track_analysis/`

Comprehensive analysis of Spotify tracks spanning 2014-2020 with insights on release trends, collaborations, and audio characteristics.

**Purpose:** Real-world data analysis demonstrating time-series analysis, categorical insights, and business intelligence.

**Files:**
- `spotify_track_analysis.ipynb` — Full exploratory data analysis with visualizations
- **Report:** `outputs/reports/spotify_track_analysis_report.md` — Detailed findings and key insights

**Dataset Overview:**
- **Total Unique Tracks:** 1,571
- **Total Unique Artists:** 1,467
- **Year Range:** 2014–2020
- **Categories:** love, night, remix, rock, sad
- **Collaboration Rate:** 33.41%
- **Average Track Duration:** 4.37 minutes
- **Busiest Release Month:** November

**Key Findings:**
- Average duration fluctuates between 3.8–4.8 minutes across the period
- 2016–2017 show highest release volume
- Duration trends slightly downward toward 2020 (streaming optimization)
- Sad category has longest avg duration (4.67 min), Love has shortest (3.86 min)
- Right-skewed distribution with outliers exceeding 10 minutes

**Data:** `data/raw/spotify_2014_2020_dataset.csv`

**Technologies:** Pandas, NumPy, Matplotlib, Seaborn

## 📊 Data (`/data/`)

### Raw Data (`data/raw/`)
- `Housing.csv` — House pricing dataset for regression analysis and EDA
- `orders.csv` — Order transaction data
- `pokemon_complete_2025.csv` — Pokémon statistics, types, and characteristics
- `spotify_2014_2020_dataset.csv` — Spotify tracks with audio features spanning six years

### Processed Data (`data/processed/`)
- `array1.npy`, `array2.npy`, `array3.npy` — NumPy binary arrays for numerical experiments

### External Resources (`data/external/`)
- `numpy-logo.npy` — NumPy logo in binary format

## 📚 Documentation (`/notes/`)

### Concept Notes

Markdown documentation on key ML concepts and algorithms:

- **01_machine_learning_intro.md** — ML fundamentals including:
  - Types of ML algorithms (Supervised, Unsupervised, Reinforcement, Recommender Systems)
  - Supervised learning: regression vs. classification
  - Unsupervised learning: clustering and dimensionality reduction
  - Anomaly detection overview

- **02_regression_model.md** — Regression model theory and applications

- **03_gradient_descent.md** — Gradient descent optimization algorithm details

## 📈 Outputs (`/outputs/`)

### Reports
- `reports/spotify_track_analysis_report.md` — Comprehensive Spotify analysis with charts and insights

### Visualizations
- `figures/spotify/` — Charts and plots from Spotify analysis

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8+ (recommended: Python 3.10+)
- pip or conda for package management

### Installation Steps

1. **Clone or navigate to the project directory:**
   ```bash
   cd /Users/aritrachatterjee/Desktop/AI-ML
   ```

2. **Create and activate a virtual environment** (if not already done):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or on Windows:
   # venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation:**
   ```bash
   python -c "import numpy, pandas, sklearn; print('All dependencies installed successfully!')"
   ```

## 🚀 Quick Start

### Running Jupyter Notebooks

1. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Start Jupyter Lab/Notebook:**
   ```bash
   jupyter lab
   # or
   jupyter notebook
   ```

3. **Navigate to a notebook:**
   - Open `experiments/01_numpy.ipynb` to learn NumPy basics
   - Open `experiments/coursera_ml_course_lab/01_supervise_ml_regression_classification/01_week/labs/C1_W1_Lab01_Python_Jupyter_Soln.ipynb` to start the Coursera course

### Running Python Scripts

1. **House price prediction:**
   ```bash
   cd projects/house_price_prediction
   python train.py
   python visualize.py
   ```

## 📖 Learning Paths

### Beginner: Core Data Science Libraries
1. `experiments/01_numpy.ipynb` — NumPy fundamentals
2. `experiments/02_pandas.ipynb` — Pandas data manipulation
3. `experiments/03_seaborn.ipynb` — Data visualization
4. `notes/01_machine_learning_intro.md` — ML concepts

### Intermediate: Machine Learning Fundamentals
1. `experiments/coursera_ml_course_lab/01_supervise_ml_regression_classification/` (Weeks 1-3)
2. `projects/house_price_prediction/` — Hands-on regression
3. `experiments/04_sklearn.ipynb` — Scikit-learn models

### Advanced: Real-World Projects
1. `projects/pokemon_analysis/` — EDA practice
2. `projects/spotify_track_analysis/` — Time-series and categorical analysis
3. Coursera Week 2-3 labs — Advanced classification and regularization

## 📝 Project Statistics

| Category            | Count |
| ------------------- | ----- |
| Jupyter Notebooks   | 14+   |
| Python Scripts      | 3+    |
| Datasets            | 4     |
| Documentation Files | 3     |
| Coursera Labs       | 15+   |
| Dependencies        | 20+   |


## 🎯 Use Cases

- **Learning ML concepts** from fundamentals to advanced topics
- **Practicing data analysis** with real-world datasets
- **Building custom ML models** from scratch
- **Understanding algorithms** through hands-on implementation
- **Portfolio building** with complete project examples

## 🔧 Troubleshooting

### Virtual Environment Issues
If you encounter import errors, ensure the virtual environment is activated:
```bash
source venv/bin/activate  # macOS/Linux
```

### Jupyter Not Found
If Jupyter won't start, reinstall it:
```bash
pip install --upgrade jupyter jupyterlab
```

### Missing Dependencies
If notebooks fail with import errors, update all packages:
```bash
pip install --upgrade -r requirements.txt
```

### macOS-Specific Issues
Some packages may require additional system dependencies. If installation fails, try:
```bash
brew install python@3.10
```

## 📚 Additional Resources

### Coursera Machine Learning Specialization
- **Instructor:** Andrew Ng
- **Focus:** Supervised Learning (Regression & Classification)
- **Platform:** Coursera
- **Course Structure:** 3+ weeks of video lectures + practical labs

### Key Concepts Covered
- Linear regression and gradient descent
- Multiple variable regression
- Feature scaling and normalization
- Logistic regression for classification
- Overfitting detection
- Regularization techniques (L1/L2)
- Scikit-learn library usage

### External Resources
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Matplotlib Tutorials](https://matplotlib.org/tutorials/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples.html)

## 📋 Directory Reference

**Quick file lookup:**
- 🔍 **Learning ML?** → Start with `notes/01_machine_learning_intro.md`
- 📊 **NumPy practice?** → Open `experiments/01_numpy.ipynb`
- 🏠 **Linear regression?** → Check `projects/house_price_prediction/`
- 🎵 **Data analysis?** → See `projects/spotify_track_analysis/`
- 🎓 **Coursera labs?** → Go to `experiments/coursera_ml_course_lab/`
- 📈 **Visualizations?** → Browse `outputs/figures/spotify/`

## ✨ Features

✅ Educational notebooks with clear explanations  
✅ Real-world datasets for practice  
✅ Custom ML implementations  
✅ Coursera ML course integration  
✅ Comprehensive documentation  
✅ Project-based learning structure  
✅ Easy setup and reproducibility  

## 📝 Notes

- All notebooks include detailed explanations and comments
- Coursera labs are pre-solved and annotated
- Datasets are included and ready to use
- The project uses Python 3.10+ conventions
- Jupyter Lab is recommended for the best notebook experience

---

**Last Updated:** April 2026  
**Status:** Active - Continuously updated with new experiments and projects

## 📈 Outputs (`/outputs/`)

### Reports
- `outputs/reports/spotify_track_analysis_report.md` — Comprehensive Spotify analysis findings

### Figures
- `outputs/figures/spotify/` — Visualizations and charts from Spotify analysis

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Installation

1. **Clone or navigate to the project:**
   ```bash
   cd /Users/aritrachatterjee/Desktop/AI-ML
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   **Key packages:**
   - `numpy` — Numerical computing
   - `pandas` — Data manipulation and analysis
   - `matplotlib` — Plotting library
   - `seaborn` — Statistical data visualization
   - `scikit-learn` — Machine learning library
   - `jupyter` — Interactive notebooks

   A complete list of dependencies with versions is available in `requirements.txt`.

## 📖 How to Run

### Jupyter Notebooks
```bash
jupyter notebook experiments/
```

Then navigate to the notebook you want to run.

### Python Scripts
```bash
# Train house price prediction model
python projects/house_price_prediction/train.py

# Visualize training results
python projects/house_price_prediction/visualize.py
```

## 🎯 Learning Path

**Recommended progression:**

1. **Start with experiments:**
   - `01_numpy.ipynb` — Foundation for numerical computing
   - `02_pandas.ipynb` — Data manipulation skills
   - `03_seaborn.ipynb` — Visualization techniques
   - `04_sklearn.ipynb` — Machine learning basics

2. **Explore projects:**
   - `house_price_eda.ipynb` — Applied EDA
   - `pokemon_analysis.ipynb` — Dataset exploration
   - `spotify_track_analysis.ipynb` — Complex analysis

3. **Study implementations:**
   - `house_price_prediction/` — Custom algorithm implementation
   - `notes/` — Theoretical foundations

---