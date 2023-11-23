from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor
import streamlit as st
import pandas as pd

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
    expressions = [self.visit(expr) for expr in ctx.expression()]
    return expressions

def visitExpression(self, ctx):
    if ctx.ID():
        return ctx.ID().getText()
    elif ctx.getChildCount() == 3:  # Binary operations
        left_operand = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right_operand = self.visit(ctx.getChild(2))
        return f"{left_operand} {operator} {right_operand}"
    elif ctx.getChildCount() == 4:  # Parentheses
        return self.visit(ctx.getChild(1))
    elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == 'as':  # Alias
        return f"{self.visit(ctx.getChild(0))} as {ctx.ID().getText()}"
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