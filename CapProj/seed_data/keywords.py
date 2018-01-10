import django
import os
import sys


PATH=os.path.abspath(os.path.dirname(__file__))

if os.name == 'posix': # Unix based systems
    bin_name = 'bin'
else:                  # Windows
    bin_name = 'Scripts'

# Relative path to the virtual environment
# (relative to the stand-alone script)
rel_path = '../venv/%s/activate_this.py' % bin_name
activate_this = os.path.join(PATH, rel_path)

sys.path.append("../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CapProj.settings")

django.setup()
from django.core.exceptions import ValidationError
from CapApp.models import Keyword, Grant


keywords =["autism", "primate", "big data", "cancer",  "biotechnology", "convergance", "cure", "evolution", "data mining", "immunotherapy", "machine learning", "learning", "memory", "nanotechnology", "novel", "scalability", "synergey", "therapy", "cancer", "AIDS", "HIV", "cardiac", "stroke", "gender" "acute", "adaptive immune response", "adaptive immunity", "adult", "youth", "disability", "flu", "deppression", "vaccine", "dementia", "malignant", "transplant"]

# "age", "age related", "aging", "antibody response", "biochemical", "biogenesis", "blood platelets", "cells", "cessation of life", "cytokine", "Cytometry", "Dendritic Cells", "disability", "flu"]

# keywords2 =
#  "elderly", "gene expression", "genetic", "health", "human", "immune",  "immune function", Immune response; Immune system; Immunologics; Immunology; immunosenescence; Impairment; improved; Individual; Infection; Influenza; Influenza A Virus, H1N1 Subtype; Influenza prevention; Influenza vaccination; Influenza virus vaccine; influenzavirus; insight; Institutes; Integration Host Factors; Lipids; Liquid Chromatography; Mass Spectrum Analysis; meetings; Metabolic; Metabolic Pathway; Metabolism; metabolomics; Methods; Mitochondria; Molecular; Molecular Profiling; monocyte; mortality; Natural Immunity; Natural Killer Cells; neutrophil; novel; Nursing Homes; Operative Surgical Procedures; Outcome; oxidation; pandemic disease; Pathway interactions; Pattern recognition receptor;
 # Pharmaceutical Preparations; Physiological; Population; Production; programs; Proteins; Public Health; receptor; receptor function; Recruitment Activity; Registries; Research; Research Infrastructure; residence; Resistance; Resources; response; Sampling; Seasons; Serum; Signal Transduction; Stress; Syndrome; targeted treatment; Toll-like receptors; transcriptome sequencing; transcriptomics; Translating; United States; Vaccination; vaccine response; Vaccines; Viral Hemagglutinins; Whole Blood; Work; young adult;

for word in keywords:
    try:
        present = Keyword.objects.get(keyword=word)
    except:
        present = None

    if present:
        print(f'this is a repeat: {present}')
    new_word = Keyword()
    new_word.keyword = word
    new_word.searches = 0

    try:
        Keyword.full_clean(new_word)
    except ValidationError as e:
        print(e)

    print(new_word.keyword)

    try:
        new_word.save()
    except:
        print(f"there was a problem saving with Keyword {word}")

    present = Keyword.objects.get(keyword=word)

    grant_list =Grant.objects.filter(project_terms__search=word)
    for grant in grant_list:
        present.grants.add(grant)
