from logging import getLogger, config

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

import lightgbm as lgb

import pickle

# 4. Create Model

logger = getLogger('__main__.modeling')

class Modeling:
    def __init__(self):
        self.logger = getLogger('__main__.modeling.Modeling')

    def create_model(self, val_hotel_reviews) -> pd.DataFrame:
       
        X = val_hotel_reviews.drop('Reviewer_Score', axis=1)
        y = val_hotel_reviews['Reviewer_Score']

        X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.3, random_state=42)
        
        train_data = lgb.Dataset(X_train, label=y_train)
        valid_data = lgb.Dataset(X_valid, label=y_valid, reference=train_data)

        params = {
            'objective': 'regression',  # 回帰タスク
            'metric': 'rmse',  # 評価指標はRMSE（平均二乗誤差の平方根）
            'boosting_type': 'gbdt',  # 勾配ブースティング木
            'learning_rate': 0.1,  # 学習率
            'num_leaves': 31,  # 決定木の複雑さを制御
            'verbose': -1,  # 詳細な出力を抑制
            'random_state':42 # 乱数の固定
        }

        model = lgb.train(
            params,
            train_data,
            valid_sets=[valid_data],
        )
        
        y_pred = model.predict(X_valid, num_iteration=model.best_iteration)

        rmse = mean_squared_error(y_valid, y_pred)
        
        self.logger.info("<<Evaluate RMSE>>")
        self.logger.info(f"RMSE: {rmse:.4f}")
        
        self.logger.info("Complete 3. Data Preprocessing")

        return model

