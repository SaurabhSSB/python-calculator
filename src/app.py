import streamlit as st
from Calculator import calculate

def main():
    st.title("Simple Calculator")

    num1 = st.number_input("Enter the first number:", format="%d", step=1)
    num2 = st.number_input("Enter the second number:", format="%d", step=1)
    operator = st.selectbox("Select operation:", ["+", "-", "*", "/", "//", "**", "%"])

    if st.button("Calculate"):
        try:
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    st.error("Cannot divide by zero")
                else:
                    result = num1 / num2
            elif operator == "//":
                if num2 == 0:
                    st.error("Cannot divide by zero")
                else:
                    result = num1 // num2
            elif operator == "**":
                result = num1 ** num2
            elif operator == "%":
                if num2 == 0:
                    st.error("Cannot divide by zero")
                else:
                    result = num1 % num2
            else:
                st.error("Please enter a valid operator")

            if 'result' in locals():
                st.success(f"The result of {num1} {operator} {num2} is: {result}")

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()