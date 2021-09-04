import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.metrics import mean_squared_error
import wget
import zipfile
import urllib.request
import os

dirname = os.path.dirname(__file__)
print(dirname)

url = 'http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip'
url2 = urllib.request.urlretrieve(url, dirname+'/ejemplo.zip')
print(url2[0])

with zipfile.ZipFile(url2[0], "r") as zip_ref:
  zip_ref.extractall(dirname)

doc = pd.read_csv('./210904COVID19MEXICO.csv')
doc = doc.drop(columns=['SECTOR','ENTIDAD_UM', 'ENTIDAD_NAC','ENTIDAD_RES','MUNICIPIO_RES', 'TIPO_PACIENTE','FECHA_INGRESO','FECHA_SINTOMAS','FECHA_DEF','INTUBADO','NACIONALIDAD','EMBARAZO','HABLA_LENGUA_INDIG','INDIGENA', 'OTRA_COM','TOMA_MUESTRA_LAB','TOMA_MUESTRA_ANTIGENO','RESULTADO_LAB','ID_REGISTRO','MIGRANTE','PAIS_NACIONALIDAD','PAIS_ORIGEN','UCI','FECHA_ACTUALIZACION','ORIGEN','RESULTADO_ANTIGENO','OTRO_CASO'])
doc = doc.query('SEXO==1 or SEXO==2')
doc = doc.query('NEUMONIA==1 or NEUMONIA==2')
doc = doc.query('DIABETES==1 or DIABETES==2')
doc = doc.query('EPOC==1 or EPOC==2')
doc = doc.query('ASMA==1 or ASMA==2')
doc = doc.query('INMUSUPR==1 or INMUSUPR==2')
doc = doc.query('HIPERTENSION==1 or HIPERTENSION==2')
doc = doc.query('CARDIOVASCULAR==1 or CARDIOVASCULAR==2')
doc = doc.query('OBESIDAD==1 or OBESIDAD==2')
doc = doc.query('RENAL_CRONICA==1 or RENAL_CRONICA==2')
doc = doc.query('TABAQUISMO==1 or TABAQUISMO==2')
doc = doc.query('CLASIFICACION_FINAL==3 or CLASIFICACION_FINAL==7')

convertion = {
    "CLASIFICACION_FINAL":{
        3:1,
        7:2
    }
}

doc.replace(convertion, inplace=True)

doc_train = doc.sample(frac=0.8, random_state=0)
doc_test = doc.drop(doc_train.index)
doc_test2_label = doc_test.pop('CLASIFICACION_FINAL')
women = doc_train.loc[doc_train.SEXO == 1]["CLASIFICACION_FINAL"]
rate_mujer = sum(women)/len(women)
print("% of women with covid:", rate_mujer)
men = doc_train.loc[doc_train.SEXO == 2]["CLASIFICACION_FINAL"]
rate_hombre = sum(men)/len(men)
print("% of men with covid:", rate_hombre)
y = doc_train["CLASIFICACION_FINAL"]

features = ["SEXO", "NEUMONIA", "EDAD", "DIABETES",'EPOC','ASMA','INMUSUPR','HIPERTENSION','CARDIOVASCULAR','OBESIDAD','RENAL_CRONICA','TABAQUISMO']
X = pd.get_dummies(doc_train[features])
X_test = pd.get_dummies(doc_test[features])

model = RandomForestClassifier(n_estimators=20, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'SEXO': doc_test.SEXO, 'POSITIVO': predictions})
print(output)
error = np.sqrt(mean_squared_error(doc_test2_label, predictions))
print(f"Error porcentual: {error * 100}")
paciente = pd.DataFrame(np.array([[1,1,50,1,1,1,2,1,1,2,1,1]]), columns=['SEXO', 'NEUMONIA','EDAD','DIABETES','EPOC','ASMA','INMUSUPR','HIPERTENSION','CARDIOVASCULAR','OBESIDAD','RENAL_CRONICA','TABAQUISMO'])
paciente_prediccion = model.predict(paciente)
print(paciente_prediccion)
