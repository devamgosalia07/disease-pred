# Multiple Disease Predictor Web App
* Machine learning based web appto predict multiple diseases based on input data.
* Web app hosted with Streamlit having multiple pages. Each page takes input for particular disease and that data fed to the model trained for that disease.
* Used multiple datasets to train multiple ML models with Logistic regression, SVM and Random Forestfor predicting diseases and deployed them using pickle. 
* Exposure: Streamlit, Random Forest, SVM , Logistic Regression.

# Logistic Regression
* It is a classification algorithm that predicts the probability of an instance belonging to a certain class.
* The fundamental idea behind logistic regression is to model the relationship between the input variables (also known as features or independent variables) and the probability of the output variable (also known as the dependent variable or target class). The output variable is binary, meaning it has two possible outcomes or classes (e.g., 0 or 1, true or false, yes or no).
* To perform logistic regression, the algorithm applies the logistic function, also called the sigmoid function, to a linear combination of the input variables. The sigmoid function maps the linear combination to a value between 0 and 1, which represents the predicted probability of the instance belonging to the positive class.
![1_klFuUpBGVAjTfpTak2HhUA](https://github.com/Anikaaasingh/Disease-Prediction/assets/96921017/84fd8e6a-e01b-44fe-b567-f75a12877914)

# SVM
* Support Vector Machines (SVM) is a powerful and widely used machine learning algorithm for classification tasks. It is particularly effective when dealing with complex datasets and nonlinear decision boundaries.
* The main idea behind SVM is to find an optimal hyperplane that separates the data into different classes with the maximum margin. This hyperplane acts as a decision boundary, where instances on one side are classified as one class, and instances on the other side are classified as the other class. The "support vectors" are the data points closest to the decision boundary and play a crucial role in defining it.
* SVM can handle both linearly separable and nonlinearly separable datasets by employing the kernel trick. The kernel trick allows SVM to transform the input data into a higher-dimensional feature space, where a linear decision boundary can be found. This transformation is performed implicitly, without explicitly calculating the coordinates of the new feature space, thanks to the use of kernel functions. Popular kernel functions include linear, polynomial, radial basis function (RBF), and sigmoid.
![support-vector-machine-algorithm](https://github.com/Anikaaasingh/Disease-Prediction/assets/96921017/57c2dc96-bfaf-4b9f-93d7-448633318f0b)

# Random Forest
* Random Forest is a popular ensemble learning algorithm used for classification tasks. It combines the power of decision trees with the concept of randomness to create a robust and accurate model.
* The fundamental idea behind a Random Forest is to build multiple decision trees and combine their predictions to make the final classification. Each decision tree in the forest is constructed using a random subset of the training data and a random subset of the input features. This randomness helps to reduce overfitting and improve the model's generalization ability.

![download](https://github.com/Anikaaasingh/Disease-Prediction/assets/96921017/86082adb-abdd-4276-a899-dd20556e33ab)

# Working Web App
* Enter the required data to get the output.
![Screenshot (340)](https://github.com/Anikaaasingh/Disease-Prediction/assets/96921017/fd49c5c8-6de5-43c3-8619-c838a041f5ca)

# Future Works
* More types of diseases can be added for prediction.
* Better models can be used to achieve more accuracy.

