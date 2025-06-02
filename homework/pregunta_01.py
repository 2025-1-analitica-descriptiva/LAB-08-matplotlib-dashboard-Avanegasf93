# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """

 # Crea la carpeta 'docs' si no existe
    os.makedirs("docs", exist_ok=True)

    # Carga los datos desde la carpeta files/input
    df = pd.read_csv("files/input/shipping-data.csv")

    # ================================
    # Gráfico 1: Envíos por bloque de almacén
    # ================================
    fig, ax = plt.subplots()
    df['Warehouse_block'].value_counts().plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title('Shipping per Warehouse Block')
    ax.set_xlabel('Warehouse Block')
    ax.set_ylabel('Number of Shipments')
    fig.tight_layout()
    fig.savefig('docs/shipping_per_warehouse.png')
    plt.close(fig)

    # ================================
    # Gráfico 2: Envíos por modo de envío
    # ================================
    fig, ax = plt.subplots()
    df['Mode_of_Shipment'].value_counts().plot(kind='bar', ax=ax, color='orange')
    ax.set_title('Mode of Shipment')
    ax.set_xlabel('Shipment Mode')
    ax.set_ylabel('Number of Shipments')
    fig.tight_layout()
    fig.savefig('docs/mode_of_shipment.png')
    plt.close(fig)

    # ================================
    # Gráfico 3: Distribución de calificaciones del cliente
    # ================================
    fig, ax = plt.subplots()
    df['Customer_rating'].value_counts().sort_index().plot(kind='bar', ax=ax, color='green')
    ax.set_title('Customer Ratings Distribution')
    ax.set_xlabel('Rating')
    ax.set_ylabel('Count')
    fig.tight_layout()
    fig.savefig('docs/average_customer_rating.png')
    plt.close(fig)

    # ================================
    # Gráfico 4: Distribución del peso en gramos
    # ================================
    fig, ax = plt.subplots()
    df['Weight_in_gms'].plot(kind='hist', bins=20, ax=ax, color='purple', edgecolor='black')
    ax.set_title('Weight Distribution')
    ax.set_xlabel('Weight (gms)')
    ax.set_ylabel('Frequency')
    fig.tight_layout()
    fig.savefig('docs/weight_distribution.png')
    plt.close(fig)

    # ================================
    # Creación del dashboard HTML
    # ================================
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Shipping Dashboard</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; background-color: #f9f9f9; }
                h1 { color: #333; }
                img { width: 600px; margin: 20px auto; display: block; border: 1px solid #ddd; padding: 10px; background: white; }
                .section { margin-bottom: 40px; }
            </style>
        </head>
        <body>
            <h1>Shipping Dashboard</h1>
            <div class="section">
                <h2>Shipping per Warehouse Block</h2>
                <img src="shipping_per_warehouse.png" alt="Shipping per Warehouse Block">
            </div>
            <div class="section">
                <h2>Mode of Shipment</h2>
                <img src="mode_of_shipment.png" alt="Mode of Shipment">
            </div>
            <div class="section">
                <h2>Customer Ratings</h2>
                <img src="average_customer_rating.png" alt="Customer Ratings">
            </div>
            <div class="section">
                <h2>Weight Distribution</h2>
                <img src="weight_distribution.png" alt="Weight Distribution">
            </div>
        </body>
        </html>
        """)