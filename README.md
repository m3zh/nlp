							Welcome aboard Captain

Overview:
https://doi.org/10.1186/s41182-019-0165-6

Meta-Analysis : background and python pipeline
https://towardsdatascience.com/meta-analysis-background-and-python-pipeline-bccaf4fde362

Package for stats analysis:
https://pypi.org/project/PythonMeta/

Package for Google Scholar searching:
https://pypi.org/project/scholarly/

Searching for PubMed:
https://marcobonzanini.com/2015/01/12/searching-pubmed-with-python/

Crossref API doc:
https://github.com/CrossRef/rest-api-doc#field-queries

More API to retrieve metadata from scientific articles :
(may be more relevant to use somthg like CrossRef than specific API for each database ?)
https://www.pauloldham.net/api-resources-for-scientific-literature/

Comparative of database engine
https://harzing.com/resources/publish-or-perish/manual/using/use-cases/general-search


/******** TECH SPECIFICATIONS *********\

1. Searching databases
	1. Query with keywords in
		- Crossref,
		- Google Scholar (operators using is possible ?)
		- PubMed (operators using is possible ?)
	2. Append each databases results into a dataframe with those informations :
		Title of publication
		Domain of contribution
		Authors name
		Date of publication
		Abstract
		DOI
		Availability of full text (pretty optionnal)
	3. Remove duplicates
	4. Merge dataframes

2. Abstract feeding

3. Title and abstract sreening
