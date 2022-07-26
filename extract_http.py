from pprint import pprint

from requests import get
from pandas import DataFrame

URL_BASE = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"

if __name__ == "__main__":
    print("1. Conectarse al enlace")
    response = get(URL_BASE)
    body = response.json()
    df = DataFrame(body["items"])

    print("2. Obtener el número de respuestas contestadas y no contestadas")
    answered = df.copy()["is_answered"].value_counts()
    answered.index = answered.index.map(
        {True: "contestada", False: "no contestada"}
    )
    pprint(answered.to_dict())

    print("3. Obtener la respuesta con menor número de vistas ! ->\n")
    respuesta = (
        df[df["view_count"] == df["view_count"].min()].iloc[0].to_dict()
    )
    pprint(respuesta)

    print("4. Obtener la respuesta más vieja ! ->\n")
    respuesta = (
        df[df["creation_date"] == df["creation_date"].min()].iloc[0].to_dict()
    )
    pprint(respuesta)

    print("5. Obtener la respuesta más actual ! \n")
    respuesta = (
        df[df["creation_date"] == df["creation_date"].max()].iloc[0].to_dict()
    )
    pprint(respuesta)

    print(
        "6. Obtener la respuesta del owner que tenga una mayor reputación ! \n"
    )
    respuesta = df[df["score"] == df["score"].max()].iloc[0].to_dict()
    pprint(respuesta)
