# underfitting and overfitting
'''
Testing different values of max_leaf_nodes for Decision Tree and calculating MAE for each
1. Train DTR with given max_leaf_nodes
2. Making predictions on validation sets
3. Calculates and prints MAE to evaluate performances

low max_leaf_nodes = 5, high MAE, underfitting
high max_leaf_nodes = 5000, overfit 
optimal max_leaf_nodes: minimize MAE without overfitting

need low mae as mae is the average of all your models mistakes
'''

from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

def get_mae(max_leaf_nodes, train_X, train_y, val_X, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes = max_leaf_nodes, random_state = 0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return mae
    
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, train_y, val_X, val_y)
    print(max_leaf_nodes, my_mae)
