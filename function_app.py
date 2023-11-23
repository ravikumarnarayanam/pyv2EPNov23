import azure.functions as func
import logging

import numpy as np
import json
import tiktoken
import openai
import requests
import os
import io
import urllib3
import fitz
from io import BytesIO
from docx import Document
from pptx import Presentation
import pandas as pd

from striprtf.striprtf import rtf_to_text
import re
import nltk
import ipaddress
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import TfidfVectorizer
from fuzzywuzzy import fuzz
from typing import Dict, List

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="httptrigger")
def httptrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )