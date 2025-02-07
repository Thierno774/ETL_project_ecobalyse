import requests
import json
import random
import time
import os 

# Définir l'URL de l'API et les en-têtes
API_URL = "https://ecobalyse.beta.gouv.fr/api" # Remplacez par l'URL de votre API
TOKEN = "b1635d73-6459-4e8f-a648-e6ceb41b0977"
HEADERS = {
    "token": TOKEN
}

# Fonction pour lancer les simulations
def fetch_simulation(data):
    response = requests.post(f"{API_URL}/textile/simulator", headers=HEADERS, json=data)
    response.raise_for_status()
    return response.json()

def generate_simulations(**kwargs):
    max_requests_per_minute = kwargs["max_requests_per_minute"]
    simulations = []
    request_count = 0
    start_time = time.time()
    #get the data that present in directory 
    current_dag_directory = os.path.dirname(os.path.abspath(__file__))
    # Specify the directory to save data 
    directory_to_save_data = os.path.join(current_dag_directory, "Output", "data")
    filename = os.path.join(directory_to_save_data, "schemas.json")
    
    with open(filename, 'r') as file:
        data = json.load(file)

    for scenario in (data):
        if request_count >= max_requests_per_minute:
            elapsed_time = time.time() - start_time
            if elapsed_time < 60:
                sleep_time = 60 - elapsed_time
                print(f"Limite atteinte, attente de {sleep_time:.2f} secondes.")
                time.sleep(sleep_time)
            start_time = time.time()
            request_count = 0
        
        # Réaliser la simulation
        try:
            simulation_result = fetch_simulation(scenario)
            simulations.append(simulation_result)
            request_count += 1
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la simulation : {e}")
    
    return simulations

