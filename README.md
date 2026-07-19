**Evaluating Ensemble Robustness in Medical Classification: A Comparative Analysis of Decision Trees and Random Forests on the Heart Disease Dataset**
**Abstract**
Predicting cardiovascular diseases with high accuracy and robustness remains a critical objective in clinical decision support systems. While individual decision trees offer high interpretability, they are notoriously susceptible to high variance and overfitting. This study investigates the performance of a baseline Decision Tree against a Random Forest classifier using the heart_h (Heart Disease) dataset. Our baseline Decision Tree achieved a limited accuracy of 50.00% and an F1 Score of 29.00%. In contrast, the proposed Random Forest model achieved a significantly higher accuracy of 81.36% and an F1 Score of 81.01%. These results demonstrate that the ensemble learning approach provides superior generalization and robustness for heart disease classification.

**1. Introduction**
Heart disease is one of the leading causes of mortality globally, necessitating the development of reliable predictive models to assist clinicians in early diagnostic decisions. In recent years, machine learning algorithms have been widely adopted to identify risk factors and predict clinical outcomes. However, the choice of classifier remains a pivotal design challenge.

Recent research, such as the llm-trees project (Knauer et al., 2024), has highlighted how structural decision trees can be induced even under zero-shot conditions using large language models. While interpretable decision boundaries are critical in medical diagnostics, standard decision trees are prone to instability, where small perturbations in the dataset can lead to major structural variations. Consequently, ensemble methodologies that aggregate multiple estimators, such as Random Forests, present a compelling alternative to improve generalization. This paper analyzes the empirical performance gap between these two methodologies on the heart_h dataset.

**2. Methodology**
We implemented and compared two models:

**Baseline Decision Tree**:A single classifier that splits the feature space recursively based on information gain or Gini impurity. While highly interpretable, a single tree's depth often captures noise in the training set, leading to overfitting and low predictive reliability on unseen clinical records.
**Proposed Random Forest**: An ensemble method consisting of a multitude of decision trees. It reduces variance and controls overfitting by employing two key techniques:
**Bootstrap Aggregating (Bagging)**: Training each tree on a random sample of the dataset with replacement.
**Random Subspace Method**: Selecting a random subset of features at each split candidate, ensuring that individual trees are decorrelated.
The final prediction is determined via majority voting across all constituent trees, mitigating the inherent instability of individual trees.

**3. Results**
Both models were trained and evaluated on the heart_h dataset. The classification performance metrics are summarized in Table 1 below.

**Table 1: Classification Performance Summary**

                  **ModelAccuracy**  **F1 Score**   
**Decision Tree (Baseline)	50.00%	29.00%
Random Forest (Alternative)	81.36%	81.01%**
As shown in Table 1, the baseline Decision Tree performed poorly, exhibiting an accuracy of 50.00%—equivalent to random chance in binary classification—and a low F1 Score of 29.00%, which indicates a high rate of false negatives or false positives. In contrast, the Random Forest model demonstrated a substantial improvement, achieving an accuracy of 81.36% and an F1 Score of 81.01%. The balanced F1 score indicates that the ensemble approach handles class imbalances effectively, resulting in stable precision and recall.

**4. Conclusion**
This study confirms that a single Decision Tree is insufficient for the complex, non-linear relationships present in clinical data such as the heart_h dataset. By aggregating diverse, decorrelated trees, the Random Forest model successfully resolves the overfitting and instability issues of the baseline. The ensemble approach achieved an absolute accuracy gain of 31.36% and an F1 Score gain of 52.01%, demonstrating its viability as a robust diagnostic tool in clinical settings. Future work will explore integrating LLM-induced decision boundaries as prior knowledge in ensemble frameworks, building on the concepts introduced in the llm-trees library.

**References**
Knauer, R., Koddenbrock, M., Wallsberger, R., Brisson, N. M., Duda, G. N., Falla, D., Evans, D. W., & Rodner, E. (2024). “Oh LLM, I'm Asking Thee, Please Give Me a Decision Tree”: Zero-Shot Decision Tree Induction and Embedding with Large Language Models. arXiv preprint arXiv:2409.18594. https://arxiv.org/abs/2409.18594
**GitHub Repository: ml-lab-htw/llm-trees https://github.com/ml-lab-htw/llm-trees**
