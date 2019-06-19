from pandas import DataFrame, Series
from scipy.cluster import hierarchy
from scipy.spatial import distance
from sklearn.manifold import MDS

from microstatistics.util.diversities import df_shannon, df_fisher, df_simpson, df_equitability, df_hurlbert, \
    df_proportion, df_bfoi


class DiversityService(object):
    FISHER = "Fisher diversity"
    SIMPSON = "Simpson diversity"
    SHANNON = "Shannon diversity"
    EQUITABILITY = "Equitability"
    HURLBERT = "Hurlbert diversity"

    diversities = {
        FISHER: df_fisher,
        SIMPSON: df_simpson,
        SHANNON: df_shannon,
        EQUITABILITY: df_equitability,
        HURLBERT: df_hurlbert
    }

    def __init__(self) -> None:
        super().__init__()

    def compute_index(self, data: DataFrame, strategy: str, size: int = 100) -> DataFrame:
        if strategy == self.FISHER:
            return data.apply(self.diversities[self.FISHER])

        elif strategy == self.SIMPSON:
            return data.apply(self.diversities[self.SIMPSON])

        elif strategy == self.SHANNON:
            return data.apply(self.diversities[self.SHANNON])

        elif strategy == self.EQUITABILITY:
            return data.apply(self.diversities[self.EQUITABILITY])

        elif strategy == self.HURLBERT:
            return data.apply(lambda x: self.diversities[self.HURLBERT](x, size))

        else:
            raise ValueError(f"Strategy not found. Please select one from the {self.__class__.__name__} constants.")

    def compute_bfoi(self, data: DataFrame):
        return data.apply(df_bfoi)

    def compute_percentages(self, data: DataFrame):
        return data.apply(df_proportion).apply(lambda x: x * 100)

    def compute_percentages_series(self, series: Series):
        return df_proportion(series).apply(lambda x: x * 100)

    def compute_morphogroups(self, data: DataFrame):
        return self.compute_percentages(data).transpose()

    def compute_linkage(self, data: DataFrame):
        item_distance = distance.pdist(data, metric="braycurtis")
        return hierarchy.linkage(item_distance, method="average")

    def compute_nmds(self, data: DataFrame, dimensions: int, runs: int):
        item_distance = distance.pdist(data.T, metric="braycurtis")
        square_dist = distance.squareform(item_distance)
        nmds = MDS(n_components=dimensions, metric=False, dissimilarity="precomputed", max_iter=runs, n_init=30)

        pos = nmds.fit(square_dist).embedding_
        stress = nmds.fit(square_dist).stress_
        pos0 = pos[:, 0].tolist()
        pos1 = pos[:, 1].tolist()

        return {"pos0": pos0, "pos1": pos1, "stress": stress}
