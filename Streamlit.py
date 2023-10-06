import streamlit as st
from simpleai.search import CspProblem, backtrack

st.write("# Cryptoarithmetic Puzzle")
woord1 = st.text_input("Geef het eerste woord")
woord2 = st.text_input("Geef het tweede woord")
woord3 = st.text_input("Geef het derde woord")

knop = st.button("Los Op")

if knop:
    input1 = woord1
    input2 = woord2
    resultaat = woord3

    # Definieer invoervariabelen en resultaatvariabele
    variables = list(set(input1 + input2 + resultaat))

    # Domeinen voor variabelen
    domains = {var: list(range(1, 10)) for var in variables}

    def constraint_unique(variables, values):
        return len(values) == len(set(values))

    def constraint_add(variables, values):
        karakter_naar_uitkomst = {char: values[i] for i, char in enumerate(variables)}

        factor1 = int(''.join([str(karakter_naar_uitkomst[char]) for char in input1]))
        factor2 = int(''.join([str(karakter_naar_uitkomst[char]) for char in input2]))
        result = int(''.join([str(karakter_naar_uitkomst[char]) for char in resultaat]))

        return factor1 + factor2 == result

    constraints = [
        (variables, constraint_unique),
        (variables, constraint_add),
    ]

    problem = CspProblem(variables, domains, constraints)

    output = backtrack(problem)
    print('\nSolutions:', output)
    st.write("# De oplossing")
    for i, j in output.items():
        st.write(i , "=", j)