**DESARROLLO Y ANEXO — ENTREGABLE 4**

**Diagnóstico ERP — El Emporio del Terciado S.A.**

*ADN Consultora · Grupo 3 · Tecnologías para la Gestión · UNLP 2026*

**1\. LECTURA DE LA CONSIGNA Y CRITERIO DE TRABAJO**

La Clase 4 pide analizar la empresa desde la perspectiva de un posible proyecto ERP y sintetizar en una página ejecutiva cuatro dimensiones: módulos ERP, parámetros y datos maestros, usuarios P/O/C y beneficio central. A la vez, el material aclara que el análisis de trabajo puede desarrollarse en páginas adicionales como anexo. Por eso este documento conserva la explicación completa que fundamenta el resumen ejecutivo.

La dinámica de clase propone elegir un proceso clave para practicar el diagnóstico. Sin embargo, la consigna formal del Entregable 4 pide determinar los módulos a partir de los procesos TO-BE definidos en la Clase 3\. Como la Entrega 3 de ADN Consultora mantiene dos procesos TO-BE diferenciados, este análisis toma ambos para no perder continuidad:

• Proceso TO-BE 1: venta presencial con servicio de corte a medida.

• Proceso TO-BE 2: consulta remota de precio, stock y presupuesto.

El criterio rector se mantiene: primero el negocio y los procesos; después la tecnología. Por eso no se parte de una marca de ERP ni se incorporan módulos “porque existen”, sino que cada decisión se vincula con necesidades detectadas previamente.

**2\. CONTINUIDAD CON LA ENTREGA 3**

La Entrega 3 definió una arquitectura común para sostener ambos procesos sin fusionarlos. Los dos recorridos comparten información crítica —productos, precios, clientes y stock— y deben evitar recargas, inconsistencias y pérdida de trazabilidad.

En esa arquitectura ya aparecían las siguientes capacidades:

• ventas y gestión de pedidos;

• inventario/stock multisucursal;

• órdenes de trabajo/taller;

• facturación;

• atención omnicanal;

• cotización/presupuestos;

• integración interna y conectores para sistemas externos.

La Entrega 4 no reemplaza esa arquitectura. El paso nuevo consiste en traducir esas capacidades al lenguaje ERP, distinguiendo qué puede resolverse con módulos del núcleo transaccional y qué podría permanecer como solución complementaria integrada.

**3\. ANÁLISIS DE MÓDULOS ERP**

| Módulo | Prioridad | Qué resuelve | Integración | Estado / observación |
| :---- | :---- | :---- | :---- | :---- |
| Ventas y Distribución | Crítica | Pedido único, remitos/facturación y conversión de presupuesto aceptado sin recarga. | Stock · Taller · Finanzas | Necesario desde el inicio. |
| Logística y Almacenes | Crítica | Stock por sucursal/ubicación, movimientos y reserva de material. | Ventas · Taller · Compras | Necesario desde el inicio. |
| Producción / Taller | Crítica | Orden de trabajo, seguimiento de estados y consumo de materiales. | Ventas · Stock | Aplicable al taller; mermas y reglas exactas a validar. |
| Finanzas y Contabilidad | Alta | Impacto contable, cobranzas, cuentas y consulta económica de las operaciones. | Ventas · Compras | Necesario para cerrar el circuito económico. |
| Compras y Abastecimiento | A validar | Reposición, órdenes de compra y proveedores vinculados al stock. | Stock · Finanzas | Coherente con el ERP, pero el circuito no fue mapeado en profundidad. |
| Recursos Humanos | No priorizado | Legajos, asistencia y liquidación de sueldos. | — | Sin evidencia que lo vuelva prioritario dentro del alcance actual. |

Justificación general:

Ventas, Logística/Almacenes y Producción/Taller forman el núcleo mínimo para sostener el recorrido pedido → reserva de material → trabajo de taller. Finanzas completa el impacto económico y contable de la venta. Compras resulta coherente con una gestión integrada de inventario, pero su prioridad debe confirmarse porque el circuito de reposición no fue relevado con el mismo nivel de detalle. Recursos Humanos no se prioriza porque no existe evidencia dentro del alcance actual que lo convierta en una necesidad crítica del proyecto.

Atención omnicanal y cotización/presupuestos:

La arquitectura de la Entrega 3 los necesita, pero la Clase 4 no obliga a tratarlos como módulos ERP. Según la solución elegida, podrían estar incluidos en el ERP o integrarse mediante API/conectores. En esta etapa conviene conservarlos como capacidades funcionales y no forzar una decisión tecnológica que corresponde al análisis de mercado posterior.

**4\. PARÁMETROS Y DATOS MAESTROS**

La Clase 4 distingue la configuración inicial del sistema de las operaciones diarias. Antes de operar hay que “enseñarle” al ERP cómo funciona la empresa. En El Emporio, la parametrización debe sostener los procesos diseñados y los datos maestros deben ser únicos y reutilizables entre módulos.

| Tipo | Elemento | Por qué se necesita |
| :---- | :---- | :---- |
| Parámetro | Sucursales, depósitos y taller | Permite distinguir ubicaciones y operar con stock multisucursal. |
| Parámetro | Unidades de medida, listas y condiciones comerciales | Necesario para cotizar y vender con criterios consistentes. |
| Parámetro | Estados de pedido y de orden de taller | Hace posible seguir el recorrido y conocer el estado de cada trabajo. |
| Parámetro | Usuarios, roles, permisos y reglas de reserva | Define responsabilidades, accesos y comportamiento operativo. |
| Dato maestro | Productos/materiales, servicios de taller, clientes y precios | Información reutilizada por ventas, stock, presupuestos y taller. |
| Dato maestro | Stock inicial por ubicación; proveedores si se incorpora Compras | Base para operar inventario y, si corresponde, abastecimiento. |

Criterio de migración:

Antes de llevar información al ERP, los datos deberían depurarse y unificarse. La existencia de varias sucursales hace especialmente importante evitar productos duplicados, nombres distintos para un mismo material o listas de precios inconsistentes. No se asume que esos problemas existan en todos los casos; se identifica como una condición de calidad necesaria para la migración.

**5\. USUARIOS DEL SISTEMA — P / O / C**

Según la terminología de la Clase 4:

• P — Parámetros: configura el sistema.

• O — Operaciones: registra transacciones.

• C — Consultas: extrae información.

| Rol funcional | P/O/C | Uso principal | Beneficio / punto de adopción |
| :---- | :---- | :---- | :---- |
| Administración del sistema | P | Configura maestros, parámetros, usuarios y permisos. | Reglas homogéneas; requiere responsable claro. |
| Ventas / atención | O/C | Registra consultas, presupuestos y pedidos; consulta precio y stock. | Evita recarga y respuestas contradictorias. |
| Depósito / stock | O/C | Registra movimientos, reservas y disponibilidad. | Visibilidad compartida entre sucursales. |
| Taller | O/C | Recibe órdenes vinculadas al pedido y actualiza estados/consumos. | Trazabilidad del trabajo; requiere disciplina de actualización. |
| Administración / finanzas | O/C | Gestiona facturación, cobranzas y registros económicos. | Reutiliza datos de la venta y reduce reproceso. |
| Dirección / gerencia | C | Consulta ventas, stock, pedidos y trabajos pendientes. | Información consolidada para seguimiento y decisión. |

La clasificación P/O/C describe el tipo de interacción y no necesariamente un cargo formal. Como no se dispone de un organigrama detallado y confirmado para todos los sectores, se utilizan roles funcionales. Una misma persona podría cumplir más de un rol en la práctica.

**6\. INTEGRACIÓN Y BENEFICIO CENTRAL**

El valor principal del ERP no es tener “muchos módulos”, sino que los módulos compartan datos y que una transacción produzca sus efectos sin recarga manual.

Para El Emporio, el flujo objetivo puede resumirse así:

Consulta/presupuesto → Pedido → Reserva de stock → Orden de taller → Facturación → Información para gestión.

Aplicación al Proceso TO-BE 1 — venta presencial con corte a medida:

1\. El vendedor registra el pedido.

2\. El sistema consulta y reserva material en la fuente común de stock.

3\. Si el pedido requiere corte o transformación, se genera una orden de taller vinculada al mismo pedido.

4\. El taller actualiza el estado y, cuando corresponda, registra consumo de material.

5\. La facturación reutiliza la información ya registrada.

6\. Los datos quedan disponibles para consultas de seguimiento y gestión.

Aplicación al Proceso TO-BE 2 — consulta remota:

1\. La consulta se registra y se utiliza la misma fuente de precios y stock que en el canal presencial.

2\. Se genera una cotización o presupuesto.

3\. Si el cliente no acepta, el proceso puede cerrarse sin generar una venta.

4\. Si acepta, la información se transforma en pedido sin volver a cargar productos, cliente y condiciones ya registradas.

5\. Desde ese punto continúa el recorrido del Proceso 1 cuando corresponda.

Este principio ataca directamente los problemas diagnosticados en entregas anteriores: recarga manual, inconsistencias de información entre canales/sucursales y pérdida de trazabilidad entre ventas, stock y taller.

**7\. TRAZABILIDAD DE LA PROPUESTA**

| Problema / necesidad | TO-BE asociado | Módulo/capacidad | Beneficio esperado |
| :---- | :---- | :---- | :---- |
| Stock informado vs. disponibilidad real | Venta presencial \+ consulta remota | Logística/Almacenes \+ fuente común | Misma disponibilidad para todos los canales y sucursales. |
| Recarga de consulta/presupuesto al vender | Consulta remota | Ventas \+ cotización integrada | Presupuesto aceptado pasa a pedido sin volver a cargar. |
| Pérdida de trazabilidad del trabajo de corte | Venta con corte a medida | Producción/Taller | Orden vinculada al pedido y seguimiento de estados. |
| Información fragmentada entre áreas | Ambos procesos | Integración ERP \+ datos compartidos | Una transacción impacta en módulos relacionados y queda disponible para gestión. |

**8\. ADOPCIÓN Y CAMBIO ORGANIZACIONAL**

El ERP no resuelve por sí solo problemas de proceso. Para que la integración funcione, deberían definirse responsables, reglas de carga, permisos y criterios de actualización. Los principales puntos de atención son:

• capacitación de los usuarios;

• definición clara de quién registra y quién valida cada dato;

• calidad de los datos migrados;

• evitar planillas o registros paralelos que vuelvan a crear silos;

• acompañar el cambio de hábitos de trabajo;

• asegurar que las tres sucursales y el taller utilicen criterios homogéneos.

Estos puntos no se presentan como fallas verificadas de la empresa, sino como condiciones que deberían gestionarse en un proyecto de implementación.

**9\. SUPUESTOS Y VALIDACIONES PENDIENTES**

Antes de seleccionar e implementar una solución concreta deben confirmarse:

• qué sistema utiliza actualmente El Emporio y qué funciones cubre;

• cómo se actualiza y reserva hoy el stock entre sucursales;

• cómo se registra el consumo de material del taller y si se controlan mermas;

• cómo se gestiona el circuito de compras y reposición;

• cómo se articula actualmente facturación con contabilidad y cobranzas;

• qué responsables reales asumirían los roles P/O/C;

• si atención omnicanal y presupuestos pueden ser cubiertos por el ERP elegido o requieren una herramienta complementaria;

• qué datos históricos deben migrarse y con qué nivel de calidad.

**10\. CONCLUSIÓN DEL ANÁLISIS**

La recomendación no es implementar “todo un ERP” de una vez. El núcleo inicial debe responder a los procesos que justifican la inversión: ventas/pedidos, stock multisucursal y taller, integrados con el impacto financiero correspondiente. El resto de los módulos debe incorporarse cuando exista una necesidad validada.

La continuidad con la Entrega 3 se conserva porque los dos procesos TO-BE siguen separados, pero trabajan sobre una arquitectura y una fuente de datos compartidas. La mejora central es que la información se capture una vez y acompañe al pedido durante todo su ciclo, evitando recargas y haciendo trazable la relación entre consulta, venta, stock, taller y administración.

