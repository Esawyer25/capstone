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


keywords =["autism", "primate"]

for word in keywords:
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

    grant_list =Grant.objects.filter(project_terms__search=word)
    for grant in grant_list:
        new_word.grants.add(grant)
