# Machine Learning-Driven Network Intrusion Detection System (NIDS)

## 1. Project Overview
This project implements an intelligent, automated Network Intrusion Detection System (NIDS) driven by supervised machine learning algorithms. Operating similarly to a digital security camera system, the network pipeline performs real-time inspection of incoming data packet traffic to instantly distinguish standard, secure connections from active cyberattacks. 

The primary objective is to transition network defense away from rigid, legacy rule-based signatures that fail against slight variations of modern threats. Instead, this system leverages mathematical pattern recognition to evaluate traffic behavior across 41 multi-dimensional features, ensuring automated anomaly detection at scale.

## 2. Dataset Architecture
The system is trained and evaluated using the **NSL-KDD dataset**, an internationally recognized academic security benchmark compiled by the Canadian Institute for Cybersecurity (CIC) at the University of New Brunswick. 

NSL-KDD resolves severe structural flaws inherent in the classic KDD Cup 99 dataset. The original data contained a massive volume of duplicate connection records that artificially inflated machine learning accuracy and created deceptive evaluations. The NSL-KDD dataset cleans this distribution, removing duplicates to establish a mathematically rigorous training environment.

### 2.1 Traffic Categorization
The ingestion pipeline cleans and preprocesses raw network telemetry logs, mapping complex connection data into five distinct, high-level macro-categories:
1. **Normal:** Legitimate user activities, including standard web browsing, routine database requests, and email communications.
2. **Denial of Service (DoS):** Volumetric resource-exhaustion floods designed to crash target servers and take services offline.
3. **Probe:** Reconnaissance and scanning activities (such as port scanning) where an attacker maps network architectures to discover open ports and vulnerabilities.
4. **Remote to Local (R2L):** Unauthorized external exploitation attempts where an outsider tries to gain local network user privileges.
5. **User to Root (U2R):** Internal privilege escalation threats where a low-level user attempts to exploit system bugs to hijack root or administrator control.

## 3. Machine Learning Framework
This project applies a rigorous systems engineering approach by evaluating and benchmarking three separate tree-based ensemble models trained under identical parameters:

*   **Random Forest:** A parallel ensemble method that builds hundreds of independent decision trees via Bootstrap Aggregating (Bagging) and maps predictions via majority voting. This architecture minimizes variance and offers consistent baseline stability.
*   **Extra Trees (Extremely Randomized Trees):** A highly randomized cousin of Random Forest that selects feature split thresholds entirely at random rather than optimizing them mathematically. This approach drastically minimizes training time while preventing overfitting to transient data noise.
*   **XGBoost (Extreme Gradient Boosting):** A sequential ensemble framework that trains weak decision trees iteratively. Each new model explicitly uses gradient descent optimization to correct the residual errors left behind by its predecessor, maximizing detection sensitivity on complex data structures.

### 3.1 Architectural Evaluation Matrix

| Metric / Feature | Random Forest | Extra Trees | XGBoost |
| :--- | :--- | :--- | :--- |
| **Tree Construction** | Parallel (Independent) | Parallel (Independent) | Sequential (Iterative) |
| **Splitting Mechanism** | Calculates optimal splits | Selects thresholds at random | Minimizes loss function via gradient descent |
| **Primary Strength** | Exceptional stability and low variance | Maximum computational speed and throughput | High Catch Rate (Recall) on rare attack signatures |

## 4. Key Engineering Objectives
*   **Multi-Dimensional Pattern Recognition:** Automatically processes complex mathematical indicators (such as protocol flags, source/destination packet bytes, and connection duration) that are impossible for human security teams to audit manually.
*   **Handling Class Imbalance:** Benchmarks model performance on low-frequency, high-severity threat vectors (U2R and R2L) which are statistically buried by overwhelming volumes of normal traffic rows.
*   **Algorithmic Generalization:** Verifies model adaptability using testing subsets that contain novel, unseen variation strategies to simulate real-world zero-day network protection.

## 5. Repository Structure
*   `data/` : Directory structures containing the NSL-KDD data subsets.
*   `preprocessing.py` : Scripts for scaling numerical values, encoding categorical strings, and mapping targets.
*   `train.py` : Core script implementing cross-validation, hyperparameter tuning, and ensemble training.
*   `evaluate.py` : Benchmarking engine generating precision, recall, confusion matrices, and final performance metrics.
