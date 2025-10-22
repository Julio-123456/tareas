import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("whitegrid")
plt.rcParams['font.size'] = 10
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['font.family'] = 'DejaVu Sans'

datos = {
    'Producto': ['Televisor', 'Celular', 'Laptop', 'Tablet', 'Audifonos'],
    'Ventas': [150, 200, 250, 300, 100],
    'Precio': [750, 650, 900, 400, 120]
}

df = pd.DataFrame(datos)


df['Ingresos'] = df['Ventas'] * df['Precio']


html_tabla = df.to_html(index=False, classes='tabla-datos', border=0)
estadisticas = df.describe().to_html(classes='tabla-estadisticas', border=0)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))


colores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
bars1 = ax1.bar(df['Producto'], df['Ventas'], color=colores, edgecolor='white', linewidth=2)
ax1.set_title('Ventas por Producto', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Producto', fontsize=12, fontweight='bold')
ax1.set_ylabel('Cantidad de Ventas', fontsize=12, fontweight='bold')
ax1.set_ylim(0, max(df['Ventas']) * 1.2)
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')


for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontweight='bold', fontsize=11)


bars2 = ax2.bar(df['Producto'], df['Ingresos']/1000, color=colores, edgecolor='white', linewidth=2)
ax2.set_title('Ingresos por Producto', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Producto', fontsize=12, fontweight='bold')
ax2.set_ylabel('Ingresos (Miles $)', fontsize=12, fontweight='bold')
ax2.set_ylim(0, max(df['Ingresos']/1000) * 1.2)
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')


for bar in bars2:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
             f'${int(height)}K',
             ha='center', va='bottom', fontweight='bold', fontsize=11)

plt.tight_layout()
plt.savefig("grafica_ventas.png", dpi=300, bbox_inches='tight')
plt.close()


css_content = """
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding: 20px;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    background: white;
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    overflow: hidden;
}

.header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 40px;
    text-align: center;
}

.header h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.header p {
    font-size: 1.2em;
    opacity: 0.9;
}

.content {
    padding: 40px;
}

.seccion {
    margin-bottom: 50px;
    animation: fadeIn 0.8s ease-in;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

h2 {
    color: #667eea;
    font-size: 1.8em;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 3px solid #667eea;
    display: inline-block;
}

.tabla-datos, .tabla-estadisticas {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    background: white;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    border-radius: 10px;
    overflow: hidden;
}

.tabla-datos thead, .tabla-estadisticas thead {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.tabla-datos th, .tabla-estadisticas th {
    padding: 15px;
    text-align: left;
    font-weight: 600;
    font-size: 1.1em;
}

.tabla-datos td, .tabla-estadisticas td {
    padding: 12px 15px;
    border-bottom: 1px solid #f0f0f0;
}

.tabla-datos tbody tr:hover, .tabla-estadisticas tbody tr:hover {
    background-color: #f8f9ff;
    transition: background-color 0.3s ease;
}

.tabla-datos tbody tr:last-child td, .tabla-estadisticas tbody tr:last-child td {
    border-bottom: none;
}

.grafica-container {
    text-align: center;
    margin-top: 30px;
    padding: 20px;
    background: #f8f9ff;
    border-radius: 15px;
}

.grafica-container img {
    max-width: 100%;
    height: auto;
    border-radius: 10px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.resumen {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-top: 30px;
}

.tarjeta {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    transition: transform 0.3s ease;
}

.tarjeta:hover {
    transform: translateY(-5px);
}

.tarjeta h3 {
    font-size: 0.9em;
    margin-bottom: 10px;
    opacity: 0.9;
}

.tarjeta p {
    font-size: 2em;
    font-weight: bold;
}

.footer {
    background: #f8f9ff;
    padding: 20px;
    text-align: center;
    color: #666;
    border-top: 2px solid #e0e0e0;
}

@media (max-width: 768px) {
    .header h1 {
        font-size: 1.8em;
    }
    
    .content {
        padding: 20px;
    }
    
    .tabla-datos, .tabla-estadisticas {
        font-size: 0.9em;
    }
}
"""


html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Análisis de Ventas - Dashboard</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Dashboard de Ventas</h1>
            <p>Análisis Completo de Productos y Rendimiento</p>
        </div>
        
        <div class="content">
            <div class="seccion">
                <h2>📈 Resumen Ejecutivo</h2>
                <div class="resumen">
                    <div class="tarjeta">
                        <h3>Total Productos</h3>
                        <p>{len(df)}</p>
                    </div>
                    <div class="tarjeta">
                        <h3>Ventas Totales</h3>
                        <p>{df['Ventas'].sum()}</p>
                    </div>
                    <div class="tarjeta">
                        <h3>Ingresos Totales</h3>
                        <p>${df['Ingresos'].sum():,.0f}</p>
                    </div>
                    <div class="tarjeta">
                        <h3>Promedio Ventas</h3>
                        <p>{df['Ventas'].mean():.0f}</p>
                    </div>
                </div>
            </div>
            
            <div class="seccion">
                <h2>📋 Tabla de Datos Completa</h2>
                {html_tabla}
            </div>
            
            <div class="seccion">
                <h2>📊 Visualización de Datos</h2>
                <div class="grafica-container">
                    <img src="grafica_ventas.png" alt="Gráficas de Ventas e Ingresos">
                </div>
            </div>
            
            <div class="seccion">
                <h2>📐 Estadísticas Descriptivas</h2>
                {estadisticas}
            </div>
        </div>
        
        <div class="footer">
            <p>© 2024 - Análisis de Ventas | Generado con Python & Pandas</p>
        </div>
    </div>
</body>
</html>
"""


with open("tabla.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("estilos.css", "w", encoding="utf-8") as f:
    f.write(css_content)

print("✅ Archivos creados exitosamente:")
print("   - tabla.html")
print("   - estilos.css")
print("   - grafica_ventas.png")
print("\n🎨 Mejoras implementadas:")
print("   ✓ Gráficas duales con colores vibrantes")
print("   ✓ Diseño moderno con gradientes")
print("   ✓ Tarjetas de resumen ejecutivo")
print("   ✓ Animaciones y efectos hover")
print("   ✓ Responsive design")
print("   ✓ Valores sobre las barras")
print("   ✓ Mayor resolución en gráficas (300 DPI)")