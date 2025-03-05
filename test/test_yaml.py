import pytest
import yaml

def test_yaml_file():
    file = "/Users/alexey/Documents/education/hugging-face-agents-course/resources/prompts.yaml"
    data = yaml.safe_load(open(file, "r"))
    
    print(data.keys())
