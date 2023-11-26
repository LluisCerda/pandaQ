from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor
import streamlit as st
import pandas as pd
from antlr4.tree import Trees

dataPath = 'data/'

class EvalVisitor(lcVisitor):
    
    def visitSelect(self, ctx):
        
        table_name = ctx.ID().getText()

        if ctx.getChild(1).getText() == '*':
            data_frame = pd.read_csv(dataPath + table_name + ".csv")
        else:
            column_list = self.visit(ctx.columnList())
            print(column_list)
            data_frame = pd.read_csv(dataPath + table_name + ".csv", usecols=column_list)

        return data_frame
    
    def visitColumnList(self, ctx):
        columns = []
        for col in ctx.column():
            id = self.visit(col)
            if id != None: columns.append(id)
        return columns

    def visitColumn(self, ctx):
        if ctx.getChildCount() == 1:
            return ctx.ID().getText()
        else:
            print(ctx.getChild(0).getText(), ctx.getChild(1).getText(), ctx.getChild(2).getText())

    def visitExpression(self, ctx):
        print("enters")
        if ctx.ID():
            print(ctx.ID().getText())
            return ctx.ID().getText()

        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':  # Phar
            self.visit(ctx.getChild(1))

        elif ctx.getChildCount() == 3:  # Binary operations
            column_id = self.visit(ctx.getChild(0))
            operator = ctx.getChild(1).getText()
            num = self.visit(ctx.getChild(2))
            print(column_id, operator, num)
    
        else:
            raise NotImplementedError("Expression not supported: " + ctx.getText())

    


def execute_query(query):
    
    input_stream = InputStream(query)
    lexer = lcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = lcParser(token_stream)

    tree = parser.select()

    eval_visitor = EvalVisitor()
    result = eval_visitor.visit(tree)

    return result

def main():
    st.title("PandaQ")

    query_input = st.text_area("Ingrese su consulta SQL:", height=20)

    # Agregar un botón para enviar la consulta
    if st.button("Enviar Consulta"):
        # Verificar si la consulta no está vacía
        if query_input.strip():
            result_df = execute_query(query_input)
            # Mostrar los resultados en una tabla
            st.write("Resultados de la Consulta:")
            st.dataframe(result_df)
        else:
            st.warning("Por favor, ingrese una consulta antes de enviar.")

if __name__ == "__main__":
    main()