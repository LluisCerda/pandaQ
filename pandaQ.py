from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

'''
example:

select first_name, last_name, job_title, department_name 
from employees inner join departments on department_id = department_id 
inner join jobs on job_id = job_id where job_title = Programmer order by first_name asc;
'''

#TODO
####################################################
# Control de errors
# revisar visit Minor, not Minot, not Equal
# Només hi ha implementada la multiplicacio
# Canviar nom constraintList?
# Num a gramatica
# ReadME.md
####################################################

dataPath = 'data/'
asignations = {}

class EvalVisitor(lcVisitor):

    def __init__(self):
        self.dataFrame = None

    def visitRoot(self, ctx):

        if isinstance(ctx.assignation(), lcParser.AssignationContext):
            return self.visitAssignation(ctx.assignation())
        
        elif isinstance(ctx.select(), lcParser.SelectContext):
            return self.visitSelect(ctx.select())
        
        elif isinstance(ctx.plot(), lcParser.PlotContext):
            return self.visitPlot(ctx.plot())

    def visitPlot(self, ctx):
        tableName = ctx.ID().getText()
        if 'asignations' in st.session_state:
            if tableName in st.session_state.asignations:

                dataFrame = st.session_state.asignations[tableName]

                numeric_columns = dataFrame.select_dtypes(include='number')
                fig, ax = plt.subplots()
                numeric_columns.plot(ax=ax, kind='line')
                st.pyplot(fig)

            #else Error no hi ha "tableName" definit
        #else Error no hi ha asignacions fetes

    def visitAssignation(self, ctx):
        result = self.visit(ctx.select())
        if 'asignations' not in st.session_state:
            st.session_state.asignations = {}
        st.session_state.asignations[ctx.ID().getText()] = result 
        return result

    
    def visitSelect(self, ctx):
        
        tableName = ctx.ID().getText()
        if 'asignations' in st.session_state:        
            if tableName in st.session_state.asignations:
                self.dataFrame = st.session_state.asignations[tableName]
            else: self.dataFrame = pd.read_csv(dataPath + ctx.ID().getText() + ".csv")
        else: self.dataFrame = pd.read_csv(dataPath + ctx.ID().getText() + ".csv")

        columns = self.visit(ctx.columnList())
        print(columns)

        if ctx.innerJoinList():
            self.visit(ctx.innerJoinList())

        if ctx.conditionList():
            conditionStr = self.visit(ctx.conditionList())
            print(conditionStr)
            print(self.dataFrame)
            self.dataFrame = self.dataFrame.query(conditionStr)

        if ctx.constraintList():
            constraintsIDs, constraintOrders = self.visit(ctx.constraintList())
            self.dataFrame = self.dataFrame.sort_values(by=constraintsIDs, ascending=constraintOrders)

        return self.dataFrame[columns]
    
    def visitInnerJoinList(self, ctx):

        for innerJoin in ctx.innerJoin():

            table = innerJoin.getChild(2).getText()
            onId = innerJoin.getChild(4).getText()

            newDataFrame = pd.read_csv(dataPath + table + ".csv")
            self.dataFrame = self.dataFrame.merge(newDataFrame, on=onId, how='inner')
    
    def visitConditionList(self, ctx):
        conditionList = []
        for condition in ctx.condition():
            conditionList.append(self.visit(condition))
        
        conditionStr = " and ".join(conditionList)
        return conditionStr

    def visitEquals(self, ctx):
        if not isNumber(ctx.getChild(2).getText()):
            return ctx.getChild(0).getText() + " == " + "'" + ctx.getChild(2).getText() + "'"
        else: return ctx.getChild(0).getText() + " == " + ctx.getChild(2).getText() 
    
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
        
        if ctx.getChild(0).getText() == '*': return self.dataFrame.columns
        columns = []
        for col in ctx.column():
            columns.append(self.visit(col))

        return columns

    def visitColumn(self, ctx):
        if ctx.getChildCount() == 1:
            return ctx.ID().getText()
        else:
            newColumnName = ctx.getChild(2).getText()
            newColumn = self.visit(ctx.getChild(0))
            self.dataFrame[newColumnName] = newColumn
            return newColumnName

    def visitMult(self, ctx):
        oldColumn = self.dataFrame[self.visit(ctx.getChild(0))]
        return oldColumn * float(ctx.getChild(2).getText())
    
    def visitIdentifier(self, ctx):
        return ctx.ID().getText()

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def execute_query(query):
    
    input_stream = InputStream(query)
    lexer = lcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = lcParser(token_stream)

    tree = parser.root()

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