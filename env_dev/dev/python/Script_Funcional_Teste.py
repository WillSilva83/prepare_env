#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pyspark.sql import SparkSession  # type: ignore


# In[3]:


def main():
    spark = (
        SparkSession.builder
        .appName("Teste do Pyspark") 
        .getOrCreate() 
    )

    # Criar um DataFrame com alguns dados de exemplo
    data = [("Alice", 34), ("Bob", 45), ("Catherine", 29)]
    columns = ["Name", "Age"]
    df = spark.createDataFrame(data, columns)

    # Mostrar os dados do DataFrame
    df.show()

    # Realizar uma operação simples: filtrar pessoas com idade acima de 30 anos
    df_filtered = df.filter(df.Age > 30)
    df_filtered.show()

    # Parar a sessão Spark
    spark.stop()

if __name__ == "__main__":
    main()

