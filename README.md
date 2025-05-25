# New Delhi Reviews - Clustering and Analysis

This project aims to preprocess textual reviews, cluster them into meaningful groups, and extract top keywords for each cluster to provide insights. The workflow includes data preprocessing, feature engineering, clustering, and keyword extraction.

# Project Workflow Details

### 1. Data Collection

Reviews were collected from a dataset consisting of user-generated content.

### 2. Text Preprocessing
The reviews were preprocessed using the following steps:

#### Lowercasing:

Converted all text to lowercase to ensure uniformity.

#### Tokenization:

Split text into individual words using NLTK (Natural Language Toolkit).

#### Lemmatization :

Reduced words to their base or root form using NLTK's WordNetLemmatizer to normalize the text

### 3. Clustering
   
#### K-Means Clustering:

Used the K-Means algorithm to cluster the reviews into distinct groups based on their Truncated SVD embeddings.

The number of clusters was determined based on domain knowledge or the elbow method.

### 4. Keyword Extraction

Used NLTK to extract meaningful keywords for each cluster.

Extracted the top 7 keywords for each cluster to summarize its central theme.

# Future Enhancements

1.Improve clustering by experimenting with advanced models like DBSCAN or hierarchical clustering.

2.Integrate a database to handle larger datasets dynamically.

# Steamlit App Run
