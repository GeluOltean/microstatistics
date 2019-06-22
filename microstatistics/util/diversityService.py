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
        """
        Computes an index based on provided strategy.

        :param data: DataFrame containing a sample dataset
        :param strategy: index selection based on provided strategy
        :param size: correction size for the indices that require such a thing
        :return: a reduced DataFrame object with one column
        """
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
        """
        Computes the benthic foraminifera oxygenation index according to K. Kaiho.

        :param data: DataFrame containing individuals separated into oxic, suboxic and disoxic categories
        :return: a reduced DataFrame object with one column where each entry represents the oxygenation index
        """
        return data.apply(df_bfoi)

    @staticmethod
    def compute_percentages(data: DataFrame) -> DataFrame:
        """
        Compute the percentage each entry represents in a sample.

        :param data: DataFrame containing a sample dataset
        :return: a reduced DataFrame object with one column where each entry represents the species percentage for a
        sample
        """
        return data.apply(df_proportion).apply(lambda x: x * 100)

    @staticmethod
    def compute_morphogroups(data: DataFrame) -> DataFrame:
        """
        Applies the @compute_percentages function to a DataFrame and transposes the results. Descriptive function to
        avoid magic .transpose() parameters in the program

        :param data: DataFrame containing a sample dataset
        :return: a reduced DataFrame object with one column where each entry represents the species percentage for a
        sample
        """
        return DiversityService.compute_percentages(data).transpose()

    @staticmethod
    def compute_linkage(data: DataFrame) -> numpy.ndarray:
        """
        Computes the Bray-Curtis distance matrix, and subsequently the average linkage between samples.

        :param data: DataFrame containing a sample dataset
        :return: Computed linkage array.
        """
        item_distance = distance.pdist(data.values, metric="braycurtis")
        return hierarchy.linkage(item_distance, method="average")

    # TODO: Add dto instead of dict
    @staticmethod
    def compute_nmds(data: DataFrame, dimensions: int, runs: int) -> Dict:
        """
        Computes non-Metric Multidimensional Scaling on a given dataset.

        :param data: DataFrame containing a sample dataset
        :param dimensions: number of dimensions to reduce to when executing nmds
        :param runs: number of runs to use when computing nmds
        :return: a dict containing the coordinates and stress values to be used for graphing
        """
        item_distance = distance.pdist(data.T.values, metric="braycurtis")
        square_dist = distance.squareform(item_distance)
        nmds = MDS(n_components=dimensions, metric=False, dissimilarity="precomputed", max_iter=runs, n_init=30)

        rez = nmds.fit(square_dist)
        pos = rez.embedding_
        stress = rez.stress_
        pos0 = pos[:, 0].tolist()
        pos1 = pos[:, 1].tolist()

        return {"pos0": pos0, "pos1": pos1, "stress": stress}
