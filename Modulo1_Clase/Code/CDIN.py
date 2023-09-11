import string
import numpy as np
import pandas as pd

class CDIN:
    def __init__(self, df):
        self.data = df
    # Métodos para clasificación de Datos en un DataFrame (Cualitativos, Cuantitativos, Binarios)
    
    #def get_cuantitativos:
    #    return col_cuantitativos, df_cuantitativos
    
    #def get_cualitativos:
    #    return col_cualitativos, df_cualitativos
    
    def get_binaries(self):
        df_cat = self.data.select_dtypes(include=['object']).copy()
        column_cat = df_cat.columns
        column_binaries = []
        for col in column_cat:
            if df_cat[col].nunique() == 2:
                column_binaries.append(col)
        return column_binaries, self.data[column_binaries]
    
    ## Métodos para la limpieza de datos
    
    # remover signos de puntuación
    @staticmethod
    def remove_punctuation(x):
        try:
            x = ''.join(ch for ch in x if ch not in string.punctuation)
        except:
            print(f'{x} no es una cadena de caracteres')
            pass
        return x
    @staticmethod
    def remove_digits(x):
        try:
            x = "".join(ch for ch in x if ch not in string.digits)
        except:
            print(f'{x} no es una cadena de caracteres')
            pass
        return x
    #remover espacios en blanco
    @staticmethod
    def remove_whitespace(x):
        try:
            x=' '.join(x.split())
        except:
            pass
        return x
    #convertimos a minúsculas
    @staticmethod
    def lower_text(x):
        try:
            x=x.lower()
        except:
            pass
        return x
    #Convertimos a mayúsculas
    @staticmethod
    def upper_text(x):
        try:
            x=x.upper()
        except:
            pass
        return x
    # función convierta a mayúsculas la primera letra
    @staticmethod
    def capitalize_text(x):
        try:
            x = x.capitalize()
        except:
            pass
        return x
    @staticmethod
    def replace_text(x,to_replace, replacement):
        try:
            x = x.replace(to_replace,replacement)
        except:
            pass
        return x