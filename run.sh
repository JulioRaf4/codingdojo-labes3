#!/bin/bash

# Comando para rodar o projeto
uvicorn api.main:app --reload --lifespan on
