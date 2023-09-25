# WikipediaPage_Generator
A tool to generate seed Wikipedia pages in several languages for people to edit and upload.

## Quick start

1. Run cell of Step 1 to download the resources needed.
2. Run first cell of Step 2 to set parameters (see below for more about parameters).
3. Run second cell of Step 2 to fetch DBpedia properties
4. Optional: select one or more properties in the resulting table using Ctrl+click on each desired property (if none specified, all will be generated).
6. Run 19 cells of Step 3 to generate a text.
7. Run the cell of Step 4 to show the text in a mock Wikipedia page.

## Parameters

**Basic parameters**

*name*: the name of the entity you want to generate a text about, e.g. "Titanic" or "Barack Obama".

*category*: the category the entity belongs to; it is usually not needed but can help the generation process.

*language*: choose the output language; currently supported: English (EN) and Irish (GA).

*ignore_properties*: list here the properties (separated by a comma) that you don't want to generate (e.g. "width" often has bad values on DBpedia, so it's recommended to ignore it).

**Advanced parameters**

*generate_intermediate_representations*: Select 'no' to get all intermediate linguistic representations, 'yes' if you're only interested in the output.

*split*: set to 'test' for Wikipedia page generation.
