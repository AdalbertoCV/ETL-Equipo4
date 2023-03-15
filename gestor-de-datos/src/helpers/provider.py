import requests

host = "http://dgraph"
port = "8080"

class Provider:

    @staticmethod
    def perform_mutate(data):
        headers = {
            "Content-Type": "application/rdf"
        }
        response = requests.post(f"{host}:{port}/mutate?commitNow=true", data=data, headers=headers)
        return response

    @staticmethod
    def perform_query(data):
        headers = {
            "Content-Type": "application/dql"
        }
        response = requests.post(f"{host}:{port}/query", data=data, headers=headers)
        return response

    @staticmethod
    def perform_alter(data):
        headers = {
            "Content-Type": "text/plain"
        }
        response = requests.post(f"{host}:{port}/alter", data=data, headers=headers)
        return response