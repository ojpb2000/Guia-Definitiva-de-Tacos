# 🌮 Guía Definitiva de Tacos - Ciudad de México

## 📊 Análisis de Taquerías de la CDMX

Este proyecto presenta un análisis completo de las mejores taquerías de la Ciudad de México basado en datos reales de Google Maps, con un dashboard interactivo que muestra los insights más relevantes sobre los tacos más populares.

## 🎯 Objetivo

Identificar y analizar los mejores tacos de la Ciudad de México, organizados por tipo, rankings y características especiales, para crear una guía definitiva que ayude a los amantes de los tacos a encontrar las mejores opciones.

## 📁 Archivos del Proyecto

- `taquerias_tlalpan_2025-08-06_googleplaces_con_sentimiento_seguro.csv` - Datos originales de las taquerías
- `analisis_taquerias.py` - Script de Python para procesar y analizar los datos
- `analisis_taquerias.json` - Resultados del análisis en formato JSON
- `dashboard_taquerias.html` - Dashboard interactivo con visualización de resultados
- `README.md` - Documentación del proyecto

## 🔍 Tipos de Tacos Analizados

El análisis incluye los siguientes tipos de tacos:

- **Pastor** - El clásico taco al pastor
- **Suadero** - Tacos de suadero tradicionales
- **Cabeza** - Tacos de cabeza de res
- **Lengua** - Tacos de lengua de res
- **Tripa** - Tacos de tripa
- **Barbacoa/Birria** - Tacos de barbacoa y birria
- **Carnitas** - Tacos de carnitas
- **Bistec** - Tacos de bistec
- **Longaniza** - Tacos de longaniza
- **Campechano** - Tacos campechanos
- **Costilla** - Tacos de costilla
- **Arrachera** - Tacos de arrachera
- **Pescado** - Tacos de pescado y mariscos
- **Mixiote** - Tacos de mixiote
- **Sesos** - Tacos de sesos
- **Maciza** - Tacos de maciza
- **Surtido** - Tacos surtidos

## 📈 Métricas Analizadas

### Estadísticas Generales
- Total de taquerías analizadas
- Calificación promedio
- Sentimiento promedio de las reseñas
- Total de reseñas

### Análisis por Tipo de Taco
- Cantidad de taquerías que ofrecen cada tipo
- Calificación promedio por tipo
- Sentimiento promedio por tipo
- Porcentaje de comentarios positivos
- Mejores taquerías por tipo

### Rankings
- **Por Calificación** - Top 10 taquerías con mejor calificación
- **Por Sentimiento** - Top 10 taquerías con mejor sentimiento en reseñas
- **Por Popularidad** - Top 10 taquerías con más reseñas

### Características Especiales
- Tortillas hechas a mano
- Salsas caseras
- Horarios nocturnos
- Servicio a domicilio
- Estacionamiento disponible
- Ambiente familiar

### Análisis de Precios
- Precio promedio por taco
- Precio mediano
- Rango de precios (mínimo y máximo)

## 🚀 Cómo Usar

### 1. Ejecutar el Análisis
```bash
python analisis_taquerias.py
```

### 2. Ver el Dashboard
Abre el archivo `dashboard_taquerias.html` en tu navegador web.

## 📊 Resultados Destacados

### Los Tacos Más Populares
1. **Pastor** - El rey de los tacos, presente en la mayoría de taquerías
2. **Suadero** - Segundo en popularidad
3. **Cabeza** - Muy apreciado por los conocedores
4. **Lengua** - Especialidad gourmet
5. **Tripa** - Para los más aventureros

### Insights Clave
- Los tacos de **pastor** tienen la mayor cantidad de taquerías especializadas
- Los tacos de **lengua** suelen tener las calificaciones más altas
- Las taquerías con **tortillas hechas a mano** reciben mejores calificaciones
- El **servicio a domicilio** es cada vez más común
- Los **horarios nocturnos** son muy valorados por los clientes

## 🎨 Características del Dashboard

- **Diseño Responsivo** - Se adapta a diferentes tamaños de pantalla
- **Visualización Interactiva** - Datos dinámicos cargados desde JSON
- **Enlaces Directos** - Acceso directo a Google Maps de cada taquería
- **Diseño Moderno** - Interfaz atractiva con gradientes y animaciones
- **Información Completa** - Rankings, estadísticas e insights detallados

## 📋 Requisitos

- Python 3.7+
- pandas
- numpy
- Navegador web moderno

## 🔧 Instalación de Dependencias

```bash
pip install pandas numpy
```

## 📝 Notas Técnicas

- Los datos fueron obtenidos de Google Maps al 6 de agosto de 2025
- El análisis de sentimiento se realizó sobre las reseñas de los clientes
- Se filtraron taquerías con al menos 10 reseñas para rankings más confiables
- Los precios se extrajeron de menciones en los comentarios

## 🌟 Características Especiales

- **Análisis de Sentimiento** - Evaluación automática del tono de las reseñas
- **Extracción de Tipos de Tacos** - Identificación automática de especialidades
- **Rankings Múltiples** - Diferentes criterios de evaluación
- **Enlaces Directos** - Acceso inmediato a Google Maps
- **Diseño de Revista** - Presentación profesional y atractiva

## 📞 Contacto

Para preguntas o sugerencias sobre este análisis, puedes contactar a través de los datos del proyecto.

---

**🌮 ¡Disfruta explorando los mejores tacos de la Ciudad de México!** 