# Kiva_NLP

## Conclustions and Recommendations



## Movitation

**About Kiva**
Kiva is an international nonprofit founded in 2005 with a mission to connect people through lending to alleviate poverty. In June 2018 Kiva was in 85 countries, and had served 2.9 Million borrowers through $ 1.16 Billion worth of loans.

We want to understand if the description can be segmented into meaningful clusters. Meaningful clusters can be potentially be used to analyze interactions with other features of the borrower profiles. Clusters can also be used to identify the features of lenders who provide funding to this cluster borrowers, which can expand Kiva's tools to analyse the best matches between borrowers and lenders.

## Data & Methodology

This analysis uses Kiva's Data Snapshot (https://build.kiva.org/docs/data/snapshots) downloaded on June 15th, 2018.
We focused on column Desprcition and Description Translated to get an overview of the profiles of Kiva loan borrowers.

We choose to use NMF model for its advantage at reducing dimensionality. It also discovers latent features which can be interpreted as topics for large set of text.

### Technology Used

- Python 
- Sklearn
- NLTK
- Pandas
- Numpy
- Beautiful Soup

## Next Steps

- exclude Spanish descriptions 
- strip out Kiva translation template copy
