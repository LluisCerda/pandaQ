from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor
import streamlit as st
import pandas as pd

dataPath = 'data/'

class EvalVisitor(lcVisitor):
    def __init__(self):
        self.selected_table = None

    # Override the visitSql_query method
    def visitSql_query(self, ctx):
        # Extract table name from the context
        table_name = ctx.ID().getText()

        data_frame = pd.read_csv(dataPath + table_name + ".csv")
        self.selected_table = data_frame
        
        return self.selected_table

def execute_query(query):
    
    lexer = lcLexer(query)
    token_stream = CommonTokenStream(lexer)
    parser = lcParser(token_stream)
    tree = parser.sql_query()

    eval_visitor = EvalVisitor()

    result = eval_visitor.visit(tree)

    return result

def main():
    st.title("PandaQ")

    # Agregar una entrada de texto para la consulta
    query_input = st.text_area("Ingrese su consulta SQL:", height=100)

    # Agregar un botón para enviar la consulta
    if st.button("Enviar Consulta"):
        # Verificar si la consulta no está vacía
        if query_input.strip():
            # Ejecutar la consulta y obtener los resultados
            result_df = execute_query(query_input)
            # Mostrar los resultados en una tabla
            st.write("Resultados de la Consulta:")
            st.dataframe(result_df)
        else:
            st.warning("Por favor, ingrese una consulta antes de enviar.")

if __name__ == "__main__":
    main()