import pandas as pd
import json

# Leer los datos
df = pd.read_csv('taquerias_tlalpan_2025-08-06_googleplaces_con_sentimiento_seguro.csv')

# Mostrar estadísticas básicas
print("=== ANÁLISIS DE TAQUERÍAS DE LA CIUDAD DE MÉXICO ===")
print(f"Total de taquerías analizadas: {len(df)}")
print(f"Calificación promedio: {df['Calificación'].mean():.2f}")
print(f"Total de reseñas: {df['Total de Reseñas'].sum():,.0f}")

# Mostrar las mejores taquerías
print("\n=== TOP 5 TAQUERÍAS POR CALIFICACIÓN ===")
top_taquerias = df.nlargest(5, 'Calificación')[['Nombre', 'Calificación', 'Total de Reseñas']]
for i, (_, row) in enumerate(top_taquerias.iterrows(), 1):
    print(f"{i}. {row['Nombre']} - {row['Calificación']}⭐ ({row['Total de Reseñas']} reseñas)")

# Mostrar tipos de tacos más mencionados
print("\n=== TIPOS DE TACOS MÁS MENCIONADOS ===")
comentarios = df['Comentarios'].str.lower().str.cat(sep=' ')
tipos_tacos = {
    'pastor': comentarios.count('pastor'),
    'suadero': comentarios.count('suadero'),
    'cabeza': comentarios.count('cabeza'),
    'lengua': comentarios.count('lengua'),
    'tripa': comentarios.count('tripa'),
    'barbacoa': comentarios.count('barbacoa') + comentarios.count('birria'),
    'carnitas': comentarios.count('carnitas')
}

for tipo, count in sorted(tipos_tacos.items(), key=lambda x: x[1], reverse=True):
    if count > 0:
        print(f"- {tipo.capitalize()}: {count} menciones")

print("\n=== DASHBOARD LISTO ===")
print("Abre el archivo 'dashboard_taquerias.html' en tu navegador para ver el análisis completo.") 