from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from antlr4.error.ErrorListener import ErrorListener

asignations = {}

####################################################
# TODO
# Format pep8
####################################################

# Parser custom error Listener


class MyErrorListener(ErrorListener):

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax Error: {msg}")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise Exception()

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise Exception()

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise Exception()


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

        else:
            st.error("Error! Expresion no soportada.")
            return None

    def visitPlot(self, ctx):
        tableName = ctx.ID().getText()
        if 'asignations' in st.session_state:
            if tableName in st.session_state.asignations:

                dataFrame = st.session_state.asignations[tableName]

                numeric_columns = dataFrame.select_dtypes(include='number')
                fig, ax = plt.subplots()
                numeric_columns.plot(ax=ax, kind='line')
                st.pyplot(fig)

            else:
                st.error(f"Error! {tableName} no esta definido.")
        else:
            st.error("Error! No hay asignaciones echas.")

    def visitAssignation(self, ctx):
        result = self.visit(ctx.select())
        if 'asignations' not in st.session_state:
            st.session_state.asignations = {}
        st.session_state.asignations[ctx.ID().getText()] = result
        return result

    def visitSelect(self, ctx):

        tableName = ctx.ID().getText()

        # FROM
        if 'asignations' in st.session_state and tableName in st.session_state.asignations:
            self.dataFrame = st.session_state.asignations[tableName]
        else:
            try:
                self.dataFrame = pd.read_csv(
                    'data/' + ctx.ID().getText() + ".csv")
            except:
                st.error(f"Error! {tableName} no existe.")
                return None

        # INNER JOIN
        if ctx.innerJoinList():
            try:
                self.visit(ctx.innerJoinList())
            except:
                st.error("Error! Misspelled or non existent inner join ID")
                return None

        # WHERE
        if ctx.conditionList():
            try:
                self.visit(ctx.conditionList())
            except:
                st.error("Error! Misspelled or non existent condition ID")
                return None

        # SUBQUERY
        if (ctx.subQuery()):
            inDataFrame = self.visit(ctx.subQuery())

        # ORDER BY
        if ctx.orderingList():
            try:
                self.visit(ctx.orderingList())
            except:
                st.error("Error! Misspelled or non existent ordering ID")
                return None

        # COLUMNS
        columns = self.visit(ctx.columnList())

        try:
            self.dataFrame = self.dataFrame[columns]
        except:
            st.error(f"Error! ID de columna no existente en {tableName}.")
            return None

        return self.dataFrame

    def visitSubQuery(self, ctx):
        saveDataFrame = self.dataFrame
        newDataFrame = self.visit(ctx.select())

        onId = ctx.ID().getText()
        self.dataFrame = saveDataFrame.merge(
            newDataFrame, on=onId, how='inner')

    def visitInnerJoinList(self, ctx):

        for innerJoin in ctx.innerJoin():

            table = innerJoin.getChild(2).getText()
            onId = innerJoin.getChild(4).getText()

            if 'asignations' in st.session_state and table in st.session_state.asignations:
                newDataFrame = st.session_state.asignations[table]
            else:
                newDataFrame = pd.read_csv('data/' + table + ".csv")

            self.dataFrame = self.dataFrame.merge(
                newDataFrame, on=onId, how='inner')

    def visitConditionList(self, ctx):
        conditionList = []
        for condition in ctx.condition():
            conditionList.append(self.visit(condition))

        conditionStr = " and ".join(conditionList)

        self.dataFrame = self.dataFrame.query(conditionStr)

    def visitEquals(self, ctx):
        if not isNumber(ctx.getChild(2).getText()):
            return ctx.getChild(0).getText() + " == " + "'" + ctx.getChild(2).getText() + "'"
        else:
            return ctx.getChild(0).getText() + " == " + ctx.getChild(2).getText()

    def visitMinor(self, ctx):
        if not isNumber(ctx.getChild(2).getText()):
            return ctx.getChild(0).getText() + " < " + "'" + ctx.getChild(2).getText() + "'"
        return ctx.getChild(0).getText() + " < " + ctx.getChild(2).getText()

    def visitNotEquals(self, ctx):
        if not isNumber(ctx.getChild(3).getText()):
            return "not " + ctx.getChild(1).getText() + " == " + "'" + ctx.getChild(3).getText() + "'"
        return "not " + ctx.getChild(1).getText() + " == " + ctx.getChild(3).getText()

    def visitNotMinor(self, ctx):
        if not isNumber(ctx.getChild(3).getText()):
            return "not " + ctx.getChild(1).getText() + " < " + "'" + ctx.getChild(3).getText() + "'"
        return "not " + ctx.getChild(1).getText() + " < " + ctx.getChild(3).getText()

    def visitOrderingList(self, ctx):
        orderIDs = []
        orders = []
        for order in ctx.order():

            id = order.ID().getText()
            if order.getChildCount() == 2:
                orderStr = order.getChild(1).getText()
            else:
                orderStr = "asc"

            orderIDs.append(id)
            orders.append(orderStr == "asc")

        self.dataFrame = self.dataFrame.sort_values(
            by=orderIDs, ascending=orders)

    def visitColumnList(self, ctx):

        if ctx.getChild(0).getText() == '*':
            return self.dataFrame.columns
        columns = []
        for col in ctx.column():
            columns.append(self.visit(col))
        return columns

    def visitColumn(self, ctx):

        if ctx.getChildCount() == 1:
            return ctx.ID().getText()

        newColumnName = ctx.getChild(2).getText()
        newColumn = self.visit(ctx.getChild(0))
        self.dataFrame[newColumnName] = newColumn
        return newColumnName

    def visitMult(self, ctx):
        oldColumn = self.visit(ctx.expression())
        return oldColumn * float(ctx.NUM().getText())

    def visitSum(self, ctx):
        oldColumn = self.visit(ctx.expression())
        return oldColumn + float(ctx.NUM().getText())

    def visitSubst(self, ctx):
        oldColumn = self.visit(ctx.expression())
        return oldColumn - float(ctx.NUM().getText())

    def visitDiv(self, ctx):
        oldColumn = self.visit(ctx.expression())
        return oldColumn / float(ctx.NUM().getText())

    def visitIdentifier(self, ctx):
        return self.dataFrame[ctx.ID().getText()]


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def execute_query(query):

    try:
        input_stream = InputStream(query)
        lexer = lcLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = lcParser(token_stream)
        parser.addErrorListener(MyErrorListener())
        tree = parser.root()

        eval_visitor = EvalVisitor()
        result = eval_visitor.visit(tree)

    except Exception as e:
        st.error(f"{e}")
        return None
    except:
        st.error(f"An unexpected error occurred: {e}")
        return None

    return result


def main():

    st.title("PandaQ")
    query_input = st.text_area("Ingrese su consulta SQL:", height=20)

    if st.button("Enviar Consulta"):

        if query_input:
            result_df = execute_query(query_input)

            if result_df is not None:
                st.write("Resultados de la Consulta:")
                st.dataframe(result_df)
        else:
            st.warning("Error! Ingrese una consulta antes de enviar.")


if __name__ == "__main__":
    main()
