import pandas as pd
import numpy as np
import re
from collections import Counter
import json

# Leer los datos
df = pd.read_csv('taquerias_tlalpan_2025-08-06_googleplaces_con_sentimiento_seguro.csv')

# Limpiar y procesar los datos
def limpiar_datos(df):
    # Convertir calificaciones a numérico
    df['Calificación'] = pd.to_numeric(df['Calificación'], errors='coerce')
    df['Total de Reseñas'] = pd.to_numeric(df['Total de Reseñas'], errors='coerce')
    
    # Limpiar columnas de sentimiento
    df['Porcentaje_Positivos'] = pd.to_numeric(df['Porcentaje_Positivos'], errors='coerce')
    df['Porcentaje_Negativos'] = pd.to_numeric(df['Porcentaje_Negativos'], errors='coerce')
    df['Score_Sentimiento_Promedio'] = pd.to_numeric(df['Score_Sentimiento_Promedio'], errors='coerce')
    
    return df

df = limpiar_datos(df)

# Análisis de tipos de tacos mencionados en comentarios
def extraer_tipos_tacos(comentarios):
    tipos_tacos = []
    if pd.isna(comentarios):
        return tipos_tacos
    
    comentarios_str = str(comentarios).lower()
    
    # Patrones para identificar tipos de tacos
    patrones = {
        'pastor': ['pastor', 'al pastor'],
        'suadero': ['suadero'],
        'cabeza': ['cabeza', 'de cabeza'],
        'lengua': ['lengua', 'de lengua'],
        'tripa': ['tripa', 'tripas'],
        'barbacoa': ['barbacoa', 'birria'],
        'carnitas': ['carnitas'],
        'bistec': ['bistec', 'bisteck'],
        'longaniza': ['longaniza'],
        'campechano': ['campechano'],
        'costilla': ['costilla'],
        'arrachera': ['arrachera'],
        'pescado': ['pescado', 'camarón', 'camarones'],
        'mixiote': ['mixiote'],
        'sesos': ['sesos'],
        'maciza': ['maciza'],
        'surtido': ['surtido']
    }
    
    for tipo, palabras in patrones.items():
        for palabra in palabras:
            if palabra in comentarios_str:
                tipos_tacos.append(tipo)
                break
    
    return tipos_tacos

# Aplicar extracción de tipos de tacos
df['Tipos_Tacos'] = df['Comentarios'].apply(extraer_tipos_tacos)

# Análisis de sentimiento por tipo de taco
def analizar_sentimiento_por_tipo():
    resultados = {}
    
    # Obtener todos los tipos de tacos únicos
    todos_tipos = []
    for tipos in df['Tipos_Tacos']:
        todos_tipos.extend(tipos)
    
    tipos_unicos = list(set(todos_tipos))
    
    for tipo in tipos_unicos:
        # Filtrar taquerías que mencionan este tipo de taco
        mask = df['Tipos_Tacos'].apply(lambda x: tipo in x)
        taquerias_tipo = df[mask]
        
        if len(taquerias_tipo) > 0:
            # Calcular total de reseñas por tipo
            total_resenas_tipo = taquerias_tipo['Total de Reseñas'].sum()
            
            # Calcular reseñas por sentimiento
            reseñas_positivas = (taquerias_tipo['Porcentaje_Positivos'] * taquerias_tipo['Total de Reseñas'] / 100).sum()
            reseñas_negativas = (taquerias_tipo['Porcentaje_Negativos'] * taquerias_tipo['Total de Reseñas'] / 100).sum()
            reseñas_neutras = total_resenas_tipo - reseñas_positivas - reseñas_negativas
            
            resultados[tipo] = {
                'cantidad_taquerias': len(taquerias_tipo),
                'calificacion_promedio': taquerias_tipo['Calificación'].mean(),
                'sentimiento_promedio': taquerias_tipo['Score_Sentimiento_Promedio'].mean(),
                'porcentaje_positivo': taquerias_tipo['Porcentaje_Positivos'].mean(),
                'total_resenas': total_resenas_tipo,
                'reseñas_positivas': int(reseñas_positivas),
                'reseñas_negativas': int(reseñas_negativas),
                'reseñas_neutras': int(reseñas_neutras),
                'mejores_taquerias': taquerias_tipo.nlargest(5, 'Calificación')[['Nombre', 'Calificación', 'URL de Google Maps']].to_dict('records')
            }
    
    return resultados

# Análisis de las mejores taquerías por calificación
def mejores_taquerias():
    # Filtrar taquerías con al menos 10 reseñas
    df_filtrado = df[df['Total de Reseñas'] >= 10].copy()
    
    # Top 10 por calificación
    top_calificacion = df_filtrado.nlargest(10, 'Calificación')[['Nombre', 'Calificación', 'Total de Reseñas', 'URL de Google Maps', 'Dirección']]
    
    # Top 10 por sentimiento
    top_sentimiento = df_filtrado.nlargest(10, 'Score_Sentimiento_Promedio')[['Nombre', 'Score_Sentimiento_Promedio', 'Total de Reseñas', 'URL de Google Maps', 'Dirección']]
    
    # Top 10 por cantidad de reseñas
    top_popularidad = df_filtrado.nlargest(10, 'Total de Reseñas')[['Nombre', 'Total de Reseñas', 'Calificación', 'URL de Google Maps', 'Dirección']]
    
    return {
        'por_calificacion': top_calificacion.to_dict('records'),
        'por_sentimiento': top_sentimiento.to_dict('records'),
        'por_popularidad': top_popularidad.to_dict('records')
    }

# Análisis de precios
def analizar_precios():
    # Extraer información de precios de los comentarios
    precios_mentions = []
    
    for comentarios in df['Comentarios']:
        if pd.notna(comentarios):
            # Buscar menciones de precios
            precios = re.findall(r'\$(\d+)', str(comentarios))
            precios_mentions.extend([int(p) for p in precios])
    
    if precios_mentions:
        return {
            'precio_promedio': np.mean(precios_mentions),
            'precio_mediano': np.median(precios_mentions),
            'precio_min': min(precios_mentions),
            'precio_max': max(precios_mentions),
            'distribucion_precios': Counter(precios_mentions)
        }
    return {}

# Análisis de características especiales
def analizar_caracteristicas():
    caracteristicas = {
        'tortillas_hechas_mano': 0,
        'salsas_caseras': 0,
        'horarios_nocturnos': 0,
        'servicio_domicilio': 0,
        'estacionamiento': 0,
        'ambiente_familiar': 0
    }
    
    for comentarios in df['Comentarios']:
        if pd.notna(comentarios):
            comentarios_str = str(comentarios).lower()
            
            if 'tortilla' in comentarios_str and ('mano' in comentarios_str or 'hecha' in comentarios_str):
                caracteristicas['tortillas_hechas_mano'] += 1
            
            if 'salsa' in comentarios_str and ('casera' in comentarios_str or 'rica' in comentarios_str):
                caracteristicas['salsas_caseras'] += 1
            
            if '24' in comentarios_str or 'madrugada' in comentarios_str or 'noche' in comentarios_str:
                caracteristicas['horarios_nocturnos'] += 1
            
            if 'domicilio' in comentarios_str or 'delivery' in comentarios_str:
                caracteristicas['servicio_domicilio'] += 1
            
            if 'estacionamiento' in comentarios_str:
                caracteristicas['estacionamiento'] += 1
            
            if 'familiar' in comentarios_str or 'familia' in comentarios_str:
                caracteristicas['ambiente_familiar'] += 1
    
    return caracteristicas

# Análisis visual para gráficos
def analisis_visual():
    # Datos para gráfico de barras apiladas
    datos_grafico = []
    
    tipos_tacos = analizar_sentimiento_por_tipo()
    
    for tipo, datos in tipos_tacos.items():
        datos_grafico.append({
            'tipo_taco': tipo.capitalize(),
            'total_resenas': datos['total_resenas'],
            'positivas': datos['reseñas_positivas'],
            'negativas': datos['reseñas_negativas'],
            'neutras': datos['reseñas_neutras'],
            'calificacion': datos['calificacion_promedio'],
            'cantidad_taquerias': datos['cantidad_taquerias']
        })
    
    # Ordenar por total de reseñas
    datos_grafico.sort(key=lambda x: x['total_resenas'], reverse=True)
    
    return {
        'datos_grafico': datos_grafico,
        'resumen_visual': {
            'total_tipos_analizados': len(datos_grafico),
            'tipo_mas_popular': datos_grafico[0]['tipo_taco'] if datos_grafico else 'N/A',
            'tipo_mejor_calificado': max(datos_grafico, key=lambda x: x['calificacion'])['tipo_taco'] if datos_grafico else 'N/A',
            'total_resenas_analizadas': sum(d['total_resenas'] for d in datos_grafico)
        }
    }

# Función para limpiar valores NaN en el JSON
def limpiar_json(obj):
    if isinstance(obj, dict):
        return {k: limpiar_json(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [limpiar_json(item) for item in obj]
    elif pd.isna(obj):
        return None
    else:
        return obj

# Generar análisis completo
def generar_analisis_completo():
    analisis = {
        'resumen_general': {
            'total_taquerias': len(df),
            'calificacion_promedio': df['Calificación'].mean(),
            'sentimiento_promedio': df['Score_Sentimiento_Promedio'].mean(),
            'total_resenas': df['Total de Reseñas'].sum()
        },
        'tipos_tacos': analizar_sentimiento_por_tipo(),
        'mejores_taquerias': mejores_taquerias(),
        'precios': analizar_precios(),
        'caracteristicas': analizar_caracteristicas(),
        'analisis_visual': analisis_visual(),
        'datos_completos': df.to_dict('records')
    }
    
    # Limpiar valores NaN antes de guardar
    analisis = limpiar_json(analisis)
    
    return analisis

# Ejecutar análisis
if __name__ == "__main__":
    analisis = generar_analisis_completo()
    
    # Guardar resultados en JSON
    with open('analisis_taquerias.json', 'w', encoding='utf-8') as f:
        json.dump(analisis, f, ensure_ascii=False, indent=2)
    
    print("Análisis completado y guardado en 'analisis_taquerias.json'")
    
    # Mostrar algunos resultados clave
    print(f"\nResumen General:")
    print(f"Total de taquerías analizadas: {analisis['resumen_general']['total_taquerias']}")
    print(f"Calificación promedio: {analisis['resumen_general']['calificacion_promedio']:.2f}")
    print(f"Sentimiento promedio: {analisis['resumen_general']['sentimiento_promedio']:.2f}")
    
    print(f"\nTipos de tacos más mencionados:")
    for tipo, datos in analisis['tipos_tacos'].items():
        print(f"- {tipo.capitalize()}: {datos['cantidad_taquerias']} taquerías, calificación: {datos['calificacion_promedio']:.2f}")
    
    print(f"\nAnálisis Visual:")
    print(f"Total de tipos analizados: {analisis['analisis_visual']['resumen_visual']['total_tipos_analizados']}")
    print(f"Tipo más popular: {analisis['analisis_visual']['resumen_visual']['tipo_mas_popular']}")
    print(f"Tipo mejor calificado: {analisis['analisis_visual']['resumen_visual']['tipo_mejor_calificado']}")
    print(f"Total de reseñas analizadas: {analisis['analisis_visual']['resumen_visual']['total_resenas_analizadas']:,}") 