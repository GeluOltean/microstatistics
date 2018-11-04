import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import AutoMinorLocator
from .diversities import dfProportion
from scipy.cluster import hierarchy as hc
from scipy.spatial import distance as dist
from sklearn.manifold import MDS

def graphIndex(lst, title: str, saveloc: str):
	"""Represents the list resulted from the calculation of an index. Requires
	an iterable collection and a title as input."""
	holder = lst
	plt.figure(dpi = 200, figsize=(3,12))
	yaxis = [x+1 for x in range(len(holder))]
	plt.plot(holder, yaxis, c="black")
	plt.title(title)
	plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
	plt.gca().set_ylim(1, len(yaxis))
	plt.gca().set_xlim(0)
	plt.yticks(yaxis)
	plt.ylabel("Sample number")
	plt.fill_betweenx(yaxis, holder, facecolor='black')

	savename = f"/{title}.svg"
	plt.savefig(saveloc + savename)

def graphPercentages(frame, index, title: str, saveloc: str):
	"""Represents a row from a dataframe (a chosen species) by their proportion
	in a sample (column). Requires a dataframe object, an index, and a title as
	input. """
	holder = dfProportion(frame) * 100 
	holder = holder.replace(np.nan, 0)
	plt.figure(dpi = 200, figsize=(3,12))
	yaxis = [x+1 for x in range(len(holder.T))]
	plt.title(title)
	plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
	plt.gca().set_ylim(1, len(yaxis))
	plt.gca().set_xlim(0, 100)
	plt.yticks(yaxis)
	plt.plot(holder.iloc[index], yaxis, c="black")
	plt.ylabel("Sample number")
	plt.fill_betweenx(yaxis, holder.iloc[index], facecolor='black')

	# savename = "/" + f"Abundance of species on row {index+2}" + ".svg"
	savename = f"/{title}.svg"
	plt.savefig(saveloc + savename)

def graphMorphogroups(frame, saveloc: str):
	"""Represents the proportion of each morphogroup, displaying foram 
	distribution by morphogroup. Requires a dataframe object as input."""
	holder = dfProportion(frame)

	holder = holder.transpose() * 100

	morphogroups = ['M1', 'M2a', 'M2b', 'M2c', 'M3a', 'M3b', 'M3c', 'M4a', 'M4b']
	plt.figure(dpi = 300, figsize = (50, 16))
	yaxis = [x+1 for x in range(len(holder))]
	plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
	plt.gca().set_ylim(1, len(yaxis))
	plt.subplots_adjust(wspace = 0.8)
	plt.ylabel("Sample number")

	first = plt.subplot(1, 9, 1)
	plt.plot(holder[1], yaxis, c='black')
	plt.xlabel(morphogroups[1])
	plt.yticks(yaxis)
	plt.gca().set_ylim(1, len(yaxis))
	plt.gca().set_xlim(0)
	plt.gca().xaxis.set_minor_locator(AutoMinorLocator(n=5))
	plt.fill_betweenx(yaxis, holder[1], facecolor='black')

	for i in range(2, len(holder.T)):
		plt.subplot(1, 9, i+1, sharex=first)
		plt.plot(holder[i], yaxis, c='black')
		plt.xlabel(morphogroups[i])
		plt.yticks(yaxis) #
		plt.gca().set_ylim(1, len(yaxis))
		plt.gca().set_xlim(0)
		# plt.gca().set_xlim(0, max(holder[i].values)+10)
		# plt.gca().set_xticks([x for x in range(0, max(holder[i].values), 10)])
		plt.gca().xaxis.set_minor_locator(AutoMinorLocator(n=5))
		plt.fill_betweenx(yaxis, holder[i], facecolor='black')

	plt.suptitle("Morphogroup abundances\n")

	savename = "/Morphogroup abundances.svg"
	plt.savefig(saveloc + savename)

def graphEpiInfDetailed(frame, saveloc: str):
	"""Represents the epifaunal to infaunal proportions by displaying foram
	proportions by their respective environment. Requires a dataframe object
	as input. """
	holder = dfProportion(frame) * 100
	# holder.iloc[0] gets the first row
	epifaunal = holder.iloc[0] 
	infShallow = holder.iloc[1] + epifaunal
	infDeep = holder.iloc[2] + infShallow
	infUndetermined = holder.iloc[3] + infDeep

	plt.figure(dpi = 200, figsize = (3,12))
	yaxis = [x+1 for x in range(len(holder.T))]
	plt.title("Detailed Epifaunal to Infaunal proportions")
	plt.ylabel("Sample number")
	plt.xlabel("Percentage")

	plt.plot(epifaunal, yaxis, '#52A55C', label='Epifaunal')
	plt.plot(infShallow, yaxis, '#236A62', label='Inf. Shallow')
	plt.plot(infDeep, yaxis, '#2E4372', label='Inf. Deep')
	plt.plot(infUndetermined, yaxis, '#535353', label='Inf. Undetermined')

	plt.fill_betweenx(yaxis, epifaunal, facecolor='#52A55C')
	plt.fill_betweenx(yaxis, epifaunal, infShallow, facecolor='#236A62')
	plt.fill_betweenx(yaxis, infShallow, infDeep, facecolor='#2E4372')
	plt.fill_betweenx(yaxis, infDeep, infUndetermined, facecolor='#535353')

	plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
	plt.yticks(yaxis)
	plt.gca().set_xlim(0, 100)
	plt.gca().set_ylim(1, len(yaxis))

	plt.subplot(111).legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5, borderaxespad=2)
	
	savename = "/Detailed Epi-Infaunal.svg"
	plt.savefig(saveloc + savename)

##### MULTIVARIATE INDICES #####

def graphSampleDendrogram(frame, saveloc: str):
	labl = list(range(1, len(frame.T)+1))
	sampleDistance = dist.pdist(frame.T, metric="braycurtis")
	plt.figure(dpi=500)
	linkage = hc.linkage(sampleDistance, method="average")
	dendrog = hc.dendrogram(linkage, labels=labl)
	plt.suptitle("R-mode Dendrogram (Bray-Curtis)")

	savename = "/R-mode Dendrogram.svg"
	plt.savefig(saveloc + savename)

def graphSpeciesDendrogram(frame, saveloc: str):
	labl = list(range(1, len(frame)+1))
	speciesDistance = dist.pdist(frame, metric="braycurtis")
	plt.figure(dpi=800)
	linkage = hc.linkage(speciesDistance, method="average")
	dendrog = hc.dendrogram(linkage, orientation="left", labels=labl)
	plt.suptitle("Q-mode Dendrogram (Bray-Curtis)")

	savename = "/Q-mode Dendrogram.svg"
	plt.savefig(saveloc + savename)

def graphNMDS(frame, dim, runs, saveloc: str):
	labl = list(range(1, len(frame.T)+1))
	sampleDistance = dist.pdist(frame.T, metric="braycurtis")
	squareDist = dist.squareform(sampleDistance)

	nmds = MDS(n_components=dim, metric=False, dissimilarity="precomputed", max_iter=runs, n_init=30)
	pos = nmds.fit(squareDist).embedding_
	stress = nmds.fit(squareDist).stress_

	pos0 = pos[:,0].tolist()
	pos1 = pos[:,1].tolist()
	fig, ax = plt.subplots()
	ax.scatter(pos0, pos1)
	for i, x in enumerate(labl):
		ax.annotate(x + 1, (pos0[i], pos1[i]))
	fig.suptitle("nMDS (Bray-Curtis)")
	ax.set_title(f"Stress = {str(stress)}")

	savename = "/nMDS.svg"
	plt.savefig(saveloc + savename)
