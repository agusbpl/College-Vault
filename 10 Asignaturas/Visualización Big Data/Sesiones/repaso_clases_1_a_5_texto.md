# Repaso General: Clases 1 a 5 de Visualización de Grandes Volúmenes de Datos

Bienvenido al repaso integral de Visualización de Datos para la cátedra de César Estrebou en la Universidad Nacional de La Plata. Hoy recorremos los conceptos troncales de las primeras cinco clases.

### Clase 1: Fundamentos y Propósito Cognitivo
La visualización no es decoración estética; es una herramienta para amplificar la cognición humana. El Cuarteto de Anscombe demuestra de forma contundente por qué la estadística descriptiva tradicional no alcanza. Cuatro conjuntos de datos con idéntica media, varianza, correlación y recta de regresión revelan realidades geométricas completamente opuestas al graficarlos: desde relaciones lineales clásicas y curvas no lineales, hasta patrones con valores atípicos severos.
Según Tamara Munzner, distinguimos tres metas esenciales: Exploración, orientada a descubrir preguntas e hipótesis en datos desconocidos; Análisis o Confirmación, para corroborar hipótesis previas; y Comunicación o Presentación, cuyo fin es sintetizar y transmitir un hallazgo a una audiencia.

### Clase 2: Percepción, Gestalt y Canales Visuales
La visión humana procesa estímulos en dos etapas: el procesamiento preatencional, que ocurre en menos de 250 milisegundos de forma paralela en la corteza visual sin esfuerzo consciente; y el procesamiento atencional, que es secuencial y requiere foco cognitivo. Atributos como el color, la orientación o el tamaño saltan a la vista de inmediato gracias a este mecanismo.
Las Leyes de la Gestalt, como proximidad, similitud, continuidad y cierre, explican cómo el cerebro agrupa elementos individuales en un todo perceptivo coherente.
En cuanto a codificación visual, Jacques Bertin y los estudios fundamentales de Cleveland y McGill establecieron una jerarquía rigurosa de efectividad perceptual. Para datos cuantitativos, el canal más preciso es la posición en una escala común alineada, seguido de la posición no alineada, longitud, ángulo y pendiente, área, volumen y, finalmente, color y luminosidad.
Para el uso del color, aplicamos tres tipos de paletas según el tipo de dato: Paletas Categóricas o Cualitativas, con matices diferenciados para variables sin orden; Paletas Secuenciales, basadas en gradientes de luminosidad para magnitudes cuantitativas ordenadas; y Paletas Divergentes, estructuradas a partir de un valor central neutro y dos extremos opuestos.

### Clase 3: El Pipeline de Visualización y Tipos de Atributos
El proceso de visualización sigue el pipeline clásico propuesto por Card, Mackinlay y Shneiderman: desde los datos crudos en su origen, pasando por la transformación hacia tablas de datos limpias y estructuradas, la definición de estructuras visuales con marcas y canales, hasta la generación de las vistas interactivas finales.
Diferenciamos tres tipos de atributos:
Categóricos o Nominales, donde no existe orden y sólo podemos verificar igualdad o diferencia;
Ordinales, que poseen un orden intrínseco pero carecen de una distancia métrica precisa entre categorías;
Y Cuantitativos, que representan magnitudes medibles continuas o discretas y admiten operaciones aritméticas.
Entre las transformaciones indispensables destacan la limpieza de datos, el filtrado, la agregación, la derivación de nuevos atributos y el ordenamiento.

### Clase 4: Visualización de Datos Tabulares
Para datos tabulares univariados y bivariados, las tareas principales son comparación, distribución y correlación.
En gráficos de barras, el ordenamiento no es un detalle secundario: ordenar las categorías según la magnitud cuantitativa reduce drásticamente el costo cognitivo de comparación respecto al orden alfabético arbitrario.
Para distribuciones, contrastamos el Histograma, cuyo comportamiento depende críticamente del ancho de los intervalos o bins, con el Diagrama de Caja y Bigotes o Boxplot de Tukey. El boxplot sintetiza la distribución mediante cinco medidas: el valor mínimo no atípico, el primer cuartil Q1, la mediana Q2, el tercer cuartil Q3, y el valor máximo no atípico. La dispersión se mide con el rango intercuartil IQR, que es la diferencia entre Q3 y Q1. Todo valor ubicado más allá de uno punto cinco veces el IQR respecto a los cuartiles se clasifica formalmente como un dato atípico u outlier.
Para correlación bivariada, el diagrama de dispersión es el estándar, debiendo gestionar el sobretrazado mediante transparencia o densidades hexagonales cuando el volumen de datos aumenta.

### Clase 5: Visualización Multidimensional y Limitaciones de Mapeo
Al superar las dos o tres dimensiones, recurrimos a técnicas avanzadas como los Mapas de Calor o Heatmaps, que visualizan matrices numéricas mediante codificación de color y se potencian con agrupamiento jerárquico para reorganizar filas y columnas por similitud.
Las Coordenadas Paralelas representan cada variable en un eje vertical independiente y cada observación como una línea poligonal que cruza todos los ejes. Permiten detectar patrones multidimensionales sin oclusión, pero su efectividad depende críticamente del orden relativo en que se ubiquen los ejes adyacentes.
Finalmente, recordamos la Regla de Expresividad de Mackinlay: una visualización debe expresar toda la información contenida en los datos y nada más que la información contenida. El error más común y peligroso es mapear una variable categórica sin orden a un canal de magnitud como el tamaño, ya que induce erróneamente en el observador la percepción de una jerarquía o importancia que los datos reales no poseen.

Con estos cinco pilares dominados, estamos listos para avanzar hacia series temporales y visualizaciones especializadas.
