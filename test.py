import pandas as pd
import os
from classes import *
import time
import requests
# start = time.time()
# list_cand = []
# d = {}

# candidates = pd.read_csv(os.getcwd() + 
#                         f"/consulta_cand_2022/consulta_cand_2022_DF.csv",
#                         sep=";", encoding="iso-8859-1")
# cand_assets = pd.read_csv(os.getcwd() + 
#                         f"/bem_candidato_2022/bem_candidato_2022_DF.csv",
#                         sep=";", encoding="iso-8859-1")

# cand_votes = pd.read_csv(os.getcwd() +
#                         f"/votacao_candidato_munzona_2022/votacao_candidato_munzona_2022_DF.csv",
#                         sep=";", encoding="iso-8859-1")


# for i in range(len(candidates)):
#     flag = False
    
#     if (candidates.at[i, "DS_CARGO"] == "DEPUTADO FEDERAL") and (candidates.at[i, "DS_SITUACAO_CANDIDATURA"] != "INAPTO"):
#         num_code = candidates.at[i, "SQ_CANDIDATO"]
#         name = candidates.at[i, "NM_URNA_CANDIDATO"]
#         age = candidates.at[i, "NR_IDADE_DATA_POSSE"]
#         gender = candidates.at[i, "DS_GENERO"]
#         color = candidates.at[i, "DS_COR_RACA"]
#         party = candidates.at[i, "SG_PARTIDO"] + " - " + candidates.at[i, "NM_PARTIDO"]
#         number = candidates.at[i, "NR_CANDIDATO"]
#         marital_status = candidates.at[i, "DS_ESTADO_CIVIL"]
#         profession = candidates.at[i, "DS_OCUPACAO"]
#         schooling = candidates.at[i, "DS_GRAU_INSTRUCAO"]
#         status = candidates.at[i, "DS_SIT_TOT_TURNO"]
#         spent = candidates.at[i, "VR_DESPESA_MAX_CAMPANHA"]
#         cand = Candidate(num_code, party, number, marital_status, 
#                          profession, schooling, "DF", status, spent)
#         cand.set_name(name)
#         cand.set_age(age)
#         cand.set_gender(gender)
#         cand.set_color(color)
#         patrimony = 0
#         flag = True
#         d[cand_votes.at[i, "SQ_CANDIDATO"]] = 0
        
#         for i in range(len(cand_assets)):
#             if cand_assets.at[i, "SQ_CANDIDATO"] == cand.get_num_code():
#                 patrimony += float(cand_assets.at[i, "VR_BEM_CANDIDATO"].replace(",", "."))

#         if flag:
#             # cand.set_votes(votes)        
#             cand.set_patrimony(patrimony)
#             list_cand.append(cand)

# votes = 0
# for i in range(len(cand_votes)):
#     if cand_votes.at[i, "SQ_CANDIDATO"] in d.keys() and d[cand_votes.at[i, "SQ_CANDIDATO"]] == 0:
#         for j in range(len(cand_votes)):
#             if cand_votes.at[j, "SQ_CANDIDATO"] in d.keys():
#                 d[cand_votes.at[j, "SQ_CANDIDATO"]] += cand_votes.at[j, "QT_VOTOS_NOMINAIS_VALIDOS"]


# print(d)
# print(list_cand[100].get_votes())
# end = time.time()
# a = end-start
# print(f"{int(a//60)}:{int(a%60)}")


data_old = pd.read_csv("data_old.csv", sep=";", encoding="iso-8859-1")
data = pd.read_csv("data.csv", sep=";", encoding="iso-8859-1")

print(data.info())

# for i in range(len(data)):
#     if (data_old.at[i, "_Candidate__patrimony"] != data.at[i, "_Candidate__patrimony"] 
#         and data_old.at[i, "_Candidate__votes"] != data.at[i, "_Candidate__votes"]):
#             print(f"erro linha {i+1}")
