from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor
import streamlit as st
import pandas as pd

#TODO
####################################################
# Canviar nom constraintList?
# Num a gramatica
# Acabar implementacio INNER JOIN
####################################################

dataPath = 'data/'

class EvalVisitor(lcVisitor):

    def __init__(self):
        self.newCols = []
        self.newColsNames = []
        self.tableName = None
        self.dataFrame = None
    
    def visitSelect(self, ctx):
        
        self.tableName = ctx.ID().getText()

        if ctx.getChild(1).getText() == '*':
            data_frame = pd.read_csv(dataPath + self.tableName + ".csv")
        else:
            column_list = self.visit(ctx.columnList())
            data_frame = pd.read_csv(dataPath + self.tableName + ".csv", usecols=column_list)
            for id, data in zip(self.newColsNames, self.newCols):
                data_frame[id] = data

        self.dataFrame = data_frame

        if ctx.conditionList():
            conditionStr = self.visit(ctx.conditionList())
            data_frame = data_frame.query(conditionStr)

        if ctx.constraintList():
            constraintsIDs, constraintOrders = self.visit(ctx.constraintList())
            data_frame = data_frame.sort_values(by=constraintsIDs, ascending=constraintOrders)

        return data_frame
    
    def visitConditionList(self, ctx):
        conditionList = []
        for condition in ctx.condition():
            conditionList.append(self.visit(condition))
        
        conditionStr = " and ".join(conditionList)
        return conditionStr

    def visitEquals(self, ctx):
        return ctx.getChild(0).getText() + " == " + ctx.getChild(2).getText()
    
    def visitMinor(self, ctx):
        return ctx.getChild(0).getText() + " < " + ctx.getChild(2).getText()
    
    def visitNotEquals(self, ctx):
        return "not " + ctx.getChild(1).getText() + " == " + ctx.getChild(3).getText()
    
    def visitNotMinor(self, ctx):
        return "not " + ctx.getChild(1).getText() + " < " + ctx.getChild(3).getText()

    def visitConstraintList(self, ctx):
        constraintIDs = []
        constraintOrders = []
        for constraint in ctx.constraint():
            id = constraint.ID().getText()
            order = constraint.getChild(1).getText()

            constraintIDs.append(id)
            constraintOrders.append(order == "asc")
        
        return constraintIDs, constraintOrders

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
            newColumnName = ctx.getChild(2).getText()
            self.newColsNames.append(newColumnName)
            newColumn = self.visit(ctx.getChild(0))
            self.newCols.append(newColumn)

    def visitIdentifier(self, ctx):
        return ctx.ID().getText()

    def visitMult(self, ctx):
        column_id = self.visit(ctx.getChild(0))
        num = ctx.getChild(2).getText()
        data_frame = pd.read_csv(dataPath + self.tableName + ".csv", usecols=[column_id])
        data_frame = data_frame * float(num)
        return data_frame


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
    
    if st.button("Enviar Consulta"):
        
        if query_input:
            result_df = execute_query(query_input)
            
            st.write("Resultados de la Consulta:")
            st.dataframe(result_df)
        else:
            st.warning("Por favor, ingrese una consulta antes de enviar.")

if __name__ == "__main__":
    main()