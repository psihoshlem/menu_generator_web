import os
from sklearn.neural_network import MLPRegressor
import numpy as np
from joblib import load, dump

def is_dump_exist(login: str) -> bool:
    return f'{login}.joblib' in os.listdir('./users_dumps')

def add_data_to_dump(login: str, train_X: list[int | float], train_y: int):
    train_X = [train_X]
    train_y = [train_y]
    if is_dump_exist(login):
        model = load(f'./users_dumps/{login}.joblib')
    else:
        model = MLPRegressor(hidden_layer_sizes=(100, ), max_iter=1000, random_state=1)
    model.fit(train_X, train_y)
    dump(model, f'./users_dumps/{login}.joblib')

def get_predict(login:str, X: list[int | float]) -> float:
    if is_dump_exist(login):
        model = load(f'./users_dumps/{login}.joblib')
    else:
        return 0
    predict = model.predict(np.array([X]))
    return max(min(predict[0], 5), 1)