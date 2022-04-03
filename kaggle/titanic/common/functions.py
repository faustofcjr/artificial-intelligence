import matplotlib.pyplot as plt

from sklearn import (
    metrics, 
    model_selection
)

from sklearn.model_selection import (
    RepeatedStratifiedKFold,
    RepeatedKFold
)

from sklearn.model_selection import (
    GridSearchCV,
    RandomizedSearchCV
)

def show_model_result(clf, X, y, y_test, y_predict):
    
    #############################################################################
    #                 Computing cross-validated metrics                         #
    #############################################################################
    print("\nComputing cross-validated metrics")
    print("----------------------------------------------------------------------")
    scores = model_selection.cross_val_score(clf, X, y)
    print("Scores:", scores)
    print("Mean = %0.2f / Standard Deviation = %0.2f" % (scores.mean(), scores.std()))      


    ##################################################################################################################
    #                                              Evaluating Model                                                  #
    #   Confunsion Matrix (https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)  #
    ##################################################################################################################
    print("\nConfunsion Matrix")
    print("----------------------------------------------------------------------")
    matrix = metrics.confusion_matrix(y_test, y_predict)
    print(matrix)

    
    #############################################################################
    #                         Classification Report                             #
    #############################################################################
    print("\nClassification Report")
    print("----------------------------------------------------------------------")
    print(metrics.classification_report(y_test, y_predict))
        
 
    #############################################################################
    #                            Model Measurements                             #
    #############################################################################
    print("----------------------------------------------------------------------")
    print("Accuracy: %0.2f" % metrics.accuracy_score(y_test, y_predict))
    print("Precicion: %0.2f" % metrics.precision_score(y_test, y_predict))
    print("Sensitivity aka Recall: %0.2f" % metrics.recall_score(y_test, y_predict))
    print("F1-Score: %0.2f" % metrics.f1_score(y_test, y_predict))


def show_curve_roc(clf, X_test, y_test, y_predict, label="Curve ROC"):
    
    #############################################################################
    #                         AUC-Area Under the ROC                            #
    #############################################################################
    print("----------------------------------------------------------------------")
    print("AUC-Area Under the ROC Curve: %0.2f" % metrics.roc_auc_score(y_test, y_predict))
    print("----------------------------------------------------------------------")

    #############################################################################
    #                                Curve ROC                                  #
    #############################################################################
    clf_prob = clf.predict_proba(X_test)
    probs = clf_prob[:, 1]
    rfp, rvp, lim = metrics.roc_curve(y_test, probs)

    plt.plot(rfp, rvp, marker=".", label="label", color="green")
    plt.plot([0,1],[0,1], color="darkblue", linestyle="--")

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")

    plt.show()


def show_best_hyperparameter_optimization(clf, space, X, y, n_splits=10, n_repeats=3, random_state=1, scoring="accuracy", n_jobs=-1):
    """
    Hyperparameter Optimization
    Note: The execution of the code below may take a few minutes or hours.
    """
    cv = RepeatedStratifiedKFold(n_splits=n_splits, n_repeats=n_repeats, random_state=random_state)
    gs = GridSearchCV(clf, space, cv=cv, scoring=scoring, n_jobs=n_jobs)
    result_gs = gs.fit(X, y)

    print('Best Score: %s' % result_gs.best_score_)
    print('Best Hyperparameters: %s' % result_gs.best_params_)