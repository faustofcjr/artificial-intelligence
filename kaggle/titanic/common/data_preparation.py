from sklearn.model_selection import (
    RepeatedStratifiedKFold,
    RepeatedKFold
)

from sklearn.model_selection import (
    GridSearchCV,
    RandomizedSearchCV
)


def fill_age(dataset, mean=None):
    """
    Fill in missing age feature with mean.
    
    Parameters
    ----------
    dataset : Pandas DataFrame
        The dataframe that contains "Age" column
    mean : 
    """
    if mean == None:
        mean = dataset["Age"].mean()
    
    dataset["Age"].fillna(mean, inplace=True)

    
def get_age_group(dataset):
    """
    Determine the age group of passengers.
    
    Age groups are classified as:

    - CHILD: Between 0 and 12;
    - TEENAGER: Between 13 and 17;
    - ADULT: Between 18 and 59;
    - ELDERLY: greater than and equal to 60.
    
    Parameters
    ----------
    dataset : Pandas DataFrame
        The dataframe that contains "Age" columns.
    
    return
    ----------
    ageGroups : list
        A list with the same order or index dataset.
    """
    ageGroups = []
    
    for index, row in dataset.iterrows():
        age = row["Age"]
        
        if age <= 12:
            ageGroups.append("CHILD")
        if age > 12 and age < 18:
            ageGroups.append("TEENAGER")
        if age >= 18 and age < 60:
            ageGroups.append("ADULT")
        if age >= 60:
            ageGroups.append("ELDERLY")
    
    return ageGroups
    
    

def add_family_name(dataset):
    """
    To each passeger, get you family name and add it in a new
    column callled FamilyName.
    
    Parameters
    ----------
    dataset : Pandas DataFrame
        The dataframe that contains "Name" column
    """
    names = dataset["Name"]
    surnames = []

    for name in names:
        surname = name.split(",")[0]
        surnames.append(surname.strip())
    
    dataset["FamilyName"] = surnames
    

    
def get_passengers_per_sex(dataset):
    """
    Group by dataset by sex.

    Parameters
    ----------
    dataset : Pandas DataFrame
        The dataframe that contains "Sex" column

    return
    ----------
    group_sex : Pandas DataFrame
        A dataframe with "Sex" and "Total" columns
    """
    group_sex = dataset.groupby(["Sex"]).size()
    return group_sex.reset_index(name="Total")


def get_survivors_per_sex(dataset):
    """
    Group by dataset whith survived by sex.

    Parameters
    ----------
    dataset : Pandas DataFrame
        The dataframe that contains "Sex" and "Survived" columns

    return
    ----------
    group_survived_sex : Pandas DataFrame
        A dataframe with "Sex", "Survived" and "Total" columns
    """

    group_survived_sex = dataset.groupby(["Sex", "Survived"]).size()
    return group_survived_sex.reset_index(name="Total")


def get_survivors_per_class(dataset):
    """
    Group by dataset whith survived by Ticket class.

    Parameters
    ----------
    dataset : Pandas DataFrame
        The dataframe that contains "Pclass" and "Survived" columns

    return
    ----------
    group_survived_pclass : Pandas DataFrame
        A dataframe with "Pclass", "Survived" and "Total" columns
    """
    group_survived_pclass = dataset.groupby(["Pclass", "Survived"]).size()
    return group_survived_pclass.reset_index(name="Total")


def get_total_features(dataset, features):
    """
    Group by dataset by array features.

    Parameters
    ----------
    dataset : Pandas DataFrame
        The dataframe that contains "Pclass" and "Survived" columns
    features : array
        Collection of columuns

    return
    ----------
    group : Pandas DataFrame
        A dataframe with features and "Total" columns
    """
    group = dataset.groupby(features).size()
    return group.reset_index(name="Total")


def calc_survival_change(dataset, decimal=2):
    """
    Calculate the chance that a group made up of passengers of the same sex 
    belonging to the same to have survived.

    Parameters
    ----------
    dataset : Pandas DataFrame
        The dataframe that contains "Sex", "Pclass" and "Survived" columns.
    decimal :int
        Decimal Places used to round result.
    
    return
    ----------
    list_survival_change : list
        A list with the same order or index dataset.
    """
    
    list_survival_change = []

    for index, row in dataset.iterrows():
        sex, pclass =  row["Sex"], row["Pclass"]

        count_sex_class = dataset[(dataset.Sex == sex) & (dataset.Pclass == pclass)]
        count_sex_class_survived = dataset[(dataset.Survived == 1) & (dataset.Sex == sex) & (dataset.Pclass == pclass)]
   
        survival_change =  len(count_sex_class_survived) / len(count_sex_class)
        survival_change = round(survival_change, decimal)
        list_survival_change.append(survival_change)

    return list_survival_change

def show_best_hyperparameter_optimization(clf, space, X, y, n_splits=10, n_repeats=3, random_state=1, scoring="accuracy", n_jobs=-1):
    """
    Hyperparameter Optimization

    Note: The execution of the code below may take a few minutes or hours.

    Uncomment and run it when you need to optimize hyperparameters.
    """
    cv = RepeatedStratifiedKFold(n_splits=n_splits, n_repeats=n_repeats, random_state=random_state)
    gs = GridSearchCV(clf, space, cv=cv, scoring=scoring, n_jobs=n_jobs)
    result_gs = gs.fit(X, y)

    print('Best Score: %s' % result_gs.best_score_)
    print('Best Hyperparameters: %s' % result_gs.best_params_)