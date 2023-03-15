from datetime import date, timedelta
import requests, json, random

class Processor:

    @staticmethod
    def extract_created_uid(res, key):
        assert isinstance(res, requests.Response)

        if res.status_code == 200:
            response = json.loads(res.text)

            if not 'data' in response.keys():
                return None

            if not 'uids' in response["data"].keys():
                return None

            return response["data"]["uids"][key]
        return None

    @staticmethod
    def extract_query_uid(res):
        assert isinstance(res, requests.Response)

        if res.status_code == 200:
            response = json.loads(res.text)

            if not 'data' in response.keys():
                return None

            try:
                if not 'response' in response["data"].keys():
                    return None
            except Exception as e:
                print(res.text)
                return None

            if len(response["data"]["response"]) == 0:
                return None

            return response["data"]["response"][0]["uid"]
        return None

    @staticmethod
    def extract_relation_uids(res, relation):
        assert isinstance(res, requests.Response)

        if res.status_code == 200:
            response = json.loads(res.text)

            if not 'data' in response.keys():
                return []

            if not 'response' in response["data"].keys():
                return []

            if len(response["data"]["response"]) == 0:
                return []

            relations = response["data"]["response"][0][relation]
            return [rel["uid"] for rel in relations]
        return []

    @staticmethod
    def compute_random_date():
        end_date = date.today()
        start_date = date(end_date.year, 1, 1)

        diff_days = (end_date - start_date).days
        random_days = random.randint(1, diff_days)
        start_date = start_date + timedelta(days=random_days)
        return start_date.strftime('%Y-%m-%d')
