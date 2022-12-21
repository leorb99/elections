"""
Data about federal elections
"""
import os
import time
import pandas as pd
from classes import Candidate

start = time.time()
CONSULT = "/consulta_cand_2022/consulta_cand_2022_"
ASSETS = "/bem_candidato_2022/bem_candidato_2022_"
VOTING = "/votacao_candidato_munzona_2022/votacao_candidato_munzona_2022_"

STATES = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO",
          "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI",
          "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

list_cand = []
# pylint: disable=no-member
for sg in STATES:
    votes_cand = {}
    patrimony_cand = {}
    sg_cand = []

    candidates = pd.read_csv(os.getcwd() +
                            f"{CONSULT + sg}.csv",
                            sep=";", encoding="iso-8859-1")

    cand_assets = pd.read_csv(os.getcwd() +
                            f"{ASSETS + sg}.csv",
                            sep=";", encoding="iso-8859-1")

    cand_votes = pd.read_csv(os.getcwd() +
                            f"{VOTING + sg}.csv",
                            sep=";", encoding="iso-8859-1")

    for i in range(len(candidates)):
        if (candidates.at[i, "DS_CARGO"] == "DEPUTADO FEDERAL"
            and candidates.at[i, "DS_SITUACAO_CANDIDATURA"] != "INAPTO"):
            num_code = candidates.at[i, "SQ_CANDIDATO"]
            name = candidates.at[i, "NM_URNA_CANDIDATO"]
            age = candidates.at[i, "NR_IDADE_DATA_POSSE"]
            gender = candidates.at[i, "DS_GENERO"]
            color = candidates.at[i, "DS_COR_RACA"]
            party = (candidates.at[i, "SG_PARTIDO"] +
            " - " + candidates.at[i, "NM_PARTIDO"])
            number = candidates.at[i, "NR_CANDIDATO"]
            marital_status = candidates.at[i, "DS_ESTADO_CIVIL"]
            profession = candidates.at[i, "DS_OCUPACAO"]
            schooling = candidates.at[i, "DS_GRAU_INSTRUCAO"]
            status = candidates.at[i, "DS_SIT_TOT_TURNO"]
            state = candidates.at[i, "NM_UE"] + " - " + sg
            reelection = candidates.at[i, "ST_REELEICAO"]
            # I couldn't find a source for the variable 'spent'.
            cand = Candidate(num_code, party, number, marital_status,
                             profession, schooling, state, status, spent=0)
            cand.set_name(name)
            cand.set_age(age)
            cand.set_gender(gender)
            cand.set_color(color)

            if (reelection == "S" and cand.get_status() == "ELEITO POR QP" or
                cand.get_status() == "ELEITO POR MÉDIA"):
                cand.set_reelected(True)

            votes_cand[num_code] = 0
            patrimony_cand[num_code] = 0
            list_cand.append(cand)
            sg_cand.append(cand)

    # The votes and patrimony are in databases.
    # To calculate the votes and the patrimony of each candidate, first we need
    # to verify if the 'SQ_CANDIDATO' is a key of the dictionary and if the
    # value of this key is 0. Then we need to search all the 'SQ_CANDIDATO'
    # with the same key and sum them. When the value of a key is different from
    # 0, this value has already been calculated.
    for i in range(len(cand_assets)):
        if (cand_assets.at[i, "SQ_CANDIDATO"] in patrimony_cand
            and patrimony_cand[cand_assets.at[i, "SQ_CANDIDATO"]] == 0):
            for j in range(i, len(cand_assets)):
                if cand_assets.at[j, "SQ_CANDIDATO"] in patrimony_cand:
                    patrimony = float(cand_assets.at[j, "VR_BEM_CANDIDATO"].replace(",", "."))
                    patrimony_cand[cand_assets.at[j, "SQ_CANDIDATO"]] += patrimony
            break

    for i in range(len(cand_votes)):
        if (cand_votes.at[i, "SQ_CANDIDATO"] in votes_cand
            and votes_cand[cand_votes.at[i, "SQ_CANDIDATO"]] == 0):
            for j in range(i, len(cand_votes)):
                if cand_votes.at[j, "SQ_CANDIDATO"] in votes_cand:
                    votes = cand_votes.at[j, "QT_VOTOS_NOMINAIS_VALIDOS"]
                    votes_cand[cand_votes.at[j, "SQ_CANDIDATO"]] += votes
            break

    # Sets the votes and patrimony for each candidate
    for c in sg_cand:
        for k, v in votes_cand.items():
            if c.get_num_code() == k:
                c.set_votes(v)
        for k, v  in patrimony_cand.items():
            if c.get_num_code() == k:
                c.set_patrimony(f"{v:.2f}")

df = pd.DataFrame([c.__dict__ for c in list_cand])
df.to_csv("data.csv", sep=";", encoding="iso-8859-1")
end = time.time()
a = end - start
print(f"{int(a//60):02d}:{int(a%60):02d}")
