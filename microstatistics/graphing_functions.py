import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from diversities import dfProportion

def graphIndex(lst, title: str):
	"""Represents the list resulted from the calculation of an index. Requires
	an iterable collection and a title as input."""
	holder = lst
	# holder = holder.replace(np.nan, 0)
	plt.figure(dpi = 200, figsize=(5,5))
	yaxis = [x+1 for x in range(len(holder))]
	plt.plot(holder, yaxis, c="black")
	plt.title(title)
	plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
	plt.yticks(yaxis)
	plt.ylabel("Sample number")
	plt.show()

def graphPercentages(frame, index, title: str):
	"""Represents a row from a dataframe (a chosen species) by their proportion
	in a sample (column). Requires a dataframe object, an index, and a title as
	input. """
	# catch out of bounds error
	holder = dfProportion(frame) * 100 
	holder = holder.replace(np.nan, 0)
	plt.figure(dpi = 200, figsize=(5,5))
	yaxis = [x+1 for x in range(len(holder.T))]
	plt.title(title)
	plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
	plt.yticks(yaxis)
	plt.plot(holder.iloc[index], yaxis, c="black")
	plt.ylabel("Sample number")
	plt.plot()
	plt.show()

def graphMorphogroups(frame):
	"""Represents the proportion of each morphogroup, displaying foram 
	distribution by morphogroup. Requires a dataframe object as input."""
	holder = dfProportion(frame)
	holder = holder.transpose() * 100
	morphogroups = ['M1', 'M2a', 'M2b', 'M2c', 'M3a', 'M3b', 'M3c', 'M4a', 'M4b']

	plt.figure(dpi = 200, figsize = (5,5))
	yaxis = [x+1 for x in range(len(holder))]
	plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

	for i in range(0, len(holder.T)):
		plt.subplot(1, 9, i+1)
		plt.plot(holder[i], yaxis, c='black')
		plt.xlabel(morphogroups[i])
		plt.yticks(yaxis) #
		plt.gca().set_ylim(1, len(yaxis))
	
	plt.suptitle("Morphogroup abundances\n")
	plt.show()

def graphEpiInfDetailed(frame):
	"""Represents the epifaunal to infaunal proportions by displaying foram
	proportions by their respective environment. Requires a dataframe object
	as input. """
	holder = dfProportion(frame) * 100
	# holder.iloc[0] gets the first row
	epifaunal = holder.iloc[0] 
	infShallow = holder.iloc[1] + epifaunal
	infDeep = holder.iloc[2] + infShallow
	infUndetermined = holder.iloc[3] + infDeep

	plt.figure(dpi = 200, figsize = (5,5))
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
	plt.show()