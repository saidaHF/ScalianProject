# Scalian Project

*Exercise:*

Tenemos dos ficheros uno de **movimientos**(flujos de operaciones)  y otro de **aggregaciones**. La cabecera marca el nombre de los campos.
En este de aggregaciones se supone que se están agregando (sumando) los flujos en función de unos ejes

Los ejes vienen dados por los campos "entity", "internal", "product", "currency","bs","desk","portfolio","account","counterpart","typology","isin","statusLiq","maturity","source_process","target"

Las cantidades que se suman son amountSent  de movimientos en dTotal de aggregaciones. amountSettled de momvientos en settledTotal de agregaciones.

**Se trata de realizar lo siguiente:**

Programa que tenga capacidad de filtrar por los campos entity y currency (filtro de entity obligatorio)

* Que deje en un fichero (nombre distinto por ejecución) todos los registros de movimientos que tengan status diferente de expected.
* Que deje en un fichero (nombre distinto por ejecución) todos los registros de aggregaciones todos los registros que tengan el campo isTotalCash  a true y statusLiq distintos de expected.


Ingestar los archivos tras el filtro y los registros que hemos deshechado (y que hemos enviado a ficheros a parte). Filtrados y deshechados no entran en la tabla ok?
Por ingestar se entiende que los dejemos en una bbdd a tu elección.

Dejar en un archivo de fallidos los registros que por el motivo que sea no hemos podido ingestar. Es decir, que nos han fallado en el proceso.
El archivo puede tener el siguiente formato por ejemplo:  id de ejecución;nombre archivo original;key del archivo original;.....


Generar una nueva tabla que emule lo que se supone que se ha realizado en aggregaciones. Me explico, como supuestamente el que nos ha dado los ficheros ha generado el fichero de aggregaciones en
función del de movimientos, se trata de crear una nueva tabla de aggregaciones realizando las agregaciones por los ejes.
Finalmente deberemos sacar en ficheros lo siguiente:
             -  Las agregaciones que cuadran entre lo que nos han enviado y lo que hemos obtenido.
			 -  Las agregaciones que nos descuadran por valor.
			 -  Aquellas agregaciones que nos han aparecido a nosotros pero no estaban en la original.
			 -  Aquellas aggregaciones que estaban en la original pero no nos han aparecido a nosotros.

> Nota: Como agregaciones originales tomamos las que finalmente hemos ingestado tras filtro y sin tener en cuenta los registros deshechados por statusLiq e isTotalCash

**Necesario:** Tener un script con los creates de las tablas que se vayan a utilizar. Es lo primero que valoraré.

> **Esto son extras por si se anda sobrado:**
>
> * Se valorará que las tablas guarden la info de distintas ejecuciones.
> * Se valorará que haya logs a diferentes niveles, info, warning, error
> * Se valorará la dockerización del proyecto.
> * Se valorará algún tipo de servicio rest para la consulta de las tablas generadas.
> * Se valorará algún tipo de front-end, bien para la ejecución del proceso con los filtros, bien para la visualización de datos ingestados (iniciales y finales).
> * Se valorarán más capacidades de filtrado.