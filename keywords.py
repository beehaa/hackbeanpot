"""
Plot graph of keywords

From Indico:
This function will return a dictionary with top_n key-value pairs.
These key-value pairs represent the likelihood that each of the
extracted keywords are relevant to the analyzed text.
The keys in the dictionary are strings containing the extracted keywords,
and the values are the likelihoods that these keywords are relevant to the analyzed text.

Using batched output, plot relevance graphs using pyplot.
input file -> text transcript

"""

import plotly.plotly as py
import plotly.graph_objs as go 
#version 2.3

import indicoio
indicoio.config.api_key = "6e20bd4ee1b0be47f25d0f227578fd14"


#identify the important words within a document

# single example
indicoio.keywords("Some call it the sunshine state", version=2)

# batch example
x = indicoio.keywords([
    "Some call it the sunshine state",
    "Some call it the sunshine state"
], version=2)

for i in x:
    for u in i:
        print(u)
