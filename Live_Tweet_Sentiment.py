{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "80823587",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: tweepy in /opt/anaconda3/lib/python3.8/site-packages (4.9.0)\n",
      "Requirement already satisfied: requests-oauthlib<2,>=1.2.0 in /opt/anaconda3/lib/python3.8/site-packages (from tweepy) (1.3.1)\n",
      "Requirement already satisfied: oauthlib<4,>=3.2.0 in /opt/anaconda3/lib/python3.8/site-packages (from tweepy) (3.2.0)\n",
      "Requirement already satisfied: requests<3,>=2.27.0 in /opt/anaconda3/lib/python3.8/site-packages (from tweepy) (2.27.1)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /opt/anaconda3/lib/python3.8/site-packages (from requests<3,>=2.27.0->tweepy) (2021.10.8)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /opt/anaconda3/lib/python3.8/site-packages (from requests<3,>=2.27.0->tweepy) (2.10)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in /opt/anaconda3/lib/python3.8/site-packages (from requests<3,>=2.27.0->tweepy) (2.0.12)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /opt/anaconda3/lib/python3.8/site-packages (from requests<3,>=2.27.0->tweepy) (1.26.4)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install tweepy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9d0c8f5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: transformers in /opt/anaconda3/lib/python3.8/site-packages (4.18.0)\n",
      "Requirement already satisfied: pyyaml>=5.1 in /opt/anaconda3/lib/python3.8/site-packages (from transformers) (5.4.1)\n",
      "Requirement already satisfied: numpy>=1.17 in /opt/anaconda3/lib/python3.8/site-packages (from transformers) (1.20.1)\n",
      "Requirement already satisfied: filelock in /opt/anaconda3/lib/python3.8/site-packages (from transformers) (3.0.12)\n",
      "Requirement already satisfied: tqdm>=4.27 in /opt/anaconda3/lib/python3.8/site-packages (from transformers) (4.59.0)\n",
      "Requirement already satisfied: packaging>=20.0 in /opt/anaconda3/lib/python3.8/site-packages (from transformers) (20.9)\n",
      "Requirement already satisfied: sacremoses in /opt/anaconda3/lib/python3.8/site-packages (from transformers) (0.0.53)\n",
      "Requirement already satisfied: tokenizers!=0.11.3,<0.13,>=0.11.1 in /opt/anaconda3/lib/python3.8/site-packages (from transformers) (0.12.1)\n",
      "Requirement already satisfied: requests in /opt/anaconda3/lib/python3.8/site-packages (from transformers) (2.27.1)\n",
      "Requirement already satisfied: huggingface-hub<1.0,>=0.1.0 in /opt/anaconda3/lib/python3.8/site-packages (from transformers) (0.5.1)\n",
      "Requirement already satisfied: regex!=2019.12.17 in /opt/anaconda3/lib/python3.8/site-packages (from transformers) (2021.4.4)\n",
      "Requirement already satisfied: typing-extensions>=3.7.4.3 in /opt/anaconda3/lib/python3.8/site-packages (from huggingface-hub<1.0,>=0.1.0->transformers) (3.7.4.3)\n",
      "Requirement already satisfied: pyparsing>=2.0.2 in /opt/anaconda3/lib/python3.8/site-packages (from packaging>=20.0->transformers) (2.4.7)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /opt/anaconda3/lib/python3.8/site-packages (from requests->transformers) (2.10)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in /opt/anaconda3/lib/python3.8/site-packages (from requests->transformers) (2.0.12)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /opt/anaconda3/lib/python3.8/site-packages (from requests->transformers) (1.26.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /opt/anaconda3/lib/python3.8/site-packages (from requests->transformers) (2021.10.8)\n",
      "Requirement already satisfied: joblib in /opt/anaconda3/lib/python3.8/site-packages (from sacremoses->transformers) (1.0.1)\n",
      "Requirement already satisfied: click in /opt/anaconda3/lib/python3.8/site-packages (from sacremoses->transformers) (7.1.2)\n",
      "Requirement already satisfied: six in /opt/anaconda3/lib/python3.8/site-packages (from sacremoses->transformers) (1.15.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install transformers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "05cc4909",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in /opt/anaconda3/lib/python3.8/site-packages (1.4.0)\n",
      "Requirement already satisfied: base58 in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (2.1.1)\n",
      "Requirement already satisfied: pydeck>=0.1.dev5 in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (0.7.1)\n",
      "Requirement already satisfied: pyarrow in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (6.0.1)\n",
      "Requirement already satisfied: pillow>=6.2.0 in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (8.2.0)\n",
      "Requirement already satisfied: pandas>=0.21.0 in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (1.2.4)\n",
      "Requirement already satisfied: toml in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: attrs in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (20.3.0)\n",
      "Requirement already satisfied: python-dateutil in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (2.8.1)\n",
      "Requirement already satisfied: gitpython!=3.1.19 in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (3.1.26)\n",
      "Requirement already satisfied: astor in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (0.8.1)\n",
      "Requirement already satisfied: requests in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (2.27.1)\n",
      "Requirement already satisfied: cachetools>=4.0 in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (5.0.0)\n",
      "Requirement already satisfied: packaging in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (20.9)\n",
      "Requirement already satisfied: click>=7.0 in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (7.1.2)\n",
      "Requirement already satisfied: validators in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (0.18.2)\n",
      "Requirement already satisfied: protobuf!=3.11,>=3.6.0 in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (3.19.3)\n",
      "Requirement already satisfied: tornado>=5.0 in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (6.1)\n",
      "Requirement already satisfied: numpy in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (1.20.1)\n",
      "Requirement already satisfied: pympler>=0.9 in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (1.0.1)\n",
      "Requirement already satisfied: blinker in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (1.4)\n",
      "Requirement already satisfied: tzlocal in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (4.1)\n",
      "Requirement already satisfied: altair>=3.2.0 in /opt/anaconda3/lib/python3.8/site-packages (from streamlit) (4.2.0)\n",
      "Requirement already satisfied: entrypoints in /opt/anaconda3/lib/python3.8/site-packages (from altair>=3.2.0->streamlit) (0.3)\n",
      "Requirement already satisfied: jsonschema>=3.0 in /opt/anaconda3/lib/python3.8/site-packages (from altair>=3.2.0->streamlit) (3.2.0)\n",
      "Requirement already satisfied: toolz in /opt/anaconda3/lib/python3.8/site-packages (from altair>=3.2.0->streamlit) (0.11.1)\n",
      "Requirement already satisfied: jinja2 in /opt/anaconda3/lib/python3.8/site-packages (from altair>=3.2.0->streamlit) (2.11.3)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in /opt/anaconda3/lib/python3.8/site-packages (from gitpython!=3.1.19->streamlit) (4.0.9)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in /opt/anaconda3/lib/python3.8/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit) (5.0.0)\n",
      "Requirement already satisfied: setuptools in /opt/anaconda3/lib/python3.8/site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (52.0.0.post20210125)\n",
      "Requirement already satisfied: six>=1.11.0 in /opt/anaconda3/lib/python3.8/site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (1.15.0)\n",
      "Requirement already satisfied: pyrsistent>=0.14.0 in /opt/anaconda3/lib/python3.8/site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (0.17.3)\n",
      "Requirement already satisfied: pytz>=2017.3 in /opt/anaconda3/lib/python3.8/site-packages (from pandas>=0.21.0->streamlit) (2021.1)\n",
      "Requirement already satisfied: ipywidgets>=7.0.0 in /opt/anaconda3/lib/python3.8/site-packages (from pydeck>=0.1.dev5->streamlit) (7.6.3)\n",
      "Requirement already satisfied: ipykernel>=5.1.2 in /opt/anaconda3/lib/python3.8/site-packages (from pydeck>=0.1.dev5->streamlit) (5.3.4)\n",
      "Requirement already satisfied: traitlets>=4.3.2 in /opt/anaconda3/lib/python3.8/site-packages (from pydeck>=0.1.dev5->streamlit) (5.0.5)\n",
      "Requirement already satisfied: appnope in /opt/anaconda3/lib/python3.8/site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.1.2)\n",
      "Requirement already satisfied: jupyter-client in /opt/anaconda3/lib/python3.8/site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (6.1.12)\n",
      "Requirement already satisfied: ipython>=5.0.0 in /opt/anaconda3/lib/python3.8/site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (7.22.0)\n",
      "Requirement already satisfied: backcall in /opt/anaconda3/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
      "Requirement already satisfied: pickleshare in /opt/anaconda3/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.5)\n",
      "Requirement already satisfied: decorator in /opt/anaconda3/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (5.0.6)\n",
      "Requirement already satisfied: pygments in /opt/anaconda3/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (2.8.1)\n",
      "Requirement already satisfied: pexpect>4.3 in /opt/anaconda3/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.8.0)\n",
      "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /opt/anaconda3/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (3.0.17)\n",
      "Requirement already satisfied: jedi>=0.16 in /opt/anaconda3/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.17.2)\n",
      "Requirement already satisfied: nbformat>=4.2.0 in /opt/anaconda3/lib/python3.8/site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.1.3)\n",
      "Requirement already satisfied: widgetsnbextension~=3.5.0 in /opt/anaconda3/lib/python3.8/site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.5.1)\n",
      "Requirement already satisfied: jupyterlab-widgets>=1.0.0 in /opt/anaconda3/lib/python3.8/site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.0.0)\n",
      "Requirement already satisfied: parso<0.8.0,>=0.7.0 in /opt/anaconda3/lib/python3.8/site-packages (from jedi>=0.16->ipython>=5.0.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.0)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in /opt/anaconda3/lib/python3.8/site-packages (from jinja2->altair>=3.2.0->streamlit) (1.1.1)\n",
      "Requirement already satisfied: ipython-genutils in /opt/anaconda3/lib/python3.8/site-packages (from nbformat>=4.2.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
      "Requirement already satisfied: jupyter-core in /opt/anaconda3/lib/python3.8/site-packages (from nbformat>=4.2.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (4.7.1)\n",
      "Requirement already satisfied: ptyprocess>=0.5 in /opt/anaconda3/lib/python3.8/site-packages (from pexpect>4.3->ipython>=5.0.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.0)\n",
      "Requirement already satisfied: wcwidth in /opt/anaconda3/lib/python3.8/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=5.0.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.5)\n",
      "Requirement already satisfied: notebook>=4.4.1 in /opt/anaconda3/lib/python3.8/site-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (6.3.0)\n",
      "Requirement already satisfied: pyzmq>=17 in /opt/anaconda3/lib/python3.8/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (20.0.0)\n",
      "Requirement already satisfied: nbconvert in /opt/anaconda3/lib/python3.8/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (6.0.7)\n",
      "Requirement already satisfied: terminado>=0.8.3 in /opt/anaconda3/lib/python3.8/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.9.4)\n",
      "Requirement already satisfied: prometheus-client in /opt/anaconda3/lib/python3.8/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.10.1)\n",
      "Requirement already satisfied: argon2-cffi in /opt/anaconda3/lib/python3.8/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (20.1.0)\n",
      "Requirement already satisfied: Send2Trash>=1.5.0 in /opt/anaconda3/lib/python3.8/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.5.0)\n",
      "Requirement already satisfied: cffi>=1.0.0 in /opt/anaconda3/lib/python3.8/site-packages (from argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.14.5)\n",
      "Requirement already satisfied: pycparser in /opt/anaconda3/lib/python3.8/site-packages (from cffi>=1.0.0->argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (2.20)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: mistune<2,>=0.8.1 in /opt/anaconda3/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.8.4)\n",
      "Requirement already satisfied: defusedxml in /opt/anaconda3/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.7.1)\n",
      "Requirement already satisfied: nbclient<0.6.0,>=0.5.0 in /opt/anaconda3/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.3)\n",
      "Requirement already satisfied: jupyterlab-pygments in /opt/anaconda3/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.1.2)\n",
      "Requirement already satisfied: testpath in /opt/anaconda3/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.4.4)\n",
      "Requirement already satisfied: bleach in /opt/anaconda3/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.3.0)\n",
      "Requirement already satisfied: pandocfilters>=1.4.1 in /opt/anaconda3/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.4.3)\n",
      "Requirement already satisfied: nest-asyncio in /opt/anaconda3/lib/python3.8/site-packages (from nbclient<0.6.0,>=0.5.0->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.5.1)\n",
      "Requirement already satisfied: async-generator in /opt/anaconda3/lib/python3.8/site-packages (from nbclient<0.6.0,>=0.5.0->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.10)\n",
      "Requirement already satisfied: webencodings in /opt/anaconda3/lib/python3.8/site-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.1)\n",
      "Requirement already satisfied: pyparsing>=2.0.2 in /opt/anaconda3/lib/python3.8/site-packages (from packaging->streamlit) (2.4.7)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in /opt/anaconda3/lib/python3.8/site-packages (from requests->streamlit) (2.0.12)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /opt/anaconda3/lib/python3.8/site-packages (from requests->streamlit) (1.26.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /opt/anaconda3/lib/python3.8/site-packages (from requests->streamlit) (2021.10.8)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /opt/anaconda3/lib/python3.8/site-packages (from requests->streamlit) (2.10)\n",
      "Requirement already satisfied: backports.zoneinfo in /opt/anaconda3/lib/python3.8/site-packages (from tzlocal->streamlit) (0.2.1)\n",
      "Requirement already satisfied: pytz-deprecation-shim in /opt/anaconda3/lib/python3.8/site-packages (from tzlocal->streamlit) (0.1.0.post0)\n",
      "Requirement already satisfied: tzdata in /opt/anaconda3/lib/python3.8/site-packages (from pytz-deprecation-shim->tzlocal->streamlit) (2021.5)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "96921e0f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tweepy as tw\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "from transformers import pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "313e7401",
   "metadata": {},
   "outputs": [],
   "source": [
    "consumer_key = 'HkE5YJuv01c4bbq1GVc8SfNo4'\n",
    "consumer_secret = 'fdSpo4SJjOKgDBtitXcKZ4s6Oe2KAgZDtwGoQ1JFoZre02AjT4'\n",
    "access_token = '455536583-boFHn3N5TG6dDrTT0sJHbB0ehyzHyRZkakLCSkQ3'\n",
    "access_token_secret = 'Ygw5qCpWu0RLL3KJnt3SKzjUqgQg1rtkUdJPVuDSeDROU'\n",
    "\n",
    "auth = tw.OAuthHandler(consumer_key, consumer_secret)\n",
    "auth_handler.set_access_token(access_token, access_token_secret)\n",
    "\n",
    "api = tw.API(auth, wait_on_rate_limit=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "88d5337a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "No model was supplied, defaulted to distilbert-base-uncased-finetuned-sst-2-english (https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english)\n",
      "2022-05-18 09:56:48.841 INFO    filelock: Lock 140549801942464 acquired on /Users/sharraeallen/.cache/huggingface/transformers/4e60bb8efad3d4b7dc9969bf204947c185166a0a3cf37ddb6f481a876a3777b5.9f8326d0b7697c7fd57366cdde57032f46bc10e37ae81cb7eb564d66d23ec96b.lock\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2d2db1f948884badb04f5f5cdde164d7",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Downloading:   0%|          | 0.00/629 [00:00<?, ?B/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-05-18 09:56:50.073 INFO    filelock: Lock 140549801942464 released on /Users/sharraeallen/.cache/huggingface/transformers/4e60bb8efad3d4b7dc9969bf204947c185166a0a3cf37ddb6f481a876a3777b5.9f8326d0b7697c7fd57366cdde57032f46bc10e37ae81cb7eb564d66d23ec96b.lock\n",
      "2022-05-18 09:56:51.289 INFO    filelock: Lock 140548912881232 acquired on /Users/sharraeallen/.cache/huggingface/transformers/8d04c767d9d4c14d929ce7ad8e067b80c74dbdb212ef4c3fb743db4ee109fae0.9d268a35da669ead745c44d369dc9948b408da5010c6bac414414a7e33d5748c.lock\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "884b3412afef4030ba7dcbd9b9f42371",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Downloading:   0%|          | 0.00/255M [00:00<?, ?B/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-05-18 09:57:32.154 INFO    filelock: Lock 140548912881232 released on /Users/sharraeallen/.cache/huggingface/transformers/8d04c767d9d4c14d929ce7ad8e067b80c74dbdb212ef4c3fb743db4ee109fae0.9d268a35da669ead745c44d369dc9948b408da5010c6bac414414a7e33d5748c.lock\n",
      "2022-05-18 09:57:34.360 INFO    filelock: Lock 140548936414544 acquired on /Users/sharraeallen/.cache/huggingface/transformers/d44ec0488a5f13d92b3934cb68cc5849bd74ce63ede2eea2bf3c675e1e57297c.627f9558061e7bc67ed0f516b2f7efc1351772cc8553101f08748d44aada8b11.lock\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3e54aece1cf9407aada88f76c7a92d82",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Downloading:   0%|          | 0.00/48.0 [00:00<?, ?B/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-05-18 09:57:34.932 INFO    filelock: Lock 140548936414544 released on /Users/sharraeallen/.cache/huggingface/transformers/d44ec0488a5f13d92b3934cb68cc5849bd74ce63ede2eea2bf3c675e1e57297c.627f9558061e7bc67ed0f516b2f7efc1351772cc8553101f08748d44aada8b11.lock\n",
      "2022-05-18 09:57:36.460 INFO    filelock: Lock 140548936414064 acquired on /Users/sharraeallen/.cache/huggingface/transformers/83261b0c74c462e53d6367de0646b1fca07d0f15f1be045156b9cf8c71279cc9.d789d64ebfe299b0e416afc4a169632f903f693095b4629a7ea271d5a0cf2c99.lock\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "7f824b50d4f4479d93c80d22a4f791d4",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Downloading:   0%|          | 0.00/226k [00:00<?, ?B/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-05-18 09:57:37.534 INFO    filelock: Lock 140548936414064 released on /Users/sharraeallen/.cache/huggingface/transformers/83261b0c74c462e53d6367de0646b1fca07d0f15f1be045156b9cf8c71279cc9.d789d64ebfe299b0e416afc4a169632f903f693095b4629a7ea271d5a0cf2c99.lock\n"
     ]
    }
   ],
   "source": [
    "classifier = pipeline('sentiment-analysis')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2a410b56",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-05-18 09:58:41.654 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /opt/anaconda3/lib/python3.8/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.title('Live Twitter Sentiment Analysis with Tweepy and HuggingFace Transformers')\n",
    "st.markdown('This app uses tweepy to get tweets from twitter based on the input name/phrase. It then processes the tweets through HuggingFace transformers pipeline function for sentiment analysis. The resulting sentiments and corresponding tweets are then put in a dataframe for display which is what you see as result.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "a3275f71",
   "metadata": {},
   "outputs": [],
   "source": [
    "def run():\n",
    "    with st.form(key=\"Enter name\"):\n",
    "        search_words = st.text_input(\"Enter the name for which you want to know the sentiment\")\n",
    "        number_of_tweets = st.number_input(\"Enter the number of latest tweets for which you want to know the sentiment(Maximum 50 tweets)\", 0,50,10)\n",
    "        submit_button = st.form_submit_button(label=\"Submit\")\n",
    "    if submit_button:\n",
    "        tweets =tw.Cursor(api.search_tweets,q=search_words,lang=\"en\").items(number_of_tweets)\n",
    "        tweet_list = [i.text for i in tweets]\n",
    "        p = [i for i in classifier(tweet_list)]\n",
    "        q=[p[i][\"label\"] for i in range(len(p))]\n",
    "        df = pd.DataFrame(list(zip(tweet_list, q)),columns =[\"Latest \"+str(number_of_tweets)+' Tweets'+ 'on' +search_words, 'sentiment'])\n",
    "    st.write(df)\n",
    " \n",
    "\n",
    "    if __name__==\"__main__\":\n",
    "        run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "78dbff76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\"name\": null}\n",
      "<class 'str'>\n",
      "{'name': None}\n",
      "<class 'dict'>\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "\n",
    "json_str = json.dumps({'name': None})\n",
    "print(json_str)  # 👉️ '{\"name\": null}'\n",
    "\n",
    "print(type(json_str))  # 👉️ <class 'str'>\n",
    "\n",
    "# ✅ Parse JSON string to native Python object\n",
    "native_python_obj = json.loads(json_str)\n",
    "print(native_python_obj)  # 👉️ {'name': None}\n",
    "\n",
    "print(type(native_python_obj))  # 👉️ <class 'dict'>\n",
    "\n",
    "print(native_python_obj['name'])  # 👉️ None\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
