---
materia: "[[Tecnologías para la Gestión]]"
tipo: Anexo de Auditoría
fase: Entregable 4 / Unidad 3 (Teoría)
empresa: "El Emporio del Terciado S.A."
consultora: "ADN Consultora · Grupo 3"
autor: "Agustín Barthe"
catedra: "Prof. Diego Erben"
fecha: "2026-09-29"
estado: Completo
tags:
  - tpi
  - erp
  - precios-mercado
  - auditoria
  - transparencia-comercial
  - argentina
---

# 🔍 Auditoría de Precios y Transparencia Comercial de ERPs en Argentina

> **ADN Consultora · Grupo 3 · Tecnologías para la Gestión · UNLP 2026**  
> *Relevamiento de fuentes primarias, políticas de publicación y estructura real de costos (Septiembre 2026).*

---

## 1. Resumen Ejecutivo: Transparencia vs. Opacidad Comercial

Al auditar los canales oficiales de los 5 ERPs evaluados para **El Emporio del Terciado S.A.**, se evidencia una brecha estructural en el mercado de software de gestión en Argentina:

| Solución ERP | ¿Precios Públicos en Web? | Modelo Comercial | Canal de Venta | Nivel de Transparencia |
| :--- | :---: | :--- | :--- | :---: |
| **Odoo Enterprise** | **SÍ (100% público)** | SaaS / PaaS / On-Premise por usuario con **PPP regional** | Directo web o vía Partner oficial | 🟢 **Alta (Autoservicio)** |
| **Flexxus Enterprise** | **NO** | Abono mensual modular por usuarios concurrentes | Venta directa consultiva / Partners | 🟡 **Media (Opaca)** |
| **Finnegans Go** | **NO** (excepto consumo API) | Suscripción SaaS por usuario nominal (tiers) | Venta directa / Partners (Morgana Tec, etc.) | 🟡 **Media (Opaca)** |
| **Tango Gestión / Nube** | **NO** (precios vía canal) | Abono en ARS por puestos + hosting Claro Cloud | Red exclusiva de Centros Certificados | 🟡 **Media (Canal cerrado)** |
| **SAP Business One** | **NO** (prohibido por SAP) | Licencia perpetua o SaaS Cloud | Partners Platinum/Gold (Seidor, Exxis, etc.) | 🔴 **Baja (Estricta reserva)** |

---

## 2. Desglose Detallado por Solución

### 1. Odoo Enterprise (v17 / v18)
* **URL Oficial de Precios:** `https://www.odoo.com/es/pricing`
* **Mecanismo:** Detección automática de geolocalización por IP y aplicación de **Paridad de Poder Adquisitivo (PPP)** para Argentina.
* **Valores Reales Verificados (Argentina PPP):**
  * **Plan Estándar:** **USD 7.25** / usuario / mes (promoción anual) — **USD 8.95** (tarifa lista sin promo).
  * **Plan Personalizado:** **USD 13.40** / usuario / mes (promoción anual) — **USD 16.40** (tarifa lista sin promo).  
    *Incluye:* Odoo.sh, On-Premise, Multiempresa, API externa, Odoo Studio y **Agentic AI**.
* **Precios Globales de Referencia (sin PPP / IP EE.UU. o Europa):**
  * Estándar: USD 19.90 (promo) / USD 24.90 (lista).
  * Personalizado: USD 29.90 (promo) / USD 37.40 (lista).
* **Infraestructura Cloud (Odoo.sh):**
  * Worker: **USD 57.60** / worker / mes (anual). Un worker soporta ~20-25 usuarios concurrentes.
  * Almacenamiento: **USD 0.20** / GB / mes.
  * Entorno Staging: **USD 14.40** / mes.
* **Facturación:** Directa a Odoo S.A. en USD con tarjeta corporativa, o en **ARS (Factura A al tipo de cambio oficial BNA)** mediante partners argentinos (Adhoc, Birtum, Quilsoft).

---

### 2. Flexxus Enterprise
* **URL Oficial:** `https://flexxus.com.ar`
* **Estado de la Web:** No publica precios para la línea *Enterprise*. La URL `/precios` redirige a contenidos formativos de capacitación interna ("Precios por Proveedor") y `/planes` retorna error HTTP 404.
* **Modelo Comercial:** Cotización personalizada en base a un núcleo administrativo más de 25 módulos activables (Producción, POS, eCommerce, API, SabIA).
* **Valores de Mercado Relevados:**
  * Planes iniciales SaaS PyME (*Flexxus Order*): Entre **$43.699 ARS** y **$57.621 ARS + IVA** por usuario/mes.
  * *Flexxus Enterprise* (20-25 puestos concurrentes con Producción y API Server): Entre **USD 1.200 y USD 2.200 / mes** (aproximadamente **$1.500.000 a $2.800.000 ARS + IVA / mes**).
  * Implementación (120-200 horas): **USD 4.000 a USD 9.000**.
* **Fuentes de Contraste:** Propuestas comerciales testigo, ComparaSoftware Argentina, Wynges y red de distribuidores (Sistemas Nimbus).

---

### 3. Finnegans Go
* **URL Oficial:** `https://finneg.com`
* **Estado de la Web:** No publica tarifas para licencias de ERP. La URL `/precios` retorna HTTP 404.
* **Modelo Comercial:** Suscripción mensual en base a **usuarios nominales** clasificados en tres niveles (Full, Limitado y Consulta).
* **Valores de Mercado Relevados:**
  * Usuario Full: **USD 35 a USD 65** / usuario / mes.
  * Usuario Limitado: **USD 15 a USD 25** / usuario / mes.
  * Usuario Consulta: **USD 10 a USD 15** / usuario / mes.
  * Estimación para El Emporio (mix de 8 Full + 8 Limitados + 4 Consulta): **USD 450 a USD 780 / mes** (+ IVA).
  * Paquete de entrada (*DAI Start*): **USD 0 de costo de implementación** incluyendo 5 usuarios Full.
  * Implementación guiada (*DAI Full*): **USD 3.000 a USD 8.000**.
* **Precios Públicos Oficiales:**
  * Consumo de APIs (`bc.finneg.com`): **USD 0,00375** por llamada excedente a partir de las 100.000 llamadas mensuales.
* **Fuentes de Contraste:** Base de Conocimiento oficial (`bc.finneg.com`), CPCECABA, EvaluandoERP y partners (Morgana Tec).

---

### 4. Tango Gestión / Tango Nube (Axoft)
* **URL Oficial:** `https://axoft.com` y `https://tangonube.com`
* **Estado de la Web:** Axoft no publica listas de precios abiertas; delega la cotización y facturación en su canal de distribución oficial.
* **Modelo Comercial:** Facturación 100% en Pesos Argentinos (ARS). La modalidad nube consiste en una alianza de hosting con **Claro Cloud** (máquinas virtuales Windows Server con acceso RDP).
* **Valores de Mercado Relevados:**
  * Tango Nube Plan Básico (2 puestos concurrentes): **$594.000 a $731.000 ARS + IVA / mes**.
  * Tango Nube Plan Pro (5 puestos concurrentes): **$912.000 ARS + IVA / mes**.
  * Puesto concurrente adicional: Aprox. **$60.000 ARS + IVA / mes**.
  * Estimación para El Emporio (15-20 puestos): **$1.500.000 a $1.900.000 ARS + IVA / mes**.
  * Módulo Punto de Venta: Se licencia por separado (adicional por caja/sucursal).
* **Fuentes de Contraste:** Centros de Servicios Certificados (Lear System, Grupo Tesys), Spom Solutions y Wynges.

---

### 5. SAP Business One
* **URL Oficial:** `https://www.sap.com/latinamerica/products/erp/business-one.html`
* **Estado de la Web:** Por directiva global de SAP, está terminantemente prohibido publicar precios de lista abiertos al consumidor final.
* **Modelo Comercial:** Venta exclusiva mediante partners certificados Platinum y Gold (Seidor Argentina, Exxis Group, One Solutions).
* **Valores de Mercado Relevados (Pricelist Oficial SAP LATAM):**
  * Licencia Perpetua Professional User: **USD 2.700 a USD 3.500** por usuario (pago único) + 18% a 22% de mantenimiento anual obligatorio.
  * Licencia Perpetua Limited User (Logistics/Financial/CRM): **USD 1.400 a USD 1.850** por usuario.
  * Suscripción Cloud (SaaS en nube privada del partner): **USD 100 a USD 150** / usuario / mes (Professional) y **USD 45 a USD 75** (Limited).
  * Tarifa de consultoría partner: **USD 60 a USD 120 / hora**.
  * Presupuesto Año 1 para 20-25 usuarios con retail: **USD 55.000 a USD 85.000** (Cloud) o **USD 80.000 a USD 120.000** (On-Premise).
* **Fuentes de Contraste:** Tarifarios de partners oficiales, Seidor Argentina y relevamientos de EvaluandoERP.

---

## 3. Conclusiones y Criterio de Selección para el TP

1. **Previsibilidad Financiera:** Odoo permite proyectar el presupuesto de licenciamiento e infraestructura con certeza matemática directa desde la web oficial, eliminando el riesgo de sobreprecios o variaciones discrecionales del canal comercial.
2. **Impacto del Beneficio PPP:** La aplicación de paridad de poder adquisitivo sitúa a Odoo Enterprise Personalizado en **USD 13.40/mes**, convirtiéndolo en la opción más competitiva en costo recurrente entre las soluciones internacionales de clase mundial.
3. **Costo Oculto de la Opacidad:** En soluciones como Flexxus o Finnegans, los presupuestos finales dependen de la habilidad de negociación, los módulos seleccionados y los paquetes de consultoría, lo que exige fijar alcances estrictos en los contratos de servicio (*SLA*).
