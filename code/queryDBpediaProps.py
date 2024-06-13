#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Query DBpedia for a given entity
# From ChatGPT. Prompt: "Thanks! Now please write a sparql query that can be used in Python to get all the properties related to Olga Bondareva on DBpedia. For example, birthDate, birthPlace, etc."
from SPARQLWrapper import SPARQLWrapper, JSON
import os
import re
import codecs
import sys
import pickle

# print('There are '+str(len(list_properties))+' different property labels.')
# print(sorted(list_properties))

class Triple:
  def __init__(self, prop, subj_value, obj_value):
    self.DBprop = prop
    self.DBsubj = subj_value
    self.DBobj = obj_value

def get_triples_seen(results, subj_name, triple_source, list_properties, ignore_properties_list):
  # Process and print the results
  list_triple_objects = []
  for result in results:
    # property_uri is something like this: http://dbpedia.org/property/deathPlace
    property_uri = result["property"]["value"]
    # value is a string (1937-04-27) or an entity uri (http://dbpedia.org/resource/Saint_Petersburg)
    value = result["value"]["value"]
    # Get the strings for property and object
    if len(value) > 0:
      url_triples = ''
      if triple_source == 'Ontology':
        url_triples = 'http://dbpedia.org/ontology/'
      elif triple_source == 'Infobox':
        url_triples = 'http://dbpedia.org/property/'
      if re.search(url_triples, property_uri):
        prop_name = property_uri.rsplit('/', 1)[1]
        obj_name = value
        if re.search('http://', value):
          obj_name = value.rsplit('/', 1)[1]
        if prop_name in list_properties and not prop_name in ignore_properties_list:
          # print(f"{prop_name}: {obj_name}")
          triple_object = Triple(prop_name, subj_name, obj_name)
          list_triple_objects.append(triple_object)
  return(list_triple_objects)

def get_properties_of_entity(uri):
  # Define the DBpedia SPARQL endpoint URL
  sparql_endpoint = "https://dbpedia.org/sparql"
  # Compose the SPARQL query
  sparql_query = f"""
  SELECT ?property ?value
  WHERE {{
    <{uri}> ?property ?value.
  }}
  """
  # Create a SPARQLWrapper object and set the query
  sparql = SPARQLWrapper(sparql_endpoint)
  sparql.setQuery(sparql_query)
  # Set the return format to JSON
  sparql.setReturnFormat(JSON)
  # Execute the query and parse the results
  results = sparql.query().convert()

  # Activate block to show all properties
  # for result in results["results"]["bindings"]:
  #   # property_uri is something like this: http://dbpedia.org/property/deathPlace
  #   property_uri = result["property"]["value"]
  #   # value is a string (1937-04-27) or an entity uri (http://dbpedia.org/resource/Saint_Petersburg)
  #   value = result["value"]["value"]
  #   print(f"{property_uri}: {value}")

  # Return the list of properties for the entity
  return(results["results"]["bindings"])

  # if __name__ == "__main__":
  #   props_list_path = sys.argv[1]
  #   entity_name = sys.argv[2]
  #   triple_source = sys.argv[3]
  #   ignore_properties_str = sys.argv[4]
  #   out_folder = sys.argv[5]

def get_dbpedia_properties(props_list_path, entity_name, triple_source, ignore_properties_str):
  ignore_properties_input = ignore_properties_str.split(',')
  ignore_properties_list = []
  for ignored_property in ignore_properties_input:
    ignore_properties_list.append(ignored_property.strip())

  # Read file with all covered properties
  fd = codecs.open(props_list_path, 'r', 'utf-8')
  lines_properties = fd.readlines()
  list_properties = []
  for line_properties in lines_properties:
    line_prop_list = line_properties.strip().split('-')
    for prop in line_prop_list:
      list_properties.append(prop)

  selected_uri = "http://dbpedia.org/resource/"+entity_name
  # selected_uri = "http://dbpedia.org/resource/Olga_Bondareva"
  subj_name = selected_uri.rsplit('/', 1)[1]
  # Get all properties for entity
  results = get_properties_of_entity(selected_uri)
  # Get properties covered by the generator and their respective objets
  list_triple_objects = get_triples_seen(results, subj_name, triple_source, list_properties, ignore_properties_list)

  # Check
  # print('Subject: '+subj_name)
  # for triple_object in list_triple_objects:
  #   print(triple_object.DBprop+' : '+triple_object.DBobj)

  list_prop = []
  list_obj = []
  list_propObj =[]

  for n, triple_object in enumerate(list_triple_objects):
    list_prop.append(triple_object.DBprop)
    list_obj.append(triple_object.DBobj)
    list_propObj.append(str(n)+' - '+triple_object.DBprop+': '+triple_object.DBobj)

  # print(list_propObj)
  return list_triple_objects, list_propObj, list_obj

  # with open(os.path.join(out_folder, 'list_PropObj'), 'wb') as fh:
  #   pickle.dump(list_propObj, fh)
    
  # with open(os.path.join(out_folder, 'list_triple_objects'), 'wb') as fh:
  #   pickle.dump(list_triple_objects, fh)
    
  # with open(os.path.join(out_folder, 'list_obj'), 'wb') as fh:
  #   pickle.dump(list_obj, fh)
