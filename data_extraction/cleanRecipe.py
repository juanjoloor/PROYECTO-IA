import pandas as pd
import emoji


filename = "total-final_clean_data.csv"
letras_mal,cambio = 'áéíóúü','aeiouu'
transform_tildes = str.maketrans(letras_mal,cambio)


def deEmojify(text):
    return emoji.get_emoji_regexp().sub(r'', text)

def _clean_process(df):
    cleanBody = (df['fullText']
                 .apply(lambda row: row.strip("\n \r "))
                 .apply(lambda txt: deEmojify(txt))
                 .apply(lambda txt: txt.lower())
                 .apply(lambda txt: txt.translate(transform_tildes))
                 )
    df['fullText'] = cleanBody
      #apply por cada valor en la columna full text aplica una funcion

def _save_data(df,filename):
    cleanFilename = 'reduce_{}'.format(filename)
    df.to_csv(cleanFilename,encoding='utf-8', index=False)

df = pd.read_csv(filename, encoding="latin-1")
print(df.head(n=5))

_clean_process(df)
_save_data(df,"prueba_sin_tildes.csv")
print(df.head(n=5))