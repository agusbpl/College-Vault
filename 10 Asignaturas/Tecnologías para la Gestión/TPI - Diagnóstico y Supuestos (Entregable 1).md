---
materia: "[[Tecnologías para la Gestión]]"
tipo: TPI
fase: Entregable 1
empresa: "El Emporio del Terciado"
consultora: "Aura Digital Consulting"
estado: Borrador Completo
tags:
  - tpi
  - entregable-1
  - diagnostico-digital
  - supuestos
  - trazabilidad
---

# 🚀 Entregable 1: Diagnóstico Digital, Matriz de Trazabilidad y Procesos AS-IS
### **Empresa Asignada**: El Emporio del Terciado (La Plata)
### **Consultora**: Aura Digital Consulting (*"Claridad estratégica, datos y tecnología para transformar la gestión"*)

> [!abstract] Resumen del Entregable
> Documento preliminar para el **Bloque 1** del Trabajo Práctico Integrador. Contiene el relevamiento del negocio, la justificación rigurosa de cada hipótesis (Señal &rarr; Supuesto &rarr; Razón Razonable &rarr; Pregunta de Validación), el diagnóstico en las 6 dimensiones de madurez digital, la matriz FODA y el diagrama del proceso actual de corte (**AS-IS**).
> 
> 📄 **[[Informe - El Emporio del Terciado.html|Ver Informe Web Interactivo (HTML)]]**

---

## 🔬 1. Matriz de Trazabilidad Metodológica (Señales &rarr; Supuestos &rarr; Razones)

Para cumplir con la consigna de la cátedra de formular **Supuestos Explícitos y Preguntas Abiertas**, desglosamos la cadena de razonamiento de cada deducción:

### 🧩 Hipótesis 1: Aprovisionamiento Empírico y Desconexión de Mermas
- **Dimensión**: *Datos y Analítica (Nivel 1)*
- 📡 **Señal Observable (Dato Real)**:
  - Clientes reportan faltantes imprevistos de placas melamínicas de colores específicos en Google Reviews.
  - La empresa no cuenta con catálogo de stock en tiempo real en su sitio web.
  - El servicio de corte y presupuestación cierra estrictamente a las 15:30 hs (1 hora antes del local).
- 💡 **Supuesto de Consultoría**:
  - Las órdenes de compra a proveedores (Egger, Faplac, Durlock) se definen por intuición o planillas Excel aisladas. No existe un módulo de analítica que calcule mermas de placas ni demanda futura.
- 🧠 **Razón Razonable (Por qué es lógico)**:
  - En la industria maderera, una placa mide 2.75 m x 1.83 mimes 1.83	ext{ m}$. Cada pedido deja sobrantes (retazos). Para que esos retazos reingresen al stock de forma automática como subproductos vendibles, el optimizador de corte debe comunicarse con un ERP. Al no existir un ERP visible ni cotizador web, los retazos se acumulan físicamente o se descartan sin registro analítico.
- ❓ **Preguntas de Validación (Para entrevista o cátedra)**:
  - *¿Cómo calculan las compras mensuales a los fabricantes de placas?*
  - *¿Se registra en algún sistema el inventario de retazos y mermas del taller?*

---

### 🧩 Hipótesis 2: Doble Carga Manual y Maquinaria en Silo Operativo
- **Dimensión**: *Tecnología e Infraestructura (Nivel 2) / Procesos (Nivel 2)*
- 📡 **Señal Observable (Dato Real)**:
  - El cliente debe presentar el plano dibujado en papel en mostrador o enviar fotos por WhatsApp.
  - Reseñas de clientes describen demoras y colas significativas en el sector de presupuestos.
- 💡 **Supuesto de Consultoría**:
  - La maquinaria de corte computarizada opera como una isla tecnológica: el vendedor tipea la cotización comercial y, posteriormente, el operario del taller vuelve a cargar a mano las medidas en el software de corte (tipo Lepton Pack o OptiCut).
- 🧠 **Razón Razonable (Por qué es lógico)**:
  - Si el sistema comercial estuviese integrado al taller, el vendedor generaría el remito y el plano de corte viajaría por red directo a la seccionadora. La existencia de la restricción horaria (cerrar cotizaciones a las 15:30 hs) evidencia que el armado del mapa de corte es un cuello de botella manual que insume demasiado tiempo humano.
- ❓ **Preguntas de Validación**:
  - *¿El software de facturación está conectado a las máquinas de corte o el operario tipea las piezas manualmente en el taller?*

---

### 🧩 Hipótesis 3: Silos de Stock entre las 3 Sucursales Físicas
- **Dimensión**: *Procesos (Nivel 2) / Tecnología (Nivel 2)*
- 📡 **Señal Observable (Dato Real)**:
  - Cuentan con 3 locales en La Plata: Casa Central (Calle 39), Egger Haus (Calle 72) y City Bell (Centenario).
  - Clientes reportan que ante la falta de un producto debieron esperar a que llamaran por teléfono a otra sucursal para confirmar disponibilidad.
- 💡 **Supuesto de Consultoría**:
  - Cada sucursal opera con inventarios independientes en bases de datos locales o planillas desconectadas, requiriendo coordinación informal (teléfono / WhatsApp interno).
- 🧠 **Razón Razonable (Por qué es lógico)**:
  - Con un ERP multi-depósito moderno en la nube, cualquier vendedor ve en su pantalla el stock consolidado de las 3 sucursales al instante y reserva material sin hacer esperar al cliente ni llamar a otro local.
- ❓ **Preguntas de Validación**:
  - *¿Pueden consultar y reservar stock de City Bell desde Casa Central en tiempo real desde la misma pantalla?*

---

### 🧩 Hipótesis 4: Disparidad de Atención y Dependencia de Empleados Clave
- **Dimensión**: *Personas y Cultura (Nivel 2) / Cliente y Canales (Nivel 2)*
- 📡 **Señal Observable (Dato Real)**:
  - Puntuación general en Google: **3.9 / 5 ⭐ (casi 800 opiniones)**.
  - Comentarios polarizados: usuarios que felicitan con nombre y apellido a ciertos vendedores ("Romina", "Pato") por su predisposición, mientras otros se quejan de mala atención y lentitud.
- 💡 **Supuesto de Consultoría**:
  - No existen procesos estandarizados de atención comercial ni una herramienta CRM; la satisfacción del cliente depende exclusivamente de la pericia y disposición individual del empleado asignado.
- 🧠 **Razón Razonable (Por qué es lógico)**:
  - Cuando el conocimiento de las cuentas (ej. carpintero habitual que compra grandes volúmenes) reside en la memoria del vendedor y no en un CRM, si ese vendedor no está disponible, el cliente recibe una atención genérica y lenta.
- ❓ **Preguntas de Validación**:
  - *¿Llevan un registro digital del historial de compras y preferencias de cada cliente profesional?*

---

## 📊 2. Diagnóstico de Madurez Digital (6 Dimensiones)

| Dimensión | Nivel (1 a 5) | Justificación Basada en Señales y Razones |
| :--- | :---: | :--- |
| **1. Estrategia Digital** | **Nivel 2** *(En desarrollo)* | Redes activas con buen contenido de diseño, pero lo digital se concibe como vidriera y no como canal transaccional integrado. |
| **2. Tecnología e Infraestructura** | **Nivel 2** *(En desarrollo)* | Maquinaria de corte computarizada de alta precisión, pero operando como isla desconectada de la facturación y el stock. |
| **3. Datos y Analítica** | **Nivel 1** *(Inicial)* | Sin repositorio centralizado. Decisiones de abastecimiento basadas en intuición y planillas locales. Sin BI de mermas. |
| **4. Procesos de Negocio** | **Nivel 2** *(En desarrollo)* | Pasos manuales con retrabajos: doble carga de medidas en mostrador y taller, y consultas telefónicas entre locales. |
| **5. Personas y Cultura** | **Nivel 2** *(En desarrollo)* | Dependencia de empleados clave. Disparidad en calidad de atención y resistencia a cotizar fuera de ventanilla. |
| **6. Cliente y Canales** | **Nivel 2** *(En desarrollo)* | WhatsApp utilizado como buzón manual saturado. Sin cotizador de autoservicio online 24/7 ni tracking de pedidos. |

---

## ⚖️ 3. Matriz FODA Estratégica

```
╔══════════════════════════════════════════════╦══════════════════════════════════════════════╗
║ FORTALEZAS (Internas)                        ║ DEBILIDADES (Internas)                       ║
╠══════════════════════════════════════════════╬══════════════════════════════════════════════╣
║ • Marca líder y tradicional en La Plata.    ║ • Cierre de presupuestos 1h antes del local. ║
║ • Maquinaria propia de corte y canteado.     ║ • Doble carga manual mostrador ➔ taller.     ║
║ • Distribuidor oficial de Egger y Faplac.    ║ • Silos de stock entre las 3 sucursales.     ║
║ • 3 sucursales (Centro, Sur y City Bell).    ║ • Falta de cotizador web de autoservicio.    ║
╠══════════════════════════════════════════════╬══════════════════════════════════════════════╣
║ OPORTUNIDADES (Externas)                     ║ AMENAZAS (Externas)                          ║
╠══════════════════════════════════════════════╬══════════════════════════════════════════════╣
║ • Cotizador de cortes online con IA 24/7.    ║ • Competidores con cotización inmediata.     ║
║ • Portal B2B y CRM para carpinteros.         ║ • Volatilidad de precios en placas.          ║
║ • BI para reducir desperdicio de mermas.     ║ • Fuga de clientes por demoras en mostrador. ║
╚══════════════════════════════════════════════╩══════════════════════════════════════════════╝
```

---

## 🔄 4. Mapeo del Proceso Crítico Actual (AS-IS) & SIPOC

### Cuadro SIPOC
- **Suppliers (Proveedores)**: Fabricantes de placas (Egger, Faplac, Durlock) y Clientes (envían especificaciones de corte).
- **Inputs (Entradas)**: Lista de despiece (alto, ancho, textura, veta, lados a cantear).
- **Process (Proceso)**: Atención mostrador &rarr; Cotización manual &rarr; Carga en optimizador &rarr; Corte &rarr; Despacho.
- **Outputs (Salidas)**: Placas seccionadas, piezas canteadas, remito y factura.
- **Customers (Clientes)**: Carpinteros, arquitectos y clientes particulares.

### Flujograma y Puntos de Dolor AS-IS
1. **Recepción**: Cliente entrega plano en papel o envía foto a WhatsApp. *[Dolor: Límite horario 15:30 hs y colas]*.
2. **Verificación de Stock**: Vendedor revisa sistema local o llama por teléfono a otra sucursal. *[Dolor: Silos y demoras]*.
3. **Carga en Optimizador**: Operario tipea manualmente medidas en el software de taller. *[Dolor: Doble carga y error humano]*.
4. **Corte y Canteado**: Máquina secciona placas. *[Dolor: Mermas sobrantes no se registran en sistema]*.
5. **Entrega**: Aviso informal al cliente. *[Dolor: Falta de trazabilidad y tracking online]*.

---

## 💡 5. Hilo Conductor para los Siguientes Bloques del TPI
- **Bloque 2 (Transaccionales)**: ERP Cloud multi-sucursal + CRM para profesionales B2B + BI de mermas y demanda.
- **Bloque 3 (IA & Tendencias)**: Cotizador online 24/7 con optimizador en la nube + Bot transaccional en WhatsApp.
- **Bloque 4 (Business Case)**: Justificación de ROI por reducción del 15% de mermas y ahorro del 70% de tiempo en mostrador.

---
[[Tecnologías para la Gestión|⬅ Volver al Panel de la Materia]] | [[TPI - Trabajo Práctico Integrador|Ver Guía General TPI]]
