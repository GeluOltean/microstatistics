import numpy
from pandas import DataFrame, Series
from scipy.cluster import hierarchy
from scipy.spatial import distance
from sklearn.manifold import MDS
from typing import Dict

from microstatistics.util.diversities import df_shannon, df_fisher, df_simpson, df_equitability, df_hurlbert, \
    df_proportion, df_bfoi, FISHER, SIMPSON, SHANNON, EQUITABILITY, HURLBERT, BFOI


class DiversityService(object):
    diversities = {
        FISHER: df_fisher,
        SIMPSON: df_simpson,
        SHANNON: df_shannon,
        EQUITABILITY: df_equitability,
        HURLBERT: df_hurlbert,
        BFOI: df_bfoi
    }

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def compute_index(data: DataFrame, strategy: str, size: int = 100) -> DataFrame:
        if strategy == FISHER:
            return data.apply(DiversityService.diversities[FISHER])

        elif strategy == SIMPSON:
            return data.apply(DiversityService.diversities[SIMPSON])

        elif strategy == SHANNON:
            return data.apply(DiversityService.diversities[SHANNON])

        elif strategy == EQUITABILITY:
            return data.apply(DiversityService.diversities[EQUITABILITY])

        elif strategy == HURLBERT:
            return data.apply(lambda x: DiversityService.diversities[HURLBERT](x, size))

        elif strategy == BFOI:
            return data.apply(DiversityService.diversities[BFOI])

        else:
            raise ValueError(f"Strategy not found. Please select one from the {DiversityService.__class__.__name__} "
                             f"constants.")

    @staticmethod
    def compute_bfoi(data: DataFrame) -> DataFrame:
        return data.apply(df_bfoi)

    @staticmethod
    def compute_percentages(data: DataFrame) -> DataFrame:
        return data.apply(df_proportion).apply(lambda x: x * 100)

    @staticmethod
    def compute_percentages_series(series: Series) -> DataFrame:
        return df_proportion(series).apply(lambda x: x * 100)

    @staticmethod
    def compute_morphogroups(data: DataFrame) -> DataFrame:
        return DiversityService.compute_percentages(data).transpose()

    @staticmethod
    def compute_linkage(data: DataFrame) -> numpy.ndarray:
        item_distance = distance.pdist(data.values, metric="braycurtis")
        return hierarchy.linkage(item_distance, method="average")

    @staticmethod
    def compute_nmds(data: DataFrame, dimensions: int, runs: int) -> Dict:
        item_distance = distance.pdist(data.T.values, metric="braycurtis")
        square_dist = distance.squareform(item_distance)
        nmds = MDS(n_components=dimensions, metric=False, dissimilarity="precomputed", max_iter=runs, n_init=30)

        rez = nmds.fit(square_dist)
        pos = rez.embedding_
        stress = rez.stress_
        pos0 = pos[:, 0].tolist()
        pos1 = pos[:, 1].tolist()

        return {"pos0": pos0, "pos1": pos1, "stress": stress}
