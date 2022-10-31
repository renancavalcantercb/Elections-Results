import re
from datetime import datetime

import requests


# function to format numbers with thousands separator
def format_number(number):
    return re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', number)


# function to get the info from TSE API
def main():
    # API URL
    url = "https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json"

    response = requests.request("GET", url)

    response = response.json()
    cand = response['cand']

    # info about the candidate with the most votes
    cand_0 = cand[0]
    cand_0_name = cand_0['nm']
    cand_0_votes = format_number(cand_0['vap'])
    cand_0_percent = cand_0['pvap']

    # info about the candidate with the second most votes
    cand_1 = cand[1]
    cand_1_name = cand_1['nm']
    cand_1_votes = format_number(cand_1['vap'])
    cand_1_percent = cand_1['pvap']

    # get the current time
    time = f"Informações coletada às {datetime.now().strftime('%H:%M:%S')}"
    cand_0 = f"O candidato {cand_0_name} tem {cand_0_votes} votos, o que representa {cand_0_percent}% dos " \
             f"votos válidos. "
    cand_1 = f"O candidato {cand_1_name} tem {cand_1_votes} votos, o que representa {cand_1_percent}% dos votos válidos."
    total = f"Já foram contabilizados {response['pst']}% votos."

    return f"{time}\n{cand_0}\n{cand_1}\n{total}"


if __name__ == '__main__':
    print(main())
