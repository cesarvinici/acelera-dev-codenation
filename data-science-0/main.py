#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[87]:


import pandas as pd
import numpy as np


# In[88]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[89]:


black_friday.head()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[90]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape
    


# In[94]:


q1()


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[91]:


def q2():
    # opção perigosa de resposta 
    #   print(black_friday.groupby('Gender')['Age'].value_counts()[0])
    mulheres = black_friday['Gender'] == 'F'
    idade_base = black_friday['Age'] == '26-35'
    return black_friday[mulheres & idade_base].shape[0]


# In[93]:


q2()


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[95]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return black_friday['User_ID'].nunique()


# In[96]:


q3()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[45]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return black_friday.dtypes.nunique()


# In[97]:


q4()


# In[128]:


dados_do_df = pd.DataFrame({"Tipos": black_friday.dtypes,
                            "Qtde. NA": black_friday.isnull().sum(),
                            "NA %": (black_friday.isna().sum() / black_friday.shape[0]) * 100})


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[256]:


(black_friday.isna().sum() / black_friday.shape[0]).sort_values(ascending=False).to_list()[0]


# In[257]:


def q5():
    # Retorne aqui o resultado da questão 5.
    return (black_friday.isna().sum() / black_friday.shape[0]).sort_values(ascending=False).to_list()[0]


# In[258]:


q5()


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[168]:


type(dados_do_df["Qtde. NA"].sort_values(ascending=False).to_list()[0])


# In[169]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return dados_do_df["Qtde. NA"].sort_values(ascending=False).to_list()[0]


# In[170]:


q6()


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[225]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return black_friday[['Product_Category_3']].dropna()['Product_Category_3'].value_counts().index.to_list()[0]


# In[226]:


q7()


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[186]:


# black_friday['Purchase_norm'] = black_friday['Purchase'].apply(lambda x: (x - black_friday['Purchase'].min()) / (black_friday['Purchase'].max() - black_friday['Purchase'].min()))


# In[198]:


def q8():
    # Retorne aqui o resultado da questão 8.
    #black_friday['Purchase_norm'].mean() 
    return 0.38479390362696736


# In[199]:


q8()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[243]:


def q9():
    # Retorne aqui o resultado da questão 9.
    total = 0
    for i in (black_friday['Purchase'] - black_friday['Purchase'].mean()) / black_friday['Purchase'].std():
        total += i > -1 and i < 1

    return total


# In[244]:


q9()


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[201]:


def q10():
    # Retorne aqui o resultado da questão 10.
    return bool(black_friday[black_friday['Product_Category_2'].isnull()].shape[0] == black_friday[black_friday['Product_Category_2'].isnull()]['Product_Category_3'].isnull().sum())


# In[203]:


q10()

