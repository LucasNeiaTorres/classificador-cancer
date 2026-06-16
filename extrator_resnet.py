import os

import pandas as pd


# 1. Le o CSV
df_treino = pd.read_csv("csv/mass_case_description_train_set.csv")

# 2. Pega apenas as 5 primeiras linhas para teste rapido
amostra_teste = df_treino.head(5)

# 3. Faz um loop por essas 5 linhas
for index, row in amostra_teste.iterrows():
    # Pega o caminho anotado no CSV
    caminho_csv_crop = row["cropped image file path"]

    # Ajusta o caminho do CSV para a pasta local JPEG
    caminho_local_crop = caminho_csv_crop.replace("CBIS-DDSM/", "jpeg/").replace(".dcm", ".jpg")
    caminho_local_crop = caminho_local_crop.replace("\n", "").strip()

    print(f"[{index}] Procurando imagem em: {caminho_local_crop}")

    # Verifica se o arquivo existe localmente
    if os.path.exists(caminho_local_crop):
        print(" -> Arquivo ENCONTRADO! Pronto para a ResNet50.")
    else:
        print(" -> Arquivo não encontrado. Precisamos ajustar o nome da pasta.")