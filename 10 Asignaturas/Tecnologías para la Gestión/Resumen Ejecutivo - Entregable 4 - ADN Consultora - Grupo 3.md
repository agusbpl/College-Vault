**RESUMEN EJECUTIVO — ENTREGABLE 4**

**El Emporio del Terciado S.A.**

*ADN Consultora · Grupo 3 · Tecnologías para la Gestión · UNLP 2026*

**CONTEXTO**

La propuesta parte de los dos procesos TO-BE ya definidos —venta presencial con servicio de corte a medida y consulta remota de precio, stock y presupuesto—. Se mantienen como recorridos distintos, pero comparten una misma fuente de datos. El criterio es implementar solo los módulos que sostienen esos procesos y reduzcan silos, recargas e inconsistencias.

**1\. MÓDULOS ERP PROPUESTOS**

| Módulo ERP | Prioridad | Aplicación en El Emporio | Integración |
| :---- | :---- | :---- | :---- |
| Ventas y Distribución | **CRÍTICA** | Pedido único, remitos/facturación y conversión de presupuesto aceptado sin recarga. | Stock · Taller · Finanzas |
| Logística y Almacenes | **CRÍTICA** | Stock común por sucursal/ubicación y reserva de material. | Ventas · Taller |
| Producción / Taller | **CRÍTICA** | Orden de trabajo vinculada al pedido y seguimiento de estados. | Ventas · Stock |
| Finanzas y Contabilidad | **ALTA** | Cobranzas, cuentas y registración contable a partir de la venta. | Ventas |
| Compras y Abastecimiento | **A VALIDAR** | Completa reposición; falta validar circuito de compras y proveedores. | Stock · Finanzas |
| Recursos Humanos | **NO PRIORIZADO** | Sin evidencia suficiente dentro del alcance actual. | — |

Nota: la atención omnicanal y la cotización/presupuestos siguen siendo capacidades necesarias de la arquitectura. Podrán estar incluidas en el ERP elegido o integrarse como soluciones complementarias; esto se definirá al evaluar el mercado.

**2\. PARÁMETROS Y DATOS MAESTROS**

| Parámetros a configurar | Datos maestros a migrar |
| :---- | :---- |
| Sucursales/depósitos y taller · unidades de medida · listas/condiciones comerciales · estados de pedido y orden de taller · reglas de reserva/liberación · usuarios, roles y permisos. | Productos/materiales y servicios de taller · precios/listas vigentes · clientes · stock inicial por ubicación · usuarios. Proveedores si Compras entra en primera etapa. |

**3\. USUARIOS Y BENEFICIOS**

| Rol | P/O/C | Beneficio concreto |
| :---- | :---- | :---- |
| Administración del sistema | **P** | Configura maestros, parámetros, usuarios y permisos; reglas homogéneas y control de accesos. |
| Ventas / atención | **O/C** | Registra consultas, presupuestos y pedidos; responde con la misma información y evita recargas. |
| Depósito / stock | **O/C** | Registra movimientos y reservas; comparte disponibilidad entre sucursales. |
| Taller | **O/C** | Recibe órdenes vinculadas al pedido y actualiza estados; mejora la trazabilidad. |
| Administración / finanzas | **O/C** | Factura, registra cobranzas y reutiliza datos originados en la venta. |
| Dirección / gerencia | **C** | Consulta ventas, stock, pedidos y trabajos pendientes para seguimiento y decisión. |

Adopción: prever capacitación, responsabilidades claras, depuración de datos y eliminación de registros paralelos que vuelvan a crear silos.

**4\. BENEFICIO CENTRAL**

Consulta/presupuesto → Pedido → Reserva de stock → Orden de taller → Facturación → Información para gestión.

El dato se captura una sola vez y se reutiliza durante todo el proceso. Así, una consulta aceptada puede convertirse en pedido sin recarga y ventas, sucursales, stock, taller y administración trabajan con información consistente y trazable.

**VALIDACIONES PENDIENTES**

Antes de una implementación real deben confirmarse: sistema actual, reglas de actualización/reserva de stock, circuito de compras, detalle de facturación/contabilidad, tratamiento de consumos y mermas del taller y responsables definitivos de cada rol.

