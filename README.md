# WikipediaPage_Generator
**Important notice**: this tool is still at an early stage of development; it can generate text that is unnatural, and sometimes ungrammatical. 

The tool is intended to generate seed Wikipedia pages in several languages for people to edit and possibly upload on Wikipedia.

## Quick start

1. Click on *Wikipedia_generator.ipynb* above and then click on *Open in Colab* at the top of the next page.
2. In Colab, run cell of Step 1 to download the resources needed (click the play button just below *Step 1*); it takes a couple of minutes to install.
3. Run first cell of Step 2 to set parameters (click the play button just below *Set parameters*; see below for more about parameters).
4. Run second cell of Step 2 to fetch DBpedia properties (click the play button just below *Get DBpedia properties*)
5. Optional: select one or more properties in the resulting table using Ctrl+click on each desired property (if none specified, all will be generated).
6. Run 19 cells of Step 3 to generate a text (click the play button just below *Step 3*).
7. Run the cell of Step 4 to show the text in a mock Wikipedia page (click the play button just below *Step 4*).

## Parameters

**Basic parameters**

*name*: the name of the entity you want to generate a text about, e.g. "Titanic" or "Barack Obama".

*category*: the category the entity belongs to; it is usually not needed but can help the generation process.

*language*: choose the output language; currently supported: English (EN) and Irish (GA).

*triple_source*: choose where to get the triples from, either the DBpedia Ontology (Ontology, generally more quality) or the Wikipedia infoboxes ('Infobox', generally more coverage). 

*ignore_properties*: list here the properties (separated by a comma) that you don't want to generate (e.g. "width" often has bad values on DBpedia, so it's recommended to ignore it).

**Advanced parameters**

*generate_intermediate_representations*: Select 'no' to get all intermediate linguistic representations, 'yes' if you're only interested in the output.

*split*: set to 'test' for Wikipedia page generation.
