import os
from typing import List

import numpy
from math import ceil
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import AutoMinorLocator
from scipy.cluster import hierarchy as hc
from pandas import DataFrame, Series

plt.style.use("seaborn-whitegrid")
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
plt.rcParams['svg.fonttype'] = 'none'


class GraphingService(object):
    def __init__(self):
        super().__init__()

    @staticmethod
    def graph_index(save_path: str, title: str, labels: List[str], data: DataFrame):
        """For use to plot graphs of diversity indices, as well as percentage graphs."""
        plt.figure(dpi=200, figsize=(3, 12))
        y_axis = [x + 1 for x in range(data.count())]
        plt.plot(data, y_axis)
        plt.title(title)
        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.gca().set_ylim(1, len(y_axis))
        plt.gca().set_xlim(0, max(data) * 1.5)
        plt.yticks(y_axis, labels)
        plt.ylabel("Sample number")
        plt.fill_betweenx(y_axis, data)

        save_name = f"/{title}.svg"
        plt.savefig(save_path + save_name)
        plt.close()

    @staticmethod
    def graph_morphogroups(save_path: str, labels: List[str], data: DataFrame):
        morphogroups = ('M1', 'M2a', 'M2b', 'M2c', 'M3a', 'M3b', 'M3c', 'M4a',
                        'M4b')

        global_max = max(data.max().values)
        y_axis = [x + 1 for x in range(data[0].count())]

        if not os.path.isdir(save_path + "/morphogroups"):
            os.mkdir(save_path + "/morphogroups")
        save_location_morphs = save_path + "/morphogroups"

        morphogroup_dict = {}
        for i in range(len(morphogroups)):
            morphogroup_dict[morphogroups[i]] = data.T.values[i]

        # ensure the same scale
        for k in morphogroup_dict:
            local_size = 5 if max(morphogroup_dict[k]) < 5 else max(morphogroup_dict[k])
            local_max = ((local_size * 100) / global_max) / 100

            plt.figure(dpi=300, figsize=[local_max * 3, 12])
            plt.plot(morphogroup_dict[k], y_axis)
            plt.title(k)
            plt.gca().set_xlim(0)
            if ceil(max(morphogroup_dict[k])) < 5:
                plt.gca().set_xlim(0, 5)
            else:
                plt.gca().set_xlim(0)
            plt.gca().set_ylim(1, len(y_axis))
            plt.gca().xaxis.set_minor_locator(AutoMinorLocator(n=5))
            plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
            plt.yticks(y_axis, labels)
            plt.fill_betweenx(y_axis, morphogroup_dict[k])
            plt.savefig(save_location_morphs + f"/{k}.svg")
            plt.close(k)

    @staticmethod
    def graph_epi_inf_detailed(save_path: str, data: DataFrame):
        """Represents the epifaunal to infaunal proportions by displaying foram
        proportions by their respective environment. Requires a dataframe object
        as input. """
        epifaunal = data.iloc[0]
        inf_shallow = data.iloc[1] + epifaunal
        inf_deep = data.iloc[2] + inf_shallow
        inf_undetermined = data.iloc[3] + inf_deep

        plt.figure(dpi=200, figsize=(3, 12))
        y_axis = [x + 1 for x in range(data.T.count())]
        plt.title("Detailed Epifaunal to Infaunal proportions")
        plt.ylabel("Sample number")
        plt.xlabel("Percentage")

        plt.plot(epifaunal, y_axis, '#52A55C', label='Epifaunal')
        plt.plot(inf_shallow, y_axis, '#236A62', label='Inf. Shallow')
        plt.plot(inf_deep, y_axis, '#2E4372', label='Inf. Deep')
        plt.plot(inf_undetermined, y_axis, '#535353', label='Inf. Undetermined')

        plt.fill_betweenx(y_axis, epifaunal, facecolor='#52A55C')
        plt.fill_betweenx(y_axis, epifaunal, inf_shallow, facecolor='#236A62')
        plt.fill_betweenx(y_axis, inf_shallow, inf_deep, facecolor='#2E4372')
        plt.fill_betweenx(y_axis, inf_deep, inf_undetermined, facecolor='#535353')

        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.yticks(y_axis)
        plt.gca().set_xlim(0, 100)
        plt.gca().set_ylim(1, len(y_axis))

        plt.subplot(111).legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
                                fancybox=True, shadow=True, ncol=5, borderaxespad=2)

        save_name = "/Detailed Epi-Infaunal.svg"
        plt.savefig(save_path + save_name)

    @staticmethod
    def graph_dendrogram(save_path: str, title: str, labels, data: numpy.ndarray):
        """For use in both R and Q mode dendrogram rendering."""
        plt.figure(dpi=500)
        hc.dendrogram(data, labels=labels)
        plt.suptitle(title)

        save_name = f"/{title}.svg"
        plt.savefig(save_path + save_name)

    @staticmethod
    def graph_nmds(save_path: str, labels, data: dict):
        pos0 = data["pos0"]
        pos1 = data["pos1"]
        stress = data["stress"]

        fig, ax = plt.subplots()
        ax.scatter(pos0, pos1)
        for i, x in enumerate(labels):
            ax.annotate(x, (pos0[i], pos1[i]))
        fig.suptitle("nMDS (Bray-Curtis)")
        ax.set_title(f"Stress = {str(stress)}")

        save_name = "/nMDS.svg"
        plt.savefig(save_path + save_name)
