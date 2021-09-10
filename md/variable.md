
| Variable | Descripcion | Valor |
| ----------- | ----------- | ----------- |
| FECHA_ACTUALIZACION | La base de datos se alimenta diariamente, esta variable permite identificar la fecha de la ultima actualizacion. | Fecha
| ID_REGISTRO | Número identificador del caso | ID
| FECHA_ACTUALIZACION | La base de datos se alimenta diariamente, esta variable permite identificar la fecha de la ultima actualizacion. | Fecha
| ORIGEN | La vigilancia centinela se realiza a través del sistema de unidades de salud monitoras de enfermedades respiratorias (USMER). Las USMER incluyen unidades médicas del primer, segundo o tercer nivel de atención y también participan como USMER las unidades de tercer nivel que por sus características contribuyen a ampliar el panorama de información epidemiológica, entre ellas las que cuenten con especialidad de neumología, infectología o pediatría. (Categorías en Catalógo Anexo). | Numero |
| SECTOR | Identifica el tipo de institución del Sistema Nacional de Salud que brindó la atención. | Numero (1-13, 99)
| ENTIDAD_UM | Identifica la entidad donde se ubica la unidad medica que brindó la atención. | Numero
| SEXO | Identifica al sexo del paciente. | Numero (1, 2, 99)
| ENTIDAD_NAC | Identifica la entidad de nacimiento del paciente. | Numero (1-32, 36, 97, 98, 99)
| ENTIDAD_RES | Identifica la entidad de residencia del paciente. | Numero (1-32, 36, 97, 98, 99)
| MUNICIPIO_RES | Identifica el municipio de residencia del paciente. | Numero (1, 2, 99)
| TIPO_PACIENTE | Identifica el tipo de atención que recibió el paciente en la unidad. Se denomina como ambulatorio si regresó a su casa o se denomina como hospitalizado si fue ingresado a hospitalización. | Fecha
| FECHA_INGRESO | Identifica la fecha de ingreso del paciente a la unidad de atención. | Fecha
| FECHA_SINTOMAS | Idenitifica la fecha en que inició la sintomatología del paciente. | Fecha
| FECHA_DEF | Identifica la fecha en que el paciente falleció. | Fecha
| INTUBADO | Identifica si el paciente requirió de intubación. | Fecha
| NEUMONIA | Identifica si al paciente se le diagnosticó con neumonía. | Fecha
| EDAD | Identifica la edad del paciente. | Fecha
| NACIONALIDAD | Identifica si el paciente es mexicano o extranjero. | Fecha
| EMBARAZO | Identifica si la paciente está embarazada.| Fecha
| HABLA_LENGUA_INDIG | Identifica si el paciente habla lengua índigena. | Fecha| 
| INDIGENA | Identifica si el paciente se autoidentifica como una persona indígena.  | Fecha
| DIABETES | Identifica si el paciente tiene un diagnóstico de diabetes.  | Fecha |
| EPOC | Identifica si el paciente tiene un diagnóstico de EPOC.   | Fecha |
| ASMA | Identifica si el paciente tiene un diagnóstico de asma.   | Fecha |
| INMUSUPR | Identifica si el paciente presenta inmunosupresión.  | Fecha |
| HIPERTENSION | Identifica si el paciente tiene un diagnóstico de hipertensión.   | Fecha |
| OTRAS_COM | Identifica si el paciente tiene diagnóstico de otras enfermedades.  | Fecha |
| CARDIOVASCULAR | Identifica si el paciente tiene un diagnóstico de enfermedades cardiovasculares.   | Fecha |
| OBESIDAD | Identifica si el paciente tiene diagnóstico de obesidad.  | Fecha |
| RENAL_CRONICA | Identifica si el paciente tiene diagnóstico de insuficiencia renal crónica.  | Fecha |
| TABAQUISMO | Identifica si el paciente tiene hábito de tabaquismo.  | Fecha |
| OTRO_CASO | Identifica si el paciente tuvo contacto con algún otro caso diagnósticado con SARS CoV-2.  | Fecha |
| TOMA_MUESTRA_LAB | Identifica si al paciente se le tomó muestra de laboratorio.  | Fecha |
| RESULTADO_LAB | Identifica el resultado del análisis de la muestra reportado por el  laboratorio de la Red Nacional de Laboratorios de Vigilancia Epidemiológica (INDRE, LESP y LAVE) y laboratorios privados avalados por el InDRE cuyos resultados son registrados en SISVER. (Catálogo de resultados diagnósticos anexo).  | Fecha |
| TOMA_MUESTRA_ANTIGENO | Identifica si al paciente se le tomó muestra de antígeno para SARS-CoV-2  | Fecha |
| RESULTADO_ANTIGENO | Identifica el resultado del análisis de la muestra de antígeno tomada al paciente  | Fecha |
| [CLASIFICACION_FINAL](clasificacionF.md) | Identifica si el paciente es un caso de COVID-19 según el catálogo "CLASIFICACION_FINAL".  | Fecha |
| MIGRANTE | Identifica si el paciente es una persona migrante.  | Fecha |
| PAIS_NACIONALIDAD | Identifica la nacionalidad del paciente.  | Fecha |
| PAIS_ORIGEN | Identifica el país del que partió el paciente rumbo a México.  | Fecha |
| UCI | Identifica si el paciente requirió ingresar a una Unidad de Cuidados Intensivos.  | Fecha |