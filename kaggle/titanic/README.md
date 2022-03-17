# Project Checklist

1. Frame the problem and look at the big picture
2. Get the data
3. Explore the data

## 1. Frame the problem and look at the big picture

### 1.1 Define the objective in business terms
Based on the conditions of the passengers (class of ticket, sex, age, among others), predict which of them would be more likely to survive the Titanic accident.

### 1.2 Define the objective in business terms
It's just to familiarize myself with how competitions on the Kaggle platform works.

### 1.3 What are the current solutions/workarounds (if any)?
It does not apply in this context.

### 1.4 How should you frame this problem?
- [x] Supervised learning
- [ ] Unsupervised learning
- [ ] Reinforcement learning
- [ ] Online
- [x] Offline

### 1.5 How should performance be measured?
The dataset is very simple and small. Do not demand high perfomance from possibles solutions.

### 1.6 Is the performance measure aligned with the business objective?
- [x] Yes
- [ ] No

### 1.7 What would be the minimum performance needed to reach the business objective?
Not a lot.

### 1.8 What are comparable problems? Can you reuse experience or tools?
Other models already submitted on the Kaggle platform.

### 1.9 Is human expertise available?
- [ ] Yes
- [x] No

### 1.10. How would you solve the problem manually?
Looking at resources like https://www.encyclopedia-titanica.org/titanic-survivors.

### 1.11 List the assumptions you or others have made so far
- Women and children were more chance to suviver.
- First-class members had advantage of getting into the lifeboat.
- On the night of sinking, the temperature was around 4.1°C and ocean approximately 4°C.
- Third-class passengers did not have easy access to the upper deck.
- The number of third-class members who dit not survive was the highest of first and second classes.
- About 80% of the crew member did not survive.
- Lifeboat with no maximum number of passengers.

### 1.12 Verify assumptions if possible


## 2. Get the data

### 2.1 List the data you need and how much you need
- List of passengers and crew members.
- Passengers Ticket Class.
- Sex of Passengers.
- Age of Passengers.
- Passengers Relationship aboard(e.g. husband, wife, children, siblings, and so on).
- Survived or not.


### 2.2 Find and document where you can get that data
All the information about the Titanic Disaster that we need, in this context, can be found here https://www.kaggle.com/c/titanic

### 2.3 Check how much space it will take
About 5MB

### 2.4 Check legal obligations, and get the authorization if necessary
Just accept rules for [Kaggle Titantic competition](https://www.kaggle.com/c/titanic/rules)

### 2.5 Get access authorizations
It just create a user in [kaggle platform](https://www.kaggle.com).

### 2.6 Create a workspace (with enough storage space)
- [x] Yes
- [ ] No

### 2.7 Get the data
- [x] Yes
- [ ] No

### 2.8 Convert the data to a format you can easily manipulate (without changing the data itself)
- [x] Data properly formatted
- [x] Data were splitted in train, validation and test
- [ ] Data need a lot of tweaking


### 2.9 Ensure sensitive information is deleted or protected (e.g., anonymized)
- [x] Yes
- [ ] No

### 2.10 Check the size and type of data (time series, sample, geographical, etc.)
- [x] Yes
- [ ] No

### 2.11 Sample a test set, put it aside, and never look at it (no data snooping!)
- [x] Yes
- [ ] No


### 3. Explore the data
<!--- <details>
<summary>Check</summary> and here
-->

### 3.1 Create a copy of the data for exploration (sampling it down to a manageable size if necessary).
- [x] Yes
- [ ] No

### 3.2 Create a Jupyter notebook to keep record of your data exploration.
- [x] Yes
- [ ] No

### 3.3 Study each attribute and its characteristics:
- [x] Names
- [x] Type (categorical, int/float, bounded/unbounded, text, structured, etc.)
- [x] % of missing values
- [x] Noisiness and type of noise (stochastic, outliers, rounding errors, etc.)
- [ ] Possibly useful for the task?
- [ ] Type of distribution (Gaussian, uniform, logarithmic, etc.)

### 3.4 For supervised learning tasks, identify the target attribute(s).
The target is "Survived" feature

### 3.5 Visualize the data.
### 3.6 Study the correlations between attributes.
### 3.7 Study how you would solve the problem manually.
### 3.8 Identify the promising transformations you may want to apply.
### 3.9 Identify extra data that would be useful (go back to "Get the Data" on page 502).
### 3.10 Document what you have learned.


<!--- </details> -->

