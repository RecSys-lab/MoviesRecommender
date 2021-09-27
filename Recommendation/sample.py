import cornac
from cornac.eval_methods import RatioSplit
from cornac.models import MF, PMF, BPR
from cornac.metrics import MAE, RMSE, Precision, Recall, NDCG, AUC, MAP


def sampleCornac():
    # load the built-in MovieLens 100K and split the data based on ratio
    ml_100k = cornac.datasets.movielens.load_feedback()
    rs = RatioSplit(data=ml_100k, test_size=0.2,
                    rating_threshold=4.0, seed=123)

    # initialize models, here we are comparing: Biased MF, PMF, and BPR
    models = [
        MF(k=10, max_iter=25, learning_rate=0.01,
           lambda_reg=0.02, use_bias=True, seed=123),
        PMF(k=10, max_iter=100, learning_rate=0.001, lambda_reg=0.001, seed=123),
        BPR(k=10, max_iter=200, learning_rate=0.001, lambda_reg=0.01, seed=123),
    ]

    # define metrics to evaluate the models
    metrics = [MAE(), RMSE(), Precision(k=10),
               Recall(k=10), NDCG(k=10), AUC(), MAP()]

    # put it together in an experiment, voilà!
    cornac.Experiment(eval_method=rs, models=models,
                      metrics=metrics, user_based=True).run()
